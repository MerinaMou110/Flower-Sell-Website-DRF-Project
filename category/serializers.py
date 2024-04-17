from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'

class flowerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    categories = serializers.StringRelatedField(many=True)
   
    class Meta:
        model = models.flower
        fields = '__all__'