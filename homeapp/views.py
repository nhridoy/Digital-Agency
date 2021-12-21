from django.shortcuts import render
from homeapp import forms


# Create your views here.

def indexView(request):
    form = forms.ReviewForm
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def aboutView(request):
    context = {

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
