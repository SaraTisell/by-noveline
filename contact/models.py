from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    regarding_an_order = models.BooleanField(default=False)
    order_number = models.CharField(max_length=35, null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=400)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} | {self.title} | {self.created_at}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} | {self.created_at}'