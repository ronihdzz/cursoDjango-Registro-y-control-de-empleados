from django.db import models
from applications.departamento.models import  Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad=models.CharField('Habilidad:',max_length=50)

    class Meta:
        # como referirnos a una instancia
        verbose_name='Habilidad'
        # como referirnos a todas nuestras instancias
        verbose_name_plural='Habilidades de empleados'
        # ordenando de forma descenente
        ordering= ['-id']
        # no se permite que la combinación de los atributos de
        # la lista den el mismo resultado
        unique_together=['habilidad','id']
    def __str__(self):
        return '{}-{}'.format(self.id,self.habilidad)

class Empleado(models.Model):
    JOB_CHOICES=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),        
        ('2', 'MARKETING DIGITAL'),
        ('3','PROGRAMADOR'),
        ('4','GESTOR DE VENTAS'),
        ('5','RECLUTADOR'),
        ('6','LIDER DE PROYECTO'),
        ('7', 'OTRO'),
    )
    first_name=models.CharField('Nombre:',max_length=50)
    last_name=models.CharField('Apellido:',max_length=50)
    job=models.CharField('Trabajo:', max_length=1, choices=JOB_CHOICES)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)
    habilidades=models.ManyToManyField(Habilidades)
    avatar=models.ImageField(upload_to='empleado',blank=True,null=True)
    def __str__(self):
        return ' {} {}  '.format(self.first_name,self.last_name)



