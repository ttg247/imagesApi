from rest_framework import serializers 
from app.models import Picture
 
 
class Pictures(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'name', 'src', 'description', 'price']