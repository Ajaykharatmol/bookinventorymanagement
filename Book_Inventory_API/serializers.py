from Book_Inventory_APP.models import Books
from rest_framework import serializers




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'