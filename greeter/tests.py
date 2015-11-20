import fudge
import redis
import fakeredis
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from greeter.models import Message


class VeryFakeStrictRedis(fakeredis.FakeStrictRedis, redis.StrictRedis):
    # have to do it like this because of how RQ checks Redis
    pass


class GreeterTests(APITestCase):

    fixtures = ['greeter']

    def test_list_members(self):
        url = reverse('member-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['slack_username'], 'eadmundo')

    @fudge.patch('greeter.signals.get_redis')
    def test_create_message(self, get_redis):
        (get_redis.is_callable()
            .returns(VeryFakeStrictRedis()))
        url = reverse('message-list')
        data = {
            'recipient': 1,
            'body': 'Oh Hai There'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().body, 'Oh Hai There')
