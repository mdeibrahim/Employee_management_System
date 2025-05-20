from django.db import models
from django.conf import settings # To get the AUTH_USER_MODEL

class Employer(models.Model):
    """
    Represents an Employer in the system.
    Each employer is linked to a specific user.
    """
    # The user who owns or created this employer entry.
    # A User can have multiple Employer entries.
    # If a User is deleted, their associated Employer entries will also be deleted (CASCADE).
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="employers" # Allows accessing employers from a user object (user.employers.all())
    )
    
    company_name = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254) # Standard email field
    phone_number = models.CharField(max_length=20) # Max length can be adjusted as needed
    address = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # Automatically set every time the object is saved

    def __str__(self):
        """
        String representation of the Employer model.
        """
        return f"{self.company_name} (Contact: {self.contact_person_name})"

    class Meta:
        ordering = ['-created_at'] # Default ordering for queries
        verbose_name = "Employer"
        verbose_name_plural = "Employers"

