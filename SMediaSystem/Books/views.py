
from typing import List

from django.shortcuts import render, HttpResponse
from .models import Book as B
from .models import Author as A
from .models import Genre as G
from .transform import TransformToRu, TransformToEn

BookModel = B.objects.in_bulk()
AuthorModel = A.objects.in_bulk()
GenreModel = G.objects.in_bulk()

ERRORS = {
    404: "Страница не найдена"
}

################################################################################################
# Отображающие функции
################################################################################################
def Index(request):
    context = {}
    BM = BookMethod(id = id)
    if request.method == "POST":
        BookRequest = str(request.POST.get("BookRequest"))
        context['AllBooks'] = SearchBook(BookRequest, BookModel)
        return render(request,'Books/index.html', context)

    context['AllBooks'] = BM.AllBooks()
    return HttpResponse()
    return render(request, 'Books/index.html', context)


def Book(request, id):
    BM = BookMethod(id)
    
    ErrorList = []
    context = {}
    if BM.CheckBook() is False:
        ErrorList.append(ERRORS[404])
        return render(request, 'Books/book_404.html')
    else:
        BM = BookMethod(id)
        print(BM.AllBooks())
        
        context['doc'] = BM.GetDoc()
        context['img'] = BM.GetIMG()[0]
        context['title'] = BM.GetTitle()
        context['summary'] = BM.GetSummary()
        context['genreList'] = BM.GetGenres()
        context['authorList'] = BM.GetAuthors()
        context['keyWordList'] = BM.GetKeyWords()
        
        return render(request, 'Books/book.html', context)


def Authors(request):
    context = {}
    AM = AuthorMethod(id = id)
    if request.method == "POST":
        AuthorRequest = str(request.POST.get("AuthorRequest"))
        context['AuthorList'] = SearchAuthor(AuthorRequest, AM.AllAuthors())
        return render(request, 'Authors/index.html', context)
    else:
        context['AuthorList'] = AM.AllAuthors()
        return render(request, 'Authors/index.html', context)


def AuthorBooks(request, id):
    AM = AuthorMethod(id = id)
    context = {}
    context['AuthorInfo'] = AM.GetAuthorInfo()
    context['AllBooks'] = AllAuthorBooks(id)
    
    return render(request, "Authors/author.html", context)


def Genres(request):
    context = {}
    GM = GenreMethod()
    if request.method == "POST":
        GenreRequest = str(request.POST.get("GenreRequest"))
        context['GenreList'] = SearchGenre(GenreRequest, GM.AllGenres())
        return render(request, 'Genres/index.html', context)
    else:
        
        context['GenreList'] = GM.AllGenres()
    
        
        return render(request, 'Genres/index.html', context)

def GenresBooks(request, id):
    context = {}
    GM = GenreMethod(id = id)
    context['GenreInfo'] = GM.GetGenreInfo()
    context['AllBooks'] = AllGenreBooks(id)
    
    return render(request, "Genres/genre.html", context)

################################################################################################
# Вспомогательные функции
################################################################################################


def SearchGenre(search: str, GenreList: List[dict]) -> List[dict]:
    Responce = []

    search = search.lower().split()
    for Genre in GenreList:
        info = []
        name = Genre['name'].lower().split()
        summary = Genre['summary'].lower().split()

        for word in name:
            info.append(word)

        for word in summary:
            info.append(word)

        if ArrInArr(info, search) is True:
            Responce.append(Genre)
        else:
            pass
    return Responce

def SearchAuthor(search: str, AuthorList: List[dict]) -> List[dict]:
    Responce = []
    search = search.lower().split()
    for Author in AuthorList:
        info = []
        name = Author['name'].lower()
        surname = Author['surname'].lower()
        patronymic = Author['patronymic'].lower()

        info.append(name)
        info.append(surname)
        info.append(patronymic)

        if ArrInArr(info, search) is True:
            Responce.append(Author)
        else:
            pass
    return Responce

def SearchBook(search: str, BookModel: object) -> List[dict]:
    Responce = []
    search = search.lower().split()
    
    return Responce

#-------------------------------------------------------------------------
def ArrInArr(arr_x: List[str], arr_y: List[str]) -> bool:
    return any(x in arr_x for x in arr_y)





def AllAuthorBooks(AuthorId: int) -> List[dict]:
    AllAuthorBooks = []
    AM = AuthorMethod(id = AuthorId)
    AuthorName = AM.GetName()
    AuthorSurname = AM.GetSurname()
    AuthorPatronymic = AM.GetPatronymic()
    #AuthorInfo = "{0} {1} {2}".format(AuthorName, AuthorSurname, AuthorPatronymic)
    AllBooks = B.objects.filter(author__name = AuthorName, 
                                author__surname = AuthorSurname,
                                author__patronymic = AuthorPatronymic).in_bulk()
    for id in AllBooks:
        BM = BookMethod(id = id)
        BookInfo = {
            "id": id,
            "title": BM.GetTitle(), 
            "img": BM.GetIMG()[0],
        }
        AllAuthorBooks.append(BookInfo)
    return AllAuthorBooks


def AllGenreBooks(GenreId: int) -> List[dict]:
    AllGenreBooks = []
    GM = GenreMethod(id = GenreId)
    GenreName = GM.GetName()
    AllBooks = B.objects.filter(genre__name = GenreName).in_bulk()
    for id in AllBooks:
        BM = BookMethod(id)
        BookInfo = {
            "id": id,
            "title": BM.GetTitle(), 
            "img": BM.GetIMG()[0],
        }
        AllGenreBooks.append(BookInfo)
    return AllGenreBooks


class BookMethod:
    def __init__(self, id:int = 1, BookModel:dict = BookModel,
                                GenreModel:dict = GenreModel,
                                 AuthorModel:dict = AuthorModel):
        self.id = id
        self.BookModel = BookModel
        self.GenreModel = GenreModel
        self.AuthorModel = AuthorModel

    def __str__(self):
        return '{}'.format(self.BookModel[self.id])
        
    def CheckBook(self) -> bool:
        try:
            self.BookModel[self.id]
            return True
        except KeyError:
            return False

    def GetTitle(self ) -> str:
        return "{}".format(self.BookModel[self.id].title)

    def GetDoc(self) -> str:
        return "{}".format(self.BookModel[self.id].doc)

    def GetSummary(self) -> str:
        return "{}".format(self.BookModel[self.id].summary)

    def GetLang(self) -> str:
        return "{}".format(self.BookModel[self.id].lang)

    def GetGenres(self):
        GenreId = []
        GenreList = []
        
        for Genre in self.BookModel[self.id].genre.all():
            GenreList.append(str(Genre))

        for id in self.GenreModel:
            if GenreModel[id].name in GenreList:
                GenreId.append(id)
            else:
                continue

        return [genre for genre in zip(GenreId, GenreList)]

    def GetAuthors(self):
        AuthorList = []
        AuthorId = []
        for Author in self.BookModel[self.id].author.all():
            AuthorList.append(str(Author))

        for id in self.AuthorModel:
            name = self.AuthorModel[id].name
            patronymic = self.AuthorModel[id].patronymic
            surname = self.AuthorModel[id].surname
            AuthorFIO = "{0} {1} {2}".format(name, patronymic, surname)
            if AuthorFIO in AuthorList:
                AuthorId.append(str(id))
            else:
                pass


        return [author for author in zip(AuthorId, AuthorList)]

    def GetKeyWords(self):
        KeyWordList = []
        for KeyWord in self.BookModel[self.id].keyword.all():
            KeyWordList.append(str(KeyWord))
        return KeyWordList

    def GetIMG(self):
        IMGList = []
        for IMG in self.BookModel[self.id].img.all():
            IMGList.append(str(IMG))
        return IMGList

    def AllBooks(self):
        Books = []
    
        for id in self.BookModel:
            BookInfo = {}
            BM = BookMethod(id = id)
            BookInfo['id'] = id
            BookInfo['doc'] = BM.GetDoc()
            BookInfo['lang'] = BM.GetLang()
            BookInfo['title'] = BM.GetTitle()
            BookInfo['IMGList'] = BM.GetIMG()
            BookInfo['summary'] = BM.GetSummary()
            BookInfo['genreList'] = BM.GetGenres()
            BookInfo['authorList'] = BM.GetAuthors()
            BookInfo['keyWordList'] = BM.GetKeyWords()
            
            Books.append(BookInfo)
        return Books

class GenreMethod:
    def __init__(self, id:int = 1, GenreModel:dict = GenreModel):
        self.id = id
        self.GenreModel = GenreModel


    def __str__(self):
        return "{}".format(self.GenreModel[self.id])

    def GetName(self) -> str:
        return "{}".format(self.GenreModel[self.id].name)

    def GetSummary(self) -> str:
        return "{}".format(self.GenreModel[self.id].summary)

    def GetIMG(self) -> List[str]:
        return [str(img) for img in self.GenreModel[self.id].img.all()]

    def AllGenres(self):
        AllGenreList = []
        for id in self.GenreModel:
            file = [str(img) for img in self.GenreModel[id].img.all()]
            name = self.GenreModel[id].name
            summary = self.GenreModel[id].summary
            GenreInfo = {
                'id': id,
                'name': name,
                'summary': summary,
                'file' : file[0],
            }
            AllGenreList.append(GenreInfo)
        return AllGenreList

    def GetGenreInfo(self):
        GenreInfo = {}
        GenreInfo['name'] = self.GetName()
        GenreInfo['img'] = self.GetIMG()[0]
        GenreInfo['summary'] = self.GetSummary()
        return GenreInfo

class AuthorMethod:
    def __init__(self, id:int = 1, AuthorModel:dict = AuthorModel) :
        self.id = id
        self.AuthorModel = AuthorModel

    def __str__(self):
        return "{}".format(self.AuthorModel[self.id])

    def GetName(self):
        return "{}".format(self.AuthorModel[self.id].name)

    def GetPatronymic(self):
        return "{}".format(self.AuthorModel[self.id].patronymic)

    def GetSurname(self):
        return "{}".format(self.AuthorModel[self.id].surname)

    def GetSummary(self):
        return "{}".format(self.AuthorModel[self.id].summary)

    def GetIMG(self):
        return [str(img) for img in self.AuthorModel[self.id].img.all()]

    def GetFIO(self):
        return "{0} {1} {2}".format(self.GetName(), self.GetPatronymic(), self.GetSurname())

    def AllAuthors(self):
        AllAuthorList = []
        for id in self.AuthorModel:
            name = self.AuthorModel[id].name
            file = [str(img) for img in self.AuthorModel[id].img.all()]
            surname = self.AuthorModel[id].surname
            patronymic = self.AuthorModel[id].patronymic
            AuthorInfo = {
                'id' : id,
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'file' : file[0],
                
            }
            AllAuthorList.append(AuthorInfo)

        return AllAuthorList
    
    def GetAuthorInfo(self):
        AuthorInfo = {}    
        AuthorInfo['name'] = self.GetFIO()
        AuthorInfo['summary'] = self.GetSummary()
        AuthorInfo['img'] = self.GetIMG()[0]
        return AuthorInfo