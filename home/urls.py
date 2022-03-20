from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('search/',views.Search,name = 'search'),
    path('signup/',views.SignUpView.as_view(),name='signup')


]