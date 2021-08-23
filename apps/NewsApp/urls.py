from . import views
from django.urls import path


urlpatterns = [
    path('<int:identifier>/main', views.MainPageTemplateView.as_view(), name='main_page'),
    path('<int:identifier>/send', views.NewsListView.as_view(), name='send_news'),
    path('<int:identifier>/create', views.NewsCreateView.as_view(), name='create_news'),
    path('<int:identifier>/detail/<int:news_identifier>', views.NewsDetailView.as_view(), name='detail_news'),
    path('<int:identifier>/update/<int:news_identifier>', views.NewsUpdateView.as_view(), name='update_news'),
]
