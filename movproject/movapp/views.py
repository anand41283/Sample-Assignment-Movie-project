from django.shortcuts import render,redirect
from django.views.generic import View
from movapp.forms import GenreForm,MovieForm
from movapp.models import Genre,Movie

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'Home.html')

class GenreFormView(View):
    def get(self,request):
        form= GenreForm()
        return render(request,'Genreform.html',{"form":form})
    def post(self,request):
        form=GenreForm(request.POST)
        if form.is_valid():
            Genre.objects.create(**form.cleaned_data)
        else:
            print("get out")    
        form=GenreForm()    
        # return render(request,'Genreform.html',{"form":form})    
        return redirect('GenMovlist')    

class MovieFormView(View):
    def get(self,request):
        form=MovieForm()
        return render(request,'moveiform.html',{"form":form})
    def post(self,request):
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("get out")    
        form=MovieForm()    
        # return render(request,'moveiform.html',{"form":form})   
        return redirect('movielist')   
    
class Genrelist(View):
    def get(self,request):
        genre=Genre.objects.all()
        return render(request,'genrelist.html',{"form":genre})

class GenrelistUpdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        G_Update=Genre.objects.get(id=id)
        form=GenreForm(instance=G_Update)
        return render(request,'Genreform.html',{"form":form})  
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        G_Update=Genre.objects.get(id=id)
        form=GenreForm(request.POST,instance=G_Update)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('GenMovlist')   

class Genrelistdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Genre.objects.get(id=id).delete()
        return redirect('genrelist') 
            
    
class GenreMovielist(View):
    def get(self,request):
        genre=Genre.objects.all()
        return render(request,'genremovielist.html',{"form":genre})
    
class Movielist(View):
    def get(self,request):
        movies=Movie.objects.all()
        return render(request,'movielist.html',{"form":movies})    
    
class MovielistUpdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')  
        movies=Movie.objects.get(id=id)  
        form=MovieForm(instance=movies)
        return render(request,'moveiform.html',{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')  
        movies=Movie.objects.get(id=id)  
        form=MovieForm(request.POST,instance=movies)
        if form.is_valid():
            form.save()
        else:
            print("get out")
        return redirect('movielist')     

class MovielistDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Movie.objects.get(id=id).delete()
        return redirect('movielist')
    
class GenreMovieView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        filter=Movie.objects.filter(Movie_genre=id) 
        return render(request,'movielist.html',{"form":filter})   

class MovielistDiscription(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Movie.objects.get(id=id)
        filter=Genre.objects.filter(Genre=qs.Movie_genre)
        return render(request,'Discription.html',{"form":filter})

       



