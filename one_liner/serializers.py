from .models import One_liner, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user_name']


class OneLinerSerializer(serializers.HyperlinkedModelSerializer):
    #author = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='author')
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = One_liner
        fields = ['pub_date', 'one_liner_text', 'author']

