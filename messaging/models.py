from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    content = models.TextField()
    shipping_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.sender} a {self.receiver}"
