from rest_framework import serializers 
from .models import Business

class BusinessSearializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields =  ('id', 'name', 'industry')


)