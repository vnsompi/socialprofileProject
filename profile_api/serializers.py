from rest_framework import serializers
from . import  models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['id','email','name','bio', 'profile_image',
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

