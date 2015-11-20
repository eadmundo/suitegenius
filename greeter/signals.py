from django.db.models.signals import post_save
from django.dispatch import receiver
from greeter.models import Message
import json
import requests
import os
from rq import Queue
import redis
from django.conf import settings


def send_message(slack_username, message):
    session = requests.Session()
    payload = {
        'username': 'suite-genius-doorman',
        'channel': '@{}'.format(slack_username),
        'text': message
    }
    r = session.post(
        settings.SLACK_WEBHOOK,
        data=json.dumps(payload)
    )
    if r.status_code != 200:
        print r.content


def get_redis():
    return redis.from_url(os.environ.get("REDIS_URL"))


@receiver(post_save)
def receive_message(sender, **kwargs):
    if issubclass(sender, Message):
        conn = get_redis()
        q = Queue(connection=conn)
        msg = kwargs['instance']
        q.enqueue(
            send_message,
            msg.recipient.slack_username,
            msg.body
        )
