from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post

# Create your views here.

class BlogHome(TemplateView):
    template_name = 'blog/bloghome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allposts = Post.objects.all()
        context = {'allposts' : allposts}
        return context
    
# class BlogPost(TemplateView):
#     template_name = 'blog/blogPost.html'

#     def get_context_data(slug,self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = Post.objects.filter(slug=slug).first()
#         context = {'post' : post}
#         return context


def BlogPost(request,slug):
    post =Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request,'blog/blogPost.html',context)


# def Search(request):
#     query = request.GET['query']
#     poststitle = Post.objects.filter(title_icontains = query)
#     params = {'posttitle' : poststitle }
#     return render(request,'blog/search.html',params)