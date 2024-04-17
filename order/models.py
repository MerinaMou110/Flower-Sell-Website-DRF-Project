from django.db import models
from django.contrib.auth.models import User
from category.models import flower
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        
        ('Complete', 'Complete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(flower, on_delete=models.CASCADE)
   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} -user ID {self.user.id}- {self.user.username}"