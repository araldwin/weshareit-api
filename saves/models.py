from django.db import models
from django.contrib.auth.models import User
from pins.models import Pin

class Save(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.ForeignKey(
        Pin, related_name='saves', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'pin']

    def __str__(self):
        return f'{self.owner} saved {self.pin}'
