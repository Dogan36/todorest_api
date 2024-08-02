from django.db import models
import datetime
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    
    def time_passed(self):
        today = date.today()
        time_diff = today - self.created_at
        return time_diff.days
    
