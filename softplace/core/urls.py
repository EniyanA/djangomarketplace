from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm

app_name='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('socialmedia/', views.socialmedia, name='socialmedia'),
    path('chat/',views.chat, name='chat' ),
    path('about/', views.about, name='about'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('privacypolicy/', views.privacypolicy, name='privacypol'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
]