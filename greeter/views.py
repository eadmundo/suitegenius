from rest_framework import viewsets
from rest_framework import filters
from greeter.models import Member, Message
from greeter.serializers import (
    MemberSerializer, MessageSerializer
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'last_name', 'first_name',
        'slack_username', 'email_address'
    )
