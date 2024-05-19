from django.db import models

class Simulation(models.Model):
    simulation_id = models.IntegerField(primary_key=True)
    simulation_name = models.CharField(max_length=255)
    company_id = models.IntegerField()
    company_name = models.CharField(max_length=255)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    signup_datetime = models.FloatField()
    progress_percent = models.IntegerField()
