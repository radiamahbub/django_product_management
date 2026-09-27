from django.db import models

# Create your models here.
class ProductModel(models.Model):

    PRODUCT_TYPES = [
<<<<<<< HEAD
        ('Gadgets','Gadgets'),
        ('Devices','Devices'),
        ('Robots','Robots')
=======
        ('Fruits','Fruits'),
        ('Grocery','Grocery'),
        ('Fashion','Fashion'),
>>>>>>> 5f9ec7a (new commits)
    ]
    
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    production_date = models.DateField(null=True)
    image = models.ImageField(upload_to='media/product_img', null=True)
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=20, null=True)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
=======
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
>>>>>>> 5f9ec7a (new commits)

    def __str__(self):
        return f'{self.name}'



