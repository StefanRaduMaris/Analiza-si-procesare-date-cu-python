from django.contrib import admin
from django.urls import path
from club.views import validare_cnp_view,rezultat_cnp_view


urlpatterns = [
    path('cnp/',validare_cnp_view),
    path('rezultat',rezultat_cnp_view),
    ]
