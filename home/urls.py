from django.urls import path
from .views import HomePage, add_news_view, PostDetailView, NewsDeleteView, NewsUpdateView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('add-new/', add_news_view, name="add_new"),

    path('post-details/<int:id>/', PostDetailView.as_view(), name='post_details'), # class-based view
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='new_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='new_update'),
]