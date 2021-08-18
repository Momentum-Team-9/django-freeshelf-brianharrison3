from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import SlugField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(
        "Author", related_name="authors"
    )
    description = models.CharField(max_length=255, null=True)
    release_date = models.DateField()



    def __repr__(self):
        return f"<Book title={self.title}>"

    def __str__(self) :
        return self.title

class Author (models.Model):
    name = models.CharField(max_length=255)
    # books = models.ManyToManyField(Book, related_name='book')

    def __repr__(self):
        return f"<Author name={self.name}>"
    def __str__(self):
        return self.name

