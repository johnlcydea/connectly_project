from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model


class Post(models.Model):
    # Model representing blog posts or articles
    title = models.CharField(max_length=255, default="Default Title")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to Django's User model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
