from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
# Create your models here.


class Posts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def publish(self):
        self.save()

    def comments(self):
        return self.comments.all()

    def get_absolute_url(self):
        return reverse('blogem:posts_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(
        'blogem.Posts', related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=25)
    content = models.TextField()

    app_comment = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blogem:post_list')

    def cmt_app(self):
        self.save()

    def __str__(self):
        return self.user
