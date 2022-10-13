from atexit import register
from django.contrib import admin
from .models import Author, Genre, Language, KeyWord, Book, IMG, AuthorIMG, GenreIMG

@admin.register(AuthorIMG)
class AuthorsIMG(admin.ModelAdmin):
    list_display = ('id', 'file')

@admin.register(Author)
class Authors(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'summary', 'display_file')

@admin.register(GenreIMG)
class GenresIMG(admin.ModelAdmin):
    list_display = ('id', 'file')

@admin.register(Genre)
class Genres(admin.ModelAdmin):
    list_display = ('id', 'name', 'summary', 'display_file')

@admin.register(Language)
class Languages(admin.ModelAdmin):
    list_display = ('id', 'language')

@admin.register(KeyWord)
class KeyWords(admin.ModelAdmin):
    list_display = ('id', 'keyword')

@admin.register(IMG)
class IMGs(admin.ModelAdmin):
    list_display = ('id', 'file')

@admin.register(Book)
class Books(admin.ModelAdmin):
    list_display = ('id', 'title', 'doc', 'display_author', 'display_genre', 'lang', 'display_keyword', 'summary', 'display_file')
# Register your models here.
