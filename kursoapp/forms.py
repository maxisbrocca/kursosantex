# -*- coding: utf-8 -*-
from django import forms
from models import BlogPost, Cliente, Diapositiva, HomePost, RespuestaBlogPost, Servicio

class RespuestaBlogPostForm(forms.ModelForm):
    class Meta:
        model = RespuestaBlogPost


class HomePostForm(forms.ModelForm):
    class Meta:
        model = HomePost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente


class DiapositivaForm(forms.ModelForm):
    class Meta:
        model = Diapositiva