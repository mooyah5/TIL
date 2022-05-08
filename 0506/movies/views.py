from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST

from .models import Movie, Genre
import random

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def recommended(request):
    if request.method == 'POST':
        selected = request.POST.getlist('test')
        if len(selected) >= 3:
            size = [4, 3, 3]
        elif len(selected) == 2:
            size = [5, 5]
        elif len(selected) == 1:
            size = [10]

        result = []
        for i in range(len(selected)):
            movies = Movie.objects.filter(genres=selected[i])
            movies = list(movies)
            if len(movies) < size[i]:
                result.extend(movies)
            else:
                select = random.sample(range(len(movies)), size[i])

                for j in range(size[i]):
                    if movies[select[j]] not in result:
                        result.append(movies[select[j]])
        
        while len(result) < 10:
            num = random.randint(1, 100)
            movie = Movie.objects.get(pk=num)
            if movie not in result:
                result.append(movie)

        context = {
            'movies': result
        }
        return render(request, 'movies/recommended.html', context)
    
    elif request.method == 'GET':
        genres = Genre.objects.all()
        context = {
            'genres': genres
        }
        return render(request, 'movies/genre.html', context)
