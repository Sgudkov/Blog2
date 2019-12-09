from django.urls import path
from .views import HomePageView, DetailArticle, SearchResultsView, ClassesView, FuncView, OtherView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('articles/<int:pk>/',DetailArticle.as_view(), name='articles'),
path('search/', SearchResultsView.as_view(), name='search'),
path('classes/', ClassesView.as_view(), name='classes'),
path('fm/', FuncView.as_view(), name='fm'),
path('other/', OtherView.as_view(), name='other')
]