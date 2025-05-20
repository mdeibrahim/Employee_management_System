from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employer model.
    """
    # Make user field read-only as it will be set automatically based on the logged-in user.
    # We can display user's email for better readability if needed, though not strictly required by the prompt.
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # Alternatively, to show more user details (e.g., email) instead of just ID:
    # user = serializers.StringRelatedField(read_only=True) 
    # user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail') # If you have a user detail endpoint

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
        read_only_fields = ['id', 'user', 'created_at', 'updated_at'] # User is set in the view

    def create(self, validated_data):
        """
        Override create to automatically set the user from the request.
        The 'user' field is passed in the context from the view.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    # You can add custom validation methods here if needed, e.g.,
    # def validate_phone_number(self, value):
    #     if not value.isdigit(): # Example: ensure phone number contains only digits
    #         raise serializers.ValidationError("Phone number must contain only digits.")
    #     if len(value) < 10:
    #          raise serializers.ValidationError("Phone number seems too short.")
    #     return value
