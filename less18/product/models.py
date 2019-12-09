from django.db import models

# Create your models here.
class Sale(models.Model):
	saleType = models.CharField(max_length=128)
	pers = models.IntegerField()

	def __str__(self): #позволшяет указать как будет выглядеть запись внутри админки
		return '{} => {}'.format(self.saleType, self.pers)

class Good(models.Model):
	title = models.CharField(max_length=128)
	desc = models.TextField()
	price = models.IntegerField()
	sale = models.ForeignKey(Sale, on_delete=models.SET_NULL,  null=True)

	def __str__(self): #позволшяет указать как будет выглядеть запись внутри админки
		#return self.title
		return '{} => {}'.format(self.title, self.price)

