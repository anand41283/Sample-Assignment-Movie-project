from django.db import models

# Create your models here.

class Genre(models.Model):
    Genre=models.CharField(max_length=20)
    Discription=models.CharField(max_length=200)

    def __str__(self):
        return self.Genre
    
    

class Movie(models.Model):
    Title=models.CharField(max_length=20)
    Release_date=models.DateField()
    Duaration=models.CharField(max_length=20)
    Summary=models.CharField(max_length=200)
    Movie_genre=models.ForeignKey(Genre,on_delete=models.CASCADE)


