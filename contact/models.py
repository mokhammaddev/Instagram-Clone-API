from django.db import models
from chat.models import Message
from django.core.validators import RegexValidator


class Contact(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='account')
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='phone_account')
    name = models.CharField(max_length=221)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
