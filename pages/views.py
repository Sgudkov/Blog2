from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts_list'
    paginate_by = 3

class ArticlesPageView(ListView):
    model = Post
    template_name = 'pages/articles.html'
    context_object_name = 'articles_list'

class DetailArticle(DetailView):
    model = Post
    template_name = 'pages/articles.html'
    context_object_name = 'articles'


class ClassesView(ListView):
    model = Post
    template_name = 'pages/classes.html'
    context_object_name = 'classes_list'

class FuncView(ListView):
    model = Post
    template_name = 'pages/FM.html'
    context_object_name = 'fm_list'

class SearchResultsView(ListView):
    model = Post
    template_name = 'pages/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query  is not None:
            object_list = Post.objects.filter(
                Q(head__icontains=query) | Q(text__icontains=query)
            )
            return object_list

