from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(blank=True, null=True)
    cell_number = models.CharField(max_length=255, blank=True, null=True)
    slack_username = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=1600)
    recipient = models.ForeignKey(Member)

    class Meta:
        ordering = ('created',)
