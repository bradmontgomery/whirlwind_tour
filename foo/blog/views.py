from django.shortcuts import render
from .models import Post


def list_posts(request):
    context = {
        'posts': Post.objects.all(),
    }
    template = "blog/list.html"
    return render(request, template, context)


def display_post(request, post_slug):
    """
    Given a slug, this view will retrive the relevant post
    and render a template.
    """
    context = {
        'post': Post.objects.get(slug=post_slug)
    }
    template = "blog/post.html"
    return render(request, template, context)
