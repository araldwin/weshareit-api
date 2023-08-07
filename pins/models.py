from django.db import models
from django.contrib.auth.models import User

class Pin(models.Model):

    pin_category_choices = [
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('fashion', 'Fashion'),
        ('nature', 'Nature'),
        ('art', 'Art'),
        ('music', 'Music'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('books', 'Books'),
        ('health', 'Health'),
        ('fitness', 'Fitness'),
        ('movies', 'Movies'),
        ('gaming', 'Gaming'),
        ('crafts', 'Crafts'),
        ('cars', 'Cars'),
        ('pets', 'Pets'),
        ('animals', 'Animals'),
        ('home', 'Home'),
        ('education', 'Education'),
        ('outdoors', 'Outdoors'),
        ('photography', 'Photography'),
        ('others', 'Others'),
        # Add more categories here
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
            upload_to='images/', default='../default_post_chzmzw.jpg', blank=False)
    category = models.CharField(max_length=20, choices=pin_category_choices)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


