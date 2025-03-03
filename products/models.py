from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    is_enable= models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_time']
        verbose_name_plural = 'Categories'















class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    is_enable= models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'











class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    is_enable= models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)




    class Meta:
        db_table = 'file'
        verbose_name = 'file'
        verbose_name_plural = 'files'
        ordering = ['-updated_time']


