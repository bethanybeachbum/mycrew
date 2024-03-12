from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f" {self.caption}"
    

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10) ])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") 
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug] )

    def __str__(self):
        return f" {self.title}"

