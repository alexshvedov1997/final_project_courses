from django.db import models

# Create your models here.

class WarpGames(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    price = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class BelconsoleGames(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    price = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)