from django.db import models

# Create your models here.

from django.db import models


class Subject(models.Model):
	name = models.CharField(max_length=255)
	grade = models.CharField(max_length=2, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
	credit = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.name} - Grade: {self.grade}, Credit: {self.credit}"

