from django.db import models


class Home(models.Model):
    imagenPortada=models.ImageField(upload_to='imagenesPortada',blank=True,null=True)
    fraseCelebre=models.CharField(max_length=150,default="")


    def __str__(self):
        return "Imagen con codigo: {}".format(self.id)
        