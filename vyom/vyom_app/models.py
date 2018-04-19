from django.db import models

# Create your models here.

class Device(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	pin_code = models.IntegerField(null=False, blank=False)
	address = models.TextField(null=False, blank=False)
	longitude = models.DecimalField(max_digits=15, decimal_places=10)
	latitude = models.DecimalField(max_digits=15, decimal_places=10)
	web_address = models.CharField(max_length=255, null=False, blank=False)

	def __str__(self):
		return str(self.id)