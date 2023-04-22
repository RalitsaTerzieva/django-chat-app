from django.db import models
from django.urls import reverse


class ChatRoom(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("chatroom", kwargs={"slug": self.slug})
