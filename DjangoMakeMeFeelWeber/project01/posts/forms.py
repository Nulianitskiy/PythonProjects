from django.forms import TextInput, Textarea, ModelForm, DateInput
from .models import Author, Publisher
from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label="Name")
    id_author = forms.ModelMultipleChoiceField(queryset=Author.author_obj.all())
    # id_author = forms.ChoiceField(choices=((i.id_author, i.pseudonym) for i in Author.author_obj.all()), label="Код автора")
    genre = forms.CharField(label="Genre")
    id_publisher = forms.ModelMultipleChoiceField(queryset=Publisher.publisher_obj.all())
    # id_publisher = forms.ChoiceField(choices=((i.id_publisher, i.name) for i in Publisher.publisher_obj.all()), label="Код издателя")
    timestamp = forms.DateField(label="Timestamp", widget=forms.DateInput)


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    second_name = forms.CharField(label="Last Name")
    father_name = forms.CharField(label="Father`s Name")
    pseudonym = forms.CharField(label="Pseudonym")
    date_birth = forms.DateField(label="Date Birth", widget=forms.DateInput)


class PublisherForm(forms.Form):
    name = forms.CharField(label="Name")
    address = forms.CharField(label="Address")
    foundation = forms.DateField(label="Foundation Date", widget=forms.DateInput)
