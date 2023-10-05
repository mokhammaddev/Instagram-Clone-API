from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Contact
from account.models import Account


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'author', 'name', 'phone_number', 'created_date']


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'created_date']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        author = Account.objects.filter(phone=phone_number).first()

        if author:
            attrs['author'] = author

            existing_contacts = Contact.objects.filter(account=self.context['request'].user)
            for contact in existing_contacts:
                if contact.author == attrs.get('author'):
                    raise ValidationError({'message': 'You already added this contact'})

            return attrs

        raise ValidationError({'message': 'Account is not found with this number'})

    def create(self, validated_data):
        request = self.context['request']
        validated_data['account'] = request.user
        instance = super().create(validated_data)
        return instance
