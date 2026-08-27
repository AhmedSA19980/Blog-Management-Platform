from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   # default is the name of image it has be the same name of picture(name of picture here, and in the same file )

   def __str__(self):
      return f'{self.user.username} Profile'

   #def save(self):
      #super().save()  #if keep this code runing you got type error (force_insert)
      img = Image.open(self.image.path)

      if img.height > 300 or img.width > 300:
         output_size = (300, 300)
         img.thumbnail(output_size)
         img.save(self.image.path)

