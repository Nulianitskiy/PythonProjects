from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getInfo', views.getInfo),
    path('InsertFolder/insert_author', views.insertAuthor),
    path('InsertFolder/insert_publisher', views.insertPublisher),
    path('InsertFolder/insert_book', views.insertBook),

    path('EditFolder/edit_publisher/', views.editPublisher),
    path('EditFolder/edit_publisher/deletePublisher/<int:id_del>/', views.deletePublisher),
    path('EditFolder/edit_publisher/editPublisher/<int:id_del>/', views.editPublisherF),

    path('EditFolder/edit_author/', views.editAuthor),
    path('EditFolder/edit_author/deleteAuthor/<int:id_del>/', views.deleteAuthor),
    path('EditFolder/edit_author/editAuthor/<int:id_del>/', views.editAuthorF),
]
