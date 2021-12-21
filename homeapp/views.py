from django.shortcuts import render, HttpResponseRedirect

from homeapp import forms, models


# Create your views here.

def indexView(request):
    form = forms.ReviewForm
    reviews = models.ReviewModel.objects.all()
    achievements = models.AchievementModel.objects.all().last()

    if request.method == 'POST':
        form = forms.ReviewForm(files=request.FILES, data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = request.POST.get('rating')
            review.comment = request.POST.get('comment')
            review.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'reviews': reviews,
        'achievements': achievements,
    }
    return render(request, 'index.html', context)


def aboutView(request):
    reviews = models.ReviewModel.objects.all()
    achievements = models.AchievementModel.objects.all().last()
    context = {
        'reviews': reviews,
        'achievements': achievements,
    }
    return render(request, 'about.html', context)


def solutionView(request):
    context = {

    }
    return render(request, 'solution.html', context)


def portfolioView(request):
    context = {

    }
    return render(request, 'portfolio.html', context)


def portfolioSingleView(request):
    context = {

    }
    return render(request, 'portfolio-single.html', context)


def blogView(request):
    context = {

    }
    return render(request, 'blog.html', context)


def blogSingleView(request):
    context = {

    }
    return render(request, 'blog-single.html', context)


def contactView(request):
    context = {

    }
    return render(request, 'contact.html', context)
