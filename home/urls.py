from django.urls import path
from .views import HomePage, add_news_view, PostDetailView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('add-new/', add_news_view, name="add_new"),

    path('post-details/<int:id>/', PostDetailView.as_view(), name='post_details'), # class-based view
    # path('post-details/<int:id>/', post_details, name='post-details'), # function-based view 
]