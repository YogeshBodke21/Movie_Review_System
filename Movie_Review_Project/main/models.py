from django.db import models

# Create your models here.


rating = (
    ("1-Star","1-Star" ),
    ("2-Star","2-Star" ),
    ("3-Star","3-Star" ),
    ("4-Star","4-Star" ),
    ("5-Star","5-Star"),
)

status_cho = (
    ("Published", "Published"),
    ("Not Published", "Not Published"),
)
DEMO_CHOICES =( 
    ("Horror", "Horror"), 
    ("Action", "Action"), 
    ("Sci-Fi", "Sci-Fi"), 
    ("Comedy", "Comedy"), 
    ("Thriller", "Thriller"), 
) 
class Movie_Review(models.Model):
    MovieTitle = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    reviewContent = models.TextField(max_length=200, null=False)
    rating = models.TextField(choices = rating, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewer_email_id = models.EmailField(max_length=100)
    status = models.TextField(choices=status_cho)
    genres = models.TextField(choices = DEMO_CHOICES)

    def __str__(self):
        return self.MovieTitle