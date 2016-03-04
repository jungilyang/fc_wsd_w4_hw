from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=40)
	#def __str__(self):
	#	return '{} 번째 카테고리명 : {}'.format(self.pk, self.name)


class Post(models.Model):
	# blog_post (appname_dbname)
	title = models.CharField(max_length=200)
	contents = models.TextField()
	tags = models.ManyToManyField('Tag')
	category = models.ForeignKey(Category, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	is_model_field = False

	def __str__(self):
		return '<{}>'.format(self.pk)
		# return '{}-{}-{}'.format(self.pk, self.title, self.contents)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	#def __str__(self):
	#	return '{}글의 {}번 댓글 - 내용 : {}'.format(self.post_id, self.id, self.content)

class Tag(models.Model):
	name = models.CharField(max_length=40)
	#def __str__(self):
	#	return '{}의 {} 태그'.format(self.post_id, self.name)