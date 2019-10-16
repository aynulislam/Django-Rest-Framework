from rest_framework import serializers
from .models import EsUser,User,ScUser,GnGroupType,ChGroup,ChUserGroup,ChConversation, ChMessage,ChReceiver

class GnGroupTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GnGroupType
        fields = "__all__"


class ScUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsUser
        fields = "__all__"


class ChGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChGroup
        fields = "__all__"


class ChUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChUserGroup
        fields = "__all__"


class ChConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChConversation
        fields = "__all__"


class ChMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChMessage
        fields = "__all__"


class ChReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChReceiver
        fields = "__all__"


