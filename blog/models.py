from django.db import models
from taggit.managers import TaggableManager

class Blog(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=100000)
	date = models.DateField()
	tags = TaggableManager()


	def __str__(self):
		return self.title + self.description
