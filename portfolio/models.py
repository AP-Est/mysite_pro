from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     pub_date = models.DateField
#     description = models.CharField(max_length=250)
#     # image = models.ImageField(upload_to='blog/images/')
#     url = models.URLField(blank=True)

