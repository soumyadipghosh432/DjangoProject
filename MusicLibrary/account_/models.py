from django.db import models

# Create your models here.
class Account(models.Model):
	userName = models.CharField(max_length=20)
	password = models.CharField(max_length=200)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	
	def __str__(self):
		return "{} : {}, {}".format(self.userName, self.lastName, self.firstName)
