from django.urls import path
from homeapp import views

app_name = 'home_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('about/', views.aboutView, name='about'),
    path('solution/', views.solutionView, name='solution'),
    path('portfolio/', views.portfolioView, name='portfolio'),
    path('portfolio-single/', views.portfolioSingleView, name='portfolio-single'),
    path('blog/', views.blogView, name='blog'),
    path('blog-single/', views.blogSingleView, name='blog-single'),
    path('contact/', views.contactView, name='contact'),
]
