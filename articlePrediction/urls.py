from unicodedata import name
from django.urls import path,include
from . import views
from .views import about_view ,contact_view

from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
urlpatterns = [
    path('', views.index, name='index'),
    path('lstm/',views.home,name='home'),
    path('forUrl/', views.for_url_view, name='forurl'),
    path('forArticle/', views.for_article_view, name='forarticle'),
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', about_view, name='about'),  # Define the URL pattern for the About page
    path('contact/', contact_view, name='contact'),  # Define the URL pattern for the About page
     path('accounts/profile/', views.profile, name='profile'),
]