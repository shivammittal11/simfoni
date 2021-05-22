from rest_framework import serializers

from user.models import ProductData, User


class ProductSerializer(serializers.ModelSerializer):
    # assign_to = serializers.SerializerMethodField()


    class Meta:
        model = ProductData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # assign_to = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = '__all__'