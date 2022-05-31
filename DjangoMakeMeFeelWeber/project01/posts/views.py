from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.
from . import models, forms
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Book, Author, Publisher


def index(request):
    return render(request, 'index.html')


def getInfo(request):
    dataBook = Book.book_obj.order_by('id')
    dataAuthor = Author.author_obj.order_by('id')
    dataPublisher = Publisher.publisher_obj.order_by('id')
    return render(request, 'getInfo.html',
                  {'dataBook': dataBook, 'dataAuthor': dataAuthor, 'dataPublisher': dataPublisher})


def insertAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            aut = Author()
            aut.first_name = request.POST.get("first_name")
            aut.second_name = request.POST.get("second_name")
            aut.father_name = request.POST.get("father_name")
            aut.pseudonym = request.POST.get("pseudonym")
            aut.date_birth = request.POST.get("date_birth")
            aut.save()
        return redirect('home')
    form = AuthorForm()
    dataAuthor = Author.author_obj.all()
    return render(request, 'InsertFolder/insert_author.html',
                  {'title': 'Add New Author', 'dataAuthor': dataAuthor, 'form': form})


def insertPublisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            pub = Publisher()
            pub.name = request.POST.get("name")
            pub.address = request.POST.get("address")
            pub.foundation = request.POST.get("foundation")
            pub.save()
        return redirect('home')
    form = PublisherForm()
    dataPublisher = Publisher.publisher_obj.all()
    return render(request, 'InsertFolder/insert_publisher.html',
                  {'title': 'Add New Publisher', 'dataPublisher': dataPublisher, 'form': form})


def insertBook(request):
    if request.method == 'POST':
        book = Book()
        book.name = request.POST.get("name")
        book.id_author = Author.author_obj.get(pk=request.POST.get("id_author"))
        book.genre = request.POST.get("genre")
        book.id_publisher = Publisher.publisher_obj.get(pk=request.POST.get("id_publisher"))
        book.timestamp = request.POST.get("timestamp")

        book.save()
        return redirect('home')
    form = BookForm()
    dataBook = Book.book_obj.all()
    return render(request, 'InsertFolder/insert_book.html',
                  {'title': 'Add New Book', 'dataBook': dataBook, 'form': form})


def deletePublisher(reqiest, id_del):
    try:
        pub = Publisher.publisher_obj.get(pk=id_del)
        pub.delete()

        return HttpResponseRedirect("/EditFolder/edit_publisher")
    except Publisher.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def editPublisher(request):
    dataPublisher = Publisher.publisher_obj.order_by('id')
    return render(request, 'EditFolder/Publisher.html',
                  {'dataPublisher': dataPublisher})


def editPublisherF(request, id_del):
    try:
        pub = Publisher.publisher_obj.get(pk=id_del)

        if request.method == "POST":
            pub.name = request.POST.get("name")
            pub.address = request.POST.get("address")
            pub.foundation = request.POST.get("foundation")
            pub.save()
            return HttpResponseRedirect("/EditFolder/edit_publisher")
        else:
            return render(request, "EditFolder/edit_publisher.html", {'dataPub': pub})
    except Publisher.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def deleteAuthor(reqiest, id_del):
    try:
        aut = Author.author_obj.get(pk=id_del)
        aut.delete()

        return HttpResponseRedirect("/EditFolder/edit_author")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def editAuthor(request):
    dataAuthor = Author.author_obj.order_by('id')
    return render(request, 'EditFolder/Author.html',
                  {'dataAuthor': dataAuthor})


def editAuthorF(request, id_del):
    try:
        aut = Author.author_obj.get(pk=id_del)

        if request.method == "POST":
            aut.first_name = request.POST.get("first_name")
            aut.second_name = request.POST.get("second_name")
            aut.father_name = request.POST.get("father_name")
            aut.pseudonym = request.POST.get("pseudonym")
            aut.date_birth = request.POST.get("date_birth")
            aut.save()
            return HttpResponseRedirect("/EditFolder/edit_author")
        else:
            return render(request, "EditFolder/edit_author.html", {'dataAut': aut})
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")
