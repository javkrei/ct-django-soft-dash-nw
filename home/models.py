from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Audio(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.audio_file.name