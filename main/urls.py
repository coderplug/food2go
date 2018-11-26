from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='main-index'),
    path('login/', views.login, name='main-login'),
    path('logout/', views.logout, name='main-logout'),
    path('signup/', views.signup, name='main-signup'),
]
