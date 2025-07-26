from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        #! read only filed not show but add
        read_only_fields = ['institute']
        #! write only field can write but not show in get
        extra_kwargs = {
            'location': {'write_only': True},
            
        }
    
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['age'] < 18:
            raise serializers.ValidationError("Children not allowed")
        
        if data['name'][0].islower():
            raise serializers.ValidationError("Fitst word can not be in Uppercase")
        return data