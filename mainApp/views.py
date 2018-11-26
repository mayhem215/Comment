from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import CommentForm
from .models import Comment


def post_single(request):
    comment = Comment.objects.order_by('-vote')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    return render(request, "mainApp/home.html", context={"form": form, "comments": comment})


def vote_view(request, id_comment):
    vote = get_object_or_404(Comment, pk=id_comment)
    vote.vote += 1
    vote.save()
    return redirect(reverse('comment:content',))
