from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post
from django.views.generic.edit import CreateView

from home.forms import SignUpForm

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/About.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'


def Search(request):
    query = request.GET['query']
    poststitle = Post.objects.filter(title__icontains = query)
    postcontent = Post.objects.filter(content__icontains = query)
    allposts = poststitle.union(postcontent)
    params = {'allposts' : allposts }
    return render(request,'home/search.html',params)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/accounts/login/'