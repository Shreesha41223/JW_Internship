from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten_url, name='shorten_url'),  # This seems redundant; consider removing it
    path('<str:short_link>', views.redirect_url, name='redirect_url'),
]