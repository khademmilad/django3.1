from .models import Blog


def list_objects(request):
    return {
        'all_posts' : Blog.objects.order_by('pub_date')
    }
