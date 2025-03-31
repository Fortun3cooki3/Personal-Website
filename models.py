from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Skills(models.Model):
  skills = models.CharField(max_length=100, unique=True, db_index=True)
  
  def __str__(self):
    return self.skills


class Projects(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  full_description = models.TextField(blank=True)
  url = models.URLField(blank=True, default="https://www.linkedin.com/in/merlijn-wolters-0b3450140/")
  git_hub = models.URLField(blank=True, default="https://www.linkedin.com/in/merlijn-wolters-0b3450140/")
  image = models.ImageField(null=True, blank=True, upload_to='images')
  slug = models.SlugField( default= "", null=False, blank=True, db_index=True)

  def get_absolute_url(self):
      return reverse("project", args=[self.slug])

  def __str__(self):
    return self.title


class Cv (models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  url = models.URLField(null=True, blank=True)
  image = models.ImageField(null=True, blank=True, upload_to='images/')
  skills = models.ManyToManyField(Skills)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)

  def __str__(self):
    return self.title
  
class CoverLetter(models.Model):
  my_name = models.CharField(max_length=50)
  picture = models.ImageField(null=True, blank=True, upload_to='images/')
  coverletter = models.TextField(blank=True)

  def __str__(self):
      return self.my_name
    
class Refrences(models.Model):
  ref_name = models.CharField(max_length=50)
  date = models.DateField(blank=True)
  refrence = models.TextField(blank=True)

  def __str__(self):
      return self.ref_name
  

class Webinfo(models.Model):
    webliner = models.CharField(max_length=100, blank=True)
    webinfo = models.TextField(blank=True)

    def __str__(self):
      return self.webinfo