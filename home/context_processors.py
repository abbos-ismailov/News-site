from .models import Category, Tags, Social, Contact, News


def LatestContext(request):
    latest_news = News.objects.all().order_by("-create_at")[:5]

    context = {
        "last_news": latest_news[1:],
        "last_new": latest_news[0],
        # 'last_new_body': latest_news[0].body[:50]
    }

    return context

def CategoryContext(request):
    data = Category.objects.all()

    context = {
        "category_data": data
    }

    return context

def TagsContext(request):
    data = Tags.objects.all()
    context = {
        "tags_data": data
    }

    return context

def SocialContext(request):
    data = Social.objects.all()

    context = {
        "social_data": data
    }
    return context