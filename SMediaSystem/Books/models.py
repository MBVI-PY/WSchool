
from unittest.util import _MAX_LENGTH
from django.db import models

class AuthorIMG(models.Model):
    file = models.FileField(upload_to='author_img/')

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name        = "Фотография для автора"
        verbose_name_plural = "Фотографии для авторов"

class Author(models.Model):
    
    name       = models.CharField(max_length=24)
    surname    = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=24)
    summary    = models.CharField(max_length=2000, null=True)
    img        = models.ManyToManyField(AuthorIMG)

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.patronymic, self.surname)

    
    def display_file(self):
        return ', '.join([str(file.file) for file in self.img.all()])

    display_file.short_description  = 'Фотография автора'

    class Meta:
        verbose_name        = "Автор"
        verbose_name_plural = "Авторы"


class GenreIMG(models.Model):
    file = models.FileField(upload_to='genre_img')

    def __str__(self):
        return str(self.file)
    
    class Meta:
        verbose_name        = "Фотография для жанра"
        verbose_name_plural = "Фотографии для жанров"

class Genre(models.Model):
    name = models.CharField(max_length=24)
    summary = models.CharField(max_length=2000, null=True)
    img = models.ManyToManyField(GenreIMG)
    def __str__(self):
        return self.name

    def display_file(self):
        return ', '.join([str(file.file) for file in self.img.all()])

    display_file.short_description  = 'Фотография жанра'

    class Meta:
        verbose_name        = "Жанр"
        verbose_name_plural = "Жанры"


class Language(models.Model):
    language = models.CharField(max_length=24)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name        = "Язык"
        verbose_name_plural = "Языки"

    
class KeyWord(models.Model):
    keyword = models.CharField(max_length=24)

    def __str__(self):
        return self.keyword
    
    class Meta:
        verbose_name        = "Ключевое слово"
        verbose_name_plural = "Ключевые слова"


class IMG(models.Model):
    file = models.FileField(upload_to='book_img/')

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name        = "Фотография для книги"
        verbose_name_plural = "Фотографии для книг"

class Book(models.Model):
    title   = models.CharField(max_length=200)
    doc     = models.FileField(upload_to='book_pdf/')
    summary = models.TextField()
    author  = models.ManyToManyField(Author)
    genre   = models.ManyToManyField(Genre)
    lang    = models.ForeignKey(Language, on_delete = models.CASCADE)
    keyword = models.ManyToManyField(KeyWord)
    img     = models.ManyToManyField(IMG)

    def display_author(self):
        return ', '.join(["{0} {1} {2}".format(author.name, author.patronymic ,author.surname) for author in self.author.all()])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def display_keyword(self):
        return ', '.join([keyword.keyword for keyword in self.keyword.all()])

    def display_file(self):
        return ', '.join([str(file.file) for file in self.img.all()])

    display_file.short_description      = 'Фотография для книги'
    display_author.short_description    = 'Авторы'
    display_genre.short_description     = 'Жанры'
    display_keyword.short_description   = 'Ключевое слово'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Книга"
        verbose_name_plural = "Книги"

"""class BookImg(models.Model):
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    file  = models.ManyToManyField(IMG)

    def display_file(self):
        return ', '.join([file.file for file in self.file.all()])

    display_file.short_description = 'Фотография для книги'"""