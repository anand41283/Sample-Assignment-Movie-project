"""movproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movapp.views import GenreFormView,MovieFormView,GenreMovielist,Movielist,MovielistUpdate,MovielistDelete,GenreMovieView,Genrelist,GenrelistUpdate
from movapp.views import Genrelistdelete,MovielistDiscription,Home,UserRegistration,UserLogin,HomeIn,UserLogout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name="home"),
    path('Home',HomeIn.as_view(),name="home2"),

    path('genreform/',GenreFormView.as_view(),name="Gform"),
    path('genrelist/',Genrelist.as_view(),name="genrelist"),
    path('genremovielist/',GenreMovielist.as_view(),name='GenMovlist'),
    path('genrelistupdate/<int:pk>',GenrelistUpdate.as_view(),name="G_Update"),
    path('genrelistdelete/<int:pk>',Genrelistdelete.as_view(),name="G_Delete"),
    path('GenreMovieView/<int:pk>/',GenreMovieView.as_view(),name="GenView"),

    path('moveiform/',MovieFormView.as_view(),name="Mform"),
    path('Movielist/',Movielist.as_view(),name="movielist"),
    path('MovielistUpdate/<int:pk>/',MovielistUpdate.as_view(),name="MUpdate"),
    path('Movielistdelete/<int:pk>/',MovielistDelete.as_view(),name="Mdelete"),
    path('MovielistDiscription/<int:pk>',MovielistDiscription.as_view(),name=("MDiscription")),

    path('register/',UserRegistration.as_view(),name="Reg"),
    path('login/',UserLogin.as_view(),name="login"),
    path('logout/',UserLogout.as_view(),name="logout"),


]
