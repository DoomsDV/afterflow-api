from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='blog/portadas/',null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.title
