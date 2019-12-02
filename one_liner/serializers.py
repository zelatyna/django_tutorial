from .models import One_liner, CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User



# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     #updates = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = User
#         fields = ['user_name', 'id']


class UserSerializer(serializers.ModelSerializer):
    updates = serializers.PrimaryKeyRelatedField(many=True, queryset=One_liner.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone_number', 'updates']

class OneLinerSerializer(serializers.HyperlinkedModelSerializer):

    #author = UserSerializer(many=False, read_only=True)
    #user_id = serializers.IntegerField(write_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = One_liner
        fields = ['pub_date', 'one_liner_text', 'author']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #validated_data['author'] = User.objects.filter(id = validated_data.pop('user_id')).first()
        return One_liner.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.one_liner_text = validated_data.get('one_liner_text', instance.one_liner_text)
    #     instance.pub_date = validated_data.get('pub_date', instance.pub_date)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.save()
    #     return instance
