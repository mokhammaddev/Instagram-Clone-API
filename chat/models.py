from django.db import models
from account.models import Account


class Room(models.Model):
    name = models.CharField(max_length=221)
    user = models.ManyToManyField(Account, related_name='user_room')

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_message')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}'s message in {self.room}"
