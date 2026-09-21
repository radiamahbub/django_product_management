from django.db import models

# Create your models here.
class ProductModel(models.Model):
    
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField(null=True)
    production_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='media/product_img', null=True)

    def __str__(self):
        return f'{self.name}-{self.price}'


# name, description, price, production_date
