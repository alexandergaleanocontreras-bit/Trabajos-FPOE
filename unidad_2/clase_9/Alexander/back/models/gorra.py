from django.db import models

class Gorra(models.Model):
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.marca} - {self.color}"