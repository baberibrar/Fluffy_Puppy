from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

size_choices = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=10, choices=size_choices)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)


class Dog(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    favoritefood = models.CharField(max_length=100, null=True, blank=True)
    favoritetoy = models.CharField(max_length=100, null=True, blank=True)
