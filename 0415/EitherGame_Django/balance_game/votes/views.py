from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count
from .models import Vote, Comment
from .forms import VoteForm, CommentForm

# Create your views here.
def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes' : votes,
    }
    return render(request, 'votes/index.html', context)

def detail(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    comment_form = CommentForm()
    comments = vote.comment_set.order_by('-pk')
    count_a = len(comments.filter(voting='A'))
    count_b = len(comments.filter(voting='B'))
    total = count_a + count_b
    if total == 0:
        voted_a = 0
        voted_b = 0
    else:
        voted_a = count_a / total * 100
        voted_b = count_b / total * 100

    # print('여기다', voted_a, voted_b)
    # vote_rate_a = Vote.objects.aggregate(Count(comments.)/Count(vote.pk)*100).get(vote_id=pk)
    # vote_rate_b = Vote.objects.aggregate(Count(vote.Issue_b)/Count(vote.pk)*100).get(vote_id=pk)
    context = {
        'vote' : vote,
        'comment_form' : comment_form,
        'comments' : comments,
        # 'vote_rate_a' : vote_rate_a,
        # 'vote_rate_b' : vote_rate_b,
        'voted_a' : voted_a,
        'voted_b' : voted_b,
    }
    return render(request, 'votes/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
            return redirect('votes:detail', vote.pk)
    else:
        form = VoteForm()
    context = {
        'form' : form,
    }
    return render(request, 'votes/create.html', context)

@require_POST
def comment_create(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.vote = vote
        comment.save()
    return redirect('votes:detail', vote.pk)