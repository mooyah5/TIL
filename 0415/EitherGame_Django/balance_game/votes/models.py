from django.db import models
from django.conf import settings

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=20)
    Issue_a = models.CharField(max_length=20)
    Issue_b = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    
    class Voting(models.TextChoices):
        A = 'A'
        B = 'B'
        
    voting = models.CharField(max_length=1, choices=Voting.choices)
    content = models.CharField(max_length=100)