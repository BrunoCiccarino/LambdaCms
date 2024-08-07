from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title
