from django.db import models

class Visit(models.Model):
	name = models.CharField(max_length=100)
	totalCount = models.PositiveIntegerField(default=0)
	dailyCount = models.PositiveIntegerField(default=0)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name