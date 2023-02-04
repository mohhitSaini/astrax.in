from django.db import models

class Speaker(models.Model):
    name=models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/',default='astrax23/images/speaker_images/default.jpg')

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name=models.TextField(max_length=100)
    website=models.TextField()
    type=models.TextField()
    image=models.ImageField(upload_to="images/",default='astrax23/images/sponsor_images/default.jpg')

    
    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    relationship_status=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',default='astrax23/images/team_images/default.jpg')

    def __str__(self):
        return self.name

