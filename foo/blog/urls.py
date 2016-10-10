from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_posts, name='list_posts'),
    url(r'^(?P<post_slug>.+)/$', views.display_post, name='display_post'),
]
