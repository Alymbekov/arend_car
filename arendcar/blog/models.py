from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=255)
    number_of_seats = models.PositiveSmallIntegerField()
    body_type = models.CharField(max_length=50)
    year_of_production = models.PositiveSmallIntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name + ', ' + str(self.year_of_production)


# Create your models here.
