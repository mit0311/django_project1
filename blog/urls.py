from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.BlogHome.as_view(),name='bloghome'),
    path('<str:slug>',views.BlogPost,name='blogPost')



]