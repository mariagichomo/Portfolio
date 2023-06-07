from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill (models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

name = models.CharField(max_length=20, blank= True, null=True)
score = models.IntegerField(default=80, blank=True, null=True)
image = models.FileField(blank=True, null=True, upload_to="skills")
is_key_skill = models.BooleanField(default=False)

def __str__(self):
    return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True, null=True, upload_to="avatars")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

