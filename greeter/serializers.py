from rest_framework import serializers
from greeter.models import Member, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
