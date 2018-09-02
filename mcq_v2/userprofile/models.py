from django.db import models

from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()

# Create your models here.



class profile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	college=models.CharField(max_length=255)
	year=models.CharField(max_length=255)
	branch=models.CharField(max_length=255)



	def __str__(self):
		return self.name
