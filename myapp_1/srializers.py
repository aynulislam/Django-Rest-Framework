from rest_framework import serializers
from .models import EmCategory,EmEmail,EmReceiver,EmGroup,EmUser,EmUserGroup,ScUser,GnGroupType

class EmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmCategory
        fields = "__all__"


class EmEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmEmail
        fields = "__all__"


class EmReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmReceiver
        fields = "__all__"


class EmGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmGroup
        fields = "__all__"

class EmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmUser
        fields = "__all__"

class EmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmUserGroup
        fields = "__all__"

class ScUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        fields = "__all__"


class GnGroupTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GnGroupType
        fields = "__all__"


