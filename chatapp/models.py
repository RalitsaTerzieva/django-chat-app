from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("chatroom", kwargs={"slug": self.slug})
    

class ChatMessage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message_content
    
    class Meta:
        ordering = ('date',)
        
        
