from django.db import models
from django.utils import timezone

# Create your models here.


class ChatSession(models.Model):
    session_id = models.CharField(max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"session {self.session_id}"


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    session = models.ForeignKey(
        ChatSession, related_name="messages", on_delete=models.CASCADE
    )
    prompt = models.TextField()
    context = models.TextField(blank=True)
    response = models.TextField()
    

    def __str__(self) -> str:
        return f"Message at {self.timestamp} in session {self.session.session_id}"
