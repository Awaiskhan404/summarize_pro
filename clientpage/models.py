from django.db import models
from autoslug import AutoSlugField

class ListViewPdf(models.Model):
    name = models.CharField(max_length=50)
    pdffile = models.FileField()
    is_paid = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    email = models.EmailField()
    number_page = models.IntegerField()
    total_price = models.FloatField()
    slug = AutoSlugField(populate_from='name', unique=True)
    def __str__(self):
        return self.name
    
