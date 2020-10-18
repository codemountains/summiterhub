from django.db import models
from summiterhub import settings_core
import uuid


def upload_path(instance, filename):
	ext = filename.split('.')[-1]
	return '/'.join([
		'news_image',
		str(instance.id)+str('.')+str(ext)
	])


class News(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	attached_image = models.ImageField(blank=True, null=True, upload_to=upload_path)

	class Meta:
		verbose_name_plural = 'News'

	def __str__(self):
		return self.title


class ReadNews(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='read_news_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	news_id = models.ForeignKey(
		News,
		related_name='read_news_news_id',
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name_plural = 'ReadNews'

	def __str__(self):
		return str(self.news_id) + '(' + str(self.user_id) + ')'
