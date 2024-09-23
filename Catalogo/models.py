from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=4, null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre
    
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=4, null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='activo')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre