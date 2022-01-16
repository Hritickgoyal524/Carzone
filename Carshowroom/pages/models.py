from django.db import models

class Team(models.Model):
    firstname=models.CharField( max_length=255)
    lastname=models.CharField( max_length=255)
    designation=models.CharField( max_length=255)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d")
    twitter_link=models.URLField(max_length=100)
    facebook_link=models.URLField(max_length=100)
    google_plus_link=models.URLField(max_length=100)
    created_date=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.firstname
