from django.db import models
from django.contrib.auth.models import User
from pins.models import Pin

class Love(models.Model):
    """
    Love model, related to 'owner' and 'pin'.
    'owner' is a User instance, 'pin' is a Post instance and 'love' is a Like instance.
    'unique_together' makes sure a user can't lob the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.ForeignKey(
        Pin, related_name='loves', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'pin']

    def __str__(self):
        return f'{self.owner} {self.pin}'