from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'^$', views.post_single, name="content"),
    url(r'^comment-vote/(?P<id_comment>[0-9]+)', views.vote_view, name="comment_vote"),
]
