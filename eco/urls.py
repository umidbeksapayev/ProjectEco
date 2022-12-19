from django.urls import path
from .views import *

urlpatterns = [
    path('', EcoHome.as_view(), name='home'),
    path('post/<int:pk>', DetailEco.as_view(), name='detail'),
    path('Issues/', NavIssues.as_view(), name='issues'),
    path('about/', NavAbout.as_view(), name='about'),
    path('society/', NavSociety.as_view(), name='society'),
    path('donation/', NavDonation.as_view(), name='donation'),
    path('journal/', NavJournal.as_view(), name='journal'),
    path('contact/', NavContact.as_view(), name='contact'),
]