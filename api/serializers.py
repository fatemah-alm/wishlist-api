
from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='api-detail', lookup_field = 'id')
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField(method_name='getFavourited')
    class Meta:
        model = Item
        fields = ['name','description', 'image', 'detail', 'added_by', 'favourited']
    def getFavourited(self, item:Item):
        return len(item.favoriteitem_set.all())
        
     


class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField(method_name='getUsers')
    class Meta:
        model = Item
        fields = '__all__'
    def getUsers(self,item:Item):
        users = []
        for item in item.favoriteitem_set.all():
            users.append(item.user.username)
        return users

