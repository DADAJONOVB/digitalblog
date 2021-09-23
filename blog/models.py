from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls.base import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published","Published"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts',blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    rasm = models.ImageField(upload_to='rasmlar/', blank=True)


    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
        args=[self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug]
        )


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',blank=True)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('created',)


    def __str__(self):
        return f"{self.author} : {self.body}"