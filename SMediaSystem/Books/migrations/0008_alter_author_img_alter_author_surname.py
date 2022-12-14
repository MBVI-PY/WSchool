# Generated by Django 4.0.5 on 2022-10-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_genreimg_genre_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='img',
            field=models.ManyToManyField(to='Books.authorimg'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
