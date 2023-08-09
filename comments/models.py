from django.db import models
from django.contrib.auth.models import User
from pins.models import Pin


class Comment(models.Model):
    """
    Comment model, related to User and Pin
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content