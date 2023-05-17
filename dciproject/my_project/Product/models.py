from django.db import models

# Create your models here.
class Product(models.Model):
   # product_id (ID) use builtin ID
   product_name= models.CharField(max_length=30)
   product_category = [] # might be a class
   product_description = models.TextField(max_length=500)
   product_image_url = models.models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
   product_price = models.DecimalField(max_digits=None,decimal_places=2)



