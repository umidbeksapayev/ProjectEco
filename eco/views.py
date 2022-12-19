from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class EcoHome(ListView):
    model = EcoPost
    template_name = 'home.html'
    context_object_name = 'eco'


class DetailEco(DetailView):
    model = EcoPost
    template_name = 'detail.html'


class NavIssues(ListView):
    model = EcoPost
    template_name = 'issues.html'


class NavAbout(ListView):
    model = EcoPost
    template_name = 'about.html'


class NavSociety(ListView):
    model = EcoPost
    template_name = 'society.html'


class NavSociety(ListView):
    model = EcoPost
    template_name = 'society.html'


class NavDonation(ListView):
    model = EcoPost
    template_name = 'donation.html'


class NavJournal(ListView):
    model = EcoPost
    template_name = 'journal.html'


class NavContact(ListView):
    model = EcoPost
    template_name = 'contact.html'

