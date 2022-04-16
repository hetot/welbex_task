from django.db import models

# Create your models here.
class Sample(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    distance = models.FloatField()

    def __str__(self):
        return self.name
