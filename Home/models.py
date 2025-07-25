from django.db import models

class Sell(models.Model):
    product_name = models.CharField(max_length=100)
    product_age = models.CharField(max_length=100)
    product_discription = models.TextField()
    product_price = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, default='9999999999')
    product_file = models.ImageField(upload_to='images/')  # Cloudinary will handle this path

    def __str__(self):
        return self.product_name
