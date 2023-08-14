from django.db import models

# Create your models here.

class Blog(models.Model):
	Title=models.CharField(max_length=100)
	Content=models.CharField(max_length=100)
	Created_at=models.DateTimeField()
	Updated_at=models.DateTimeField()


	def __str__(self):
		return self.Title+' '+self.Created_at