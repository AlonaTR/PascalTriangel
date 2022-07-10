from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
# class Movie(models.Model):
# 	name = models.CharField(max_length=40), # charfield make str
# 	rating = models.IntegerField()

	
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget= models.IntegerField(default=10000000)
    slug= models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_movie', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating} %'

    