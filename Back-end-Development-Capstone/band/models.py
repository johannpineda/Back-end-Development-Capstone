from django.db import models
class Concert(models.Model):
    name=models.CharField(max_length=200)
    venue=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField()
    description=models.TextField(blank=True)
    def __str__(self): return f'{self.name} - {self.city}'
