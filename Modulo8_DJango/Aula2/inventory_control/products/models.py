from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        


class Product(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    sale_price = models.FloatField()
    is_perishable = models.BooleanField()
    expiration_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="products", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails", blank=True, null=True)
    enabled = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.__uptade_is_perishable()
        
        #Removendo imagens antigas
        if self.pk:
            old_obj = Product.objects.filter(pk=self.pk).first()
            if old_obj and old_obj.photo != self.photo:
                self.__delete_file_if_exists(old_obj.photo)
            if old_obj and old_obj.thumbnail:
                self.__delete_file_if_exists(old_obj.thumbnail)
               
        super(Product, self).save(*args, **kwargs)
        
        self.__create_thubnail()
        super(Product, self).save(*args, **kwargs)
        
    def __uptade_is_perishable(self):
        self.is_perishable = bool(self.expiration_date)        
       
    def __create_thubnail(self):
        if not self.photo:
            return
            
        # Gerando thumbnail
        img = Image.open(self.photo.path)
        # Redimensionar a imagem
        size = (30,30)
        img.thumbnail(size)
        # Salvar a imagem redimensionada
        thumb_io = BytesIO()
        img.save(thumb_io, img.format, quality=85) 
        # Criar um nome para a thumbnail
        name, extension = os.path.splitext(self.photo.name)
        thumb_filename = f"{name}_thumb{extension}"  
        # Salvando a miniatura
        self.thumbnail.save(thumb_filename, ContentFile(thumb_io.getvalue()), save=False)
        
    def __delete_file_if_exists(self, file):
        if file and os.path.isfile(file.path):
            os.remove(file.path)
            
    def delete(self, *args, **kwargs):
        self.__delete_file_if_exists(self.photo)
        super(Product, self).delete(*args, **kwargs)        
      
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        
        
