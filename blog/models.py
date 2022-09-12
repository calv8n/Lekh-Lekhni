from django.db import models
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null = True, blank = True, upload_to="images/")
    slug = models.SlugField()
    intro = models.TextField()
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']