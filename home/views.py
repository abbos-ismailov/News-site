from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import News, Contact, Social, Tags, Category
from django.urls import reverse_lazy
from .forms import AddNewForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
# Create your views here.


class HomePage(ListView):
    template_name = 'index.html'
    model = News
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context['popular_news'] = News.objects.all().order_by('view_count').reverse()[:5]
        context['popular_new'] = context['popular_news'][0]
        context['data_news'] = News.objects.all()

        return context

@login_required
def add_news_view(request):
    if request.POST:
        form = AddNewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
    context = {

    }
    context['form'] = AddNewForm()
    return render(request, 'add_new.html', context)



# Class based view
class PostDetailView(DetailView):
    context_object_name = 'detail_news'
    template_name = 'single-page.html'

    # Overriding the class get_object method
    def get_object(self):
        post_id = self.kwargs.get('id')
        post = get_object_or_404(News, id=post_id)
        # Update the view count on each visit to this post.
        if post:
            post.view_count = post.view_count + 1
            post.save()

            # Or
            # post.update_views()

        return post

    # You might have other methods in here if necessary