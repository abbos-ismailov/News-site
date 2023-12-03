from django.urls import path
from .views import (HomePage, 
                    AddNewView, 
                    PostDetailView, 
                    NewsDeleteView, 
                    NewsUpdateView, 
                    CategoryDetail, 
                    TagsDetail, 
                    SearchView,
                    MyNewsView,
                    )

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('add-new/', AddNewView.as_view(), name="add_new"),
    path('my-news/', MyNewsView.as_view(), name="my_news"),

    path('post-details/<int:id>/', PostDetailView.as_view(), name='post_details'), # class-based view
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='new_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='new_update'),

    path('category/<int:pk>/', CategoryDetail.as_view(), name="category_new"),
    path('tags/<int:pk>/', TagsDetail.as_view(), name="tags_new"),

    path("search/", SearchView.as_view(), name="search"),
]