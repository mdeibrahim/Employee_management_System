from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    
    # Make user field read-only as it will be set automatically based on the logged-in user.
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # Alternatively, to show more user details (e.g., email) instead of just ID:
    

    class Meta:
        model = Employer
        fields = [
            'id', 
            'user', # The user (owner) of this employer record
            'company_name', 
            'contact_person_name', 
            'email', 
            'phone_number', 
            'address', 
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Override create to automatically set the user from the request.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    
