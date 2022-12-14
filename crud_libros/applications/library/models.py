from distutils.command.upload import upload
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Titulo', max_length=100)
    image = models.ImageField(verbose_name='Imagen',upload_to='images/', null=True)
    description = models.TextField(verbose_name='Descripción', max_length=300)

    def __str__(self):
        return self.title
        
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
