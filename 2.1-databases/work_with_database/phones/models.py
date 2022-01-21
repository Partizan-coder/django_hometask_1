from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=110)
    release_date = models.IntegerField(default=0)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(default=slugify(name))

