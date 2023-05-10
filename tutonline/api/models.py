from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Administrador(models.Model):
    rutAdmin = models.CharField(primary_key=True, null=False, max_length=12, verbose_name="Rut Administrador", )
    nombreAdmin = models.CharField(null=False, max_length=20, verbose_name="Nombre", )
    apellidoPaternoAdmin = models.CharField(null=False, max_length=20,verbose_name="Apellido Paterno")
    apellidoMaternoAdmin = models.CharField(null=False, max_length=20,verbose_name="Apellido Materno")
    correoAdmin = models.CharField(null=False, max_length=35,verbose_name="Correo")
    contrasenaAdmin = models.CharField(null=False, max_length=12, verbose_name="Contrasenia")
    numeroTelefonoAdmin = models.IntegerField()
      
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table = "Administrador"
    def __str__(self):
        return f"{self.rutAdmin} ; {self.nombreAdmin} {self.apellidoPaternoAdmin} {self.apellidoMaternoAdmin}"

class Profesor(models.Model):
    rutProf = models.CharField(primary_key=True, null=False, max_length=12, verbose_name="Rut Profesor")
    nombreProf = models.CharField(null=False, max_length=20, verbose_name="Nombre", )
    apellidoPaternoProf = models.CharField(null=False, max_length=20,verbose_name="Apellido Paterno")
    apellidoMaternoProf = models.CharField(null=False, max_length=20,verbose_name="Apellido Materno")
    fechaNacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    correoProf = models.CharField(null=False, max_length=35,verbose_name="Correo")
    contrasenaProf = models.CharField(null=False, max_length=12, verbose_name="Contrasenia")
    numeroTelefonoProf = models.IntegerField()
    regionProf = models.CharField(null=False, max_length=30, verbose_name="Region")
    comunaProf = models.CharField(null=False, max_length=30, verbose_name="Comuna")
    fotoPerfil = models.BinaryField(verbose_name="Foto de perfil")
        
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        db_table = "Profesor"
    def __str__(self):
        return f"{self.rutProf} ; {self.nombreProf} {self.apellidoPaternoProf} {self.apellidoMaternoProf}"

class estudiante(models.Model):
    rutEst = models.CharField(primary_key=True, null=False, max_length=12, verbose_name="Rut Estudiante")
    nombreEst = models.CharField(null=False, max_length=20, verbose_name="Nombre", )
    apellidoPaternoEst = models.CharField(null=False, max_length=20,verbose_name="Apellido Paterno")
    apellidoMaternoEst = models.CharField(null=False, max_length=20,verbose_name="Apellido Materno")
    fechaNacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    correoEst = models.CharField(null=False, max_length=35,verbose_name="Correo")
    contrasenaEst = models.CharField(null=False, max_length=12, verbose_name="Contrasenia")
    numeroTelefonoEst = models.IntegerField()
    regionEst = models.CharField(null=False, max_length=30, verbose_name="Region")
    comunaEst = models.CharField(null=False, max_length=30, verbose_name="Comuna")
    fotoPerfil = models.BinaryField(verbose_name="Foto de perfil")
    saldo = models.DecimalField(null=False,max_digits=10,decimal_places=2, default=0)

    class Meta:
        db_table = "Estudiante"
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
    def __str__(self):
        return f"{self.rutEst} ; {self.nombreEst} {self.apellidoPaternoEst} {self.apellidoMaternoEst}"

class profesion(models.Model):
    codigoVerificador = models.CharField(primary_key=True, null=False, max_length=100,verbose_name="Codigo verificador")
    institucion = models.CharField(null=False, max_length=30, verbose_name="Institucion")
    profesion = models.CharField(null=False, max_length=30,verbose_name="Profesion")
    anioEgreso = models.DateField()
    tituloValidado = models.CharField(null=True, max_length=9,verbose_name="Titulo validado")
    rutProfProfesion = models.ForeignKey(Profesor,on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "Profesiones"
        db_table = "Profesion"

class descripcion(models.Model):
    idDescripcion = models.IntegerField(primary_key=True,null=False,verbose_name="Id Descripcion")
    descripcionTutor = models.CharField(null=False, max_length=100,verbose_name="Descripicion del tutor")
    rutProfDesc = models.ForeignKey(Profesor,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "Descripciones"
        db_table = "Descripcion"
        