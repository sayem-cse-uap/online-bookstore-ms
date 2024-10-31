from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  publisher = models.CharField(max_length=255)
  description = models.TextField()
  price = models.IntegerField()
  stock = models.IntegerField()
  book_type = models.CharField(max_length=50)
  img = models.ImageField(upload_to='book_images/', default='book_images/default.png')
  category = models.CharField(max_length=100)

  def __str__(self):
    return self.title