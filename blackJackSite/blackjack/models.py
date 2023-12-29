from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' score: ' + str(self.score)