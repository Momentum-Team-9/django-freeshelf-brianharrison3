# Generated by Django 3.2.4 on 2021-08-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='book', to='books.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='books.Author'),
        ),
    ]