from django.urls import path
from parola.views import parola_view,alege_view

urlpatterns = [
path('parola/',parola_view),
path('alege/',alege_view),
]


