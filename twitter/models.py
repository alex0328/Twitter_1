from django.db import models
from django.contrib.auth.models import User

TWITER_MAX_LENGTH = 280

# Create your models here.
class Tweet(models.Model):
    content = models.CharField(max_length=TWITER_MAX_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'[{self.creation_date}] ' \
               f'TWEET by {self.author}: {self.content[:20]}'