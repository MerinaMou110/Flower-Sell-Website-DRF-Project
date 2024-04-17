from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
    


class flower(models.Model):
    title = models.CharField(max_length=50, default='Rose')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to="category/images/")
    categories = models.ManyToManyField(category)
    details=models.TextField()
    
    def __str__(self):
        return self.title 