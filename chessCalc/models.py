from django.db import models

class User(models.Model):
    username = models.TextField()
    mail = models.EmailField()
    password = models.TextField()
