from django.db import models
from django.utils import timezone


class Post(models.Model):
	author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
	title=models.CharField(max_length=250)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	image=models.ImageField(null=True,blank=True,height_field='height_field',width_field='width_field')
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post=models.ForeignKey('blog.post',on_delete=models.CASCADE,related_name='comments')
	author=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	approved_comment=models.BooleanField(default=False)

	def approved(self):
		self.approved_comment=True
		self.save()

	def __str__(self):
		return self.text