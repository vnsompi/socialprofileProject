from rest_framework import serializers
from . import  models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['id','email','name','bio','password', 'profile_image',
                  'date_joined']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedItem
        fields = ['id','user_profile','content','image','created_at','updated_at', 'is_public']
        extra_kwargs = {'user_profile': {'read_only': True}}
