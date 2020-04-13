from rest_framework import serializers
from rest_framework import prolist

class prolistSerializer(serializers.ModelSerializer):

    class Meta:
        model = prolist

     fields= '__all__'    