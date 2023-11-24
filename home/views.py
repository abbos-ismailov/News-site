from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# from django.views.generic.edit import DeleteView
from .models import News, Contact, Social, Tags, Category
from django.urls import reverse_lazy
from .forms import AddNewForm
from django.contrib.auth.decorators import login_required  ### this is function

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)  ### This is class. Permission

from django.db.models import Q

# Create your views here.


class HomePage(ListView):
    template_name = "index.html"
    model = News

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["popular_item"] = (
            News.objects.filter(is_active=True).order_by("view_count").reverse()[:5]
        )
        context["popular_new"] = context["popular_item"][0]
        context['popular_news'] = context['popular_item'][1:]
        context["data_news"] = News.objects.filter(is_active=True)

        return context


class AddNewView(CreateView):
    model = News
    success_url = reverse_lazy('home')
    template_name = 'add_new.html'
    form_class = AddNewForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user ### Shu joyini korish kerak
        return super().form_valid(form)

# @login_required
# def add_news_view(request):
#     if request.POST:
#         form = AddNewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return redirect("home")
#     context = {}
#     context["form"] = AddNewForm()
#     return render(request, "add_new.html", context)


# Class based view
class PostDetailView(DetailView):
    context_object_name = "detail_news"  ### Shu narsa delete qilishda kerak boldi
    template_name = "single-page.html"

    # Overriding the class get_object method
    def get_object(self):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(News, id=post_id)
        # Update the view count on each visit to this post.
        if post:
            post.view_count = post.view_count + 1
            post.save()

        return post


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = reverse_lazy("home")
    template_name = "news_delete.html"  ### Bu qaysi templatega jonatsin

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ["title", "img", "body", "category", "tags"]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("post_details", kwargs={"id": pk})

    template_name = "update_news.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser


class CategoryDetail(DetailView):
    context_object_name = "data_category_type"
    template_name = 'data_category.html'

    def get_object(self):
        id = self.kwargs['pk']
        return News.objects.filter(category__id=id)


class TagsDetail(DetailView):
    context_object_name = "data_tags_type"
    template_name = 'data_tags.html'

    def get_object(self):
        id = self.kwargs['pk']
        return News.objects.filter(tags__id=id)


class SearchResultsView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'search_results.html'

    
    def get_queryset(self): # new
        return News.objects.filter(
            Q(title="Boston") | Q(body="NY")
        )


class MyNewsView(LoginRequiredMixin, ListView):
    template_name = "my_news.html"
    model = News
    # context_object_name = "my_news"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['my_news'] = News.objects.filter(user=self.request.user)
        return context