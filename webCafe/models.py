from django.db import models


# class Image(models.Model):
#     caption=models.CharField(max_length=100)
#     image=models.ImageField(upload_to="img/%y")
#     def __str__(self):
#         return self.caption


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    message = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    description = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='img/%y')
