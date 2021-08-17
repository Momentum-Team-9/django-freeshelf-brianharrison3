from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="books"
    )
    release_date = models.DateField()

    def __repr__(self):
        return f"<Book title={self.title}>"

    def __str__(self) :
        return self.title

class Author (models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return f"<Author name={self.name}>"
    def __str__(self):
        return self.name
