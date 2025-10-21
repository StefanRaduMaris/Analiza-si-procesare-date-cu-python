from django.urls import path
from capitalize.views import capitalize_word,parametri_view

urlpatterns = [
path('parametri/',parametri_view),
path('<text>',capitalize_word) ,
 
]