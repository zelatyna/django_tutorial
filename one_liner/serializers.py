from .models import One_liner, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user_name']


class OneLinerSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = One_liner
        fields = ['pub_date', 'one_liner_text', 'author']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return One_liner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.one_liner_text = validated_data.get('one_liner_text', instance.one_liner_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance
