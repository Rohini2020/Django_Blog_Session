from rest_framework import serializers
from .models import User

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","password","username","email","description","linkdin_url","contact_number",
                  "status"]

    def create(self,validated_data):
        user = User.objects.create_user(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            username=validated_data.pop('username'),
            password=validated_data.pop("password"),
            email=validated_data.pop('email'),
            description=validated_data.pop('description'),
            linkdin_url=validated_data.pop('linkdin_url'),
            contact_number=validated_data.pop('contact_number'),
            status=validated_data.pop('status')
        )
        return user