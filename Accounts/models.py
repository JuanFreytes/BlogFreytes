from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatar',blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    
def __str__(self):
    return f"{self.nombre} {self.apellido}"
