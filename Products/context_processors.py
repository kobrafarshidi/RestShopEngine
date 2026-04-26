from .models import Category


def navbar_categories(request):
    categories = Category.objects.all()

    return {
        "navbar_categories": categories
    }
