from django.db import models

# Create your models here.
class Item(models.Model):
	product = models.CharField(max_length=200)
	product_name = models.CharField(max_length=200)
	label = models.CharField(max_length=200)
	product_price = models.FloatField(blank=False, null=False)

	def __str__(self):
		return self.product