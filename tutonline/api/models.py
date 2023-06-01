from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
# nuevarama
class User(AbstractUser):
    USUARIO_CHOICES= (
        ('Estudiante','Estudiante'),
        ('Tutor','Tutor')
    )
    tipoDeUsuario = models.CharField(null=False, max_length=10,choices=USUARIO_CHOICES,default='Estudiante', verbose_name='Tipo de usuario')
    rut = models.CharField(unique=True, null=False, max_length=12, verbose_name="Rut")
    fechaNacimiento = models.DateField(null=False,verbose_name="Fecha de nacimiento", default=datetime.date.today)
    numeroTelefono = models.IntegerField(null=False, default=00000000)
    region = models.CharField(null=False, max_length=30, verbose_name="Region", default="")
    comuna = models.CharField(null=False, max_length=30, verbose_name="Comuna", default="")
    fotoPerfil = models.ImageField(null=True, verbose_name="Foto de perfil", default='../img/usuarios.png')
    saldo = models.DecimalField(null=False,max_digits=10,decimal_places=2, default=0)

    def __str__(self):
        return self.rut

class Profesion(models.Model):
    VALIDACION_CHOICES= (
        ('No','No'),
        ('Si','Si'),
        ('En proceso','En proceso')
    )
    codigoVerificador = models.CharField(primary_key=True, null=False, max_length=100,verbose_name="Codigo verificador")
    institucion = models.CharField(null=False, max_length=30, verbose_name="Institucion")
    profesion = models.CharField(null=False, max_length=30,verbose_name="Profesion")
    anioEgreso = models.DateField(verbose_name="Anio de egreso")
    tituloValidado = models.CharField(null=True, max_length=10,verbose_name="Titulo validado",choices=VALIDACION_CHOICES,default='En proceso')
    idProfesor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "Profesiones"
        db_table = "Profesion"
    def __str__(self):
        return f"Codigo verificador: {self.codigoVerificador} | Institucion: {self.institucion} | Profesion: {self.profesion} | Anio de egreso: {self.anioEgreso} | ¿Titulo Validado?: {self.tituloValidado} | {self.idProfesor}"

class Descripcion(models.Model):
    descripcionTutor = models.CharField(null=False, max_length=100,verbose_name="Descripicion del tutor")
    idProfesor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "Descripciones"
        db_table = "Descripcion"
    def __str__(self):
        return f"ID: {self.id} | Descripcion del tutor: {self.descripcionTutor} | {self.idProfesor}"
    
class Asignatura(models.Model):
    nombreAsignatura = models.CharField(null=False,max_length=30,verbose_name="Nombre de la asignatura")
    carreraPerteneciente = models.CharField(null=False,max_length=30,verbose_name="Carrera a la que pertenece")
    descripcionAsignatura = models.CharField(null=False,max_length=500,verbose_name="Descripcion de la asignatura")

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        db_table = "Asignatura"
    def __str__(self):
        return f"ID: {self.id} | Asignatura: {self.nombreAsignatura} | Carrera: {self.carreraPerteneciente}"

class Clase(models.Model):
    fecha = models.DateField(verbose_name="Fecha de la clase")
    hora = models.TimeField(verbose_name="Hora de la clase")
    modalidad = models.CharField(null=False,max_length=10,verbose_name="Modadlidad de la clase")
    tarifa = models.DecimalField(null=False,max_digits=10,decimal_places=2, default=0)
    idProfesor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
        db_table = "Clase"
    def __str__(self):
        return f"{self.idProfesor} | Fecha: {self.fecha} | Hora: {self.hora} | Modalidad: {self.modalidad} | ID asignatura: {self.idAsignatura}"

class Publicacion(models.Model):
    titulo = models.CharField(null=False,max_length=30,verbose_name="Titulo de la publicacion")
    descripcionPublicacion = models.CharField(null=False,max_length=100,verbose_name="Descripcion de la publicacion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de la publicacion")
    hora = models.TimeField(auto_now_add=True, verbose_name="Hora de la publicacion")
    idEstudiante = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE,null=False)
    
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
        db_table = "Publicacion"

    def __str__(self):
        return f"ID: {self.id} | Fecha: {self.fecha} | Hora: {self.hora} | {self.idEstudiante} | ID asignatura: {self.idAsignatura}"
    
class Comentario(models.Model):
    comentario = models.CharField(null=False,max_length=50,verbose_name="Comentario")
    valoracion = models.IntegerField (null=False,verbose_name="Valoracion",default=1)
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha del comentario")
    idEstudianteEmisor = models.ForeignKey(User, related_name='comentarios_enviados', on_delete=models.CASCADE, null=False)
    idProfesorReceptor = models.ForeignKey(User, related_name='comentarios_recibidos', on_delete=models.CASCADE, null=False)
   
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        db_table = "Comentario"

    def __str__(self):
        return f"ID: {self.id} | Valoracion: {self.valoracion} | Fecha: {self.fecha} | {self.idEstudianteEmisor} | {self.idProfesorReceptor}"
    
class ClaseAgendada(models.Model):
    idEstudiante = models.ForeignKey(User, related_name='estudiante_agendado', on_delete=models.CASCADE, null=False)
    idProfesor = models.ForeignKey(User, related_name='profesor_agendador', on_delete=models.CASCADE, null=False)
    idClase = models.ForeignKey(Clase,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Clase Agendada"
        verbose_name_plural = "Clases Agendadas"
        db_table = "ClaseAgendada"

    def __str__(self):
        return f"ID: {self.id} | {self.idProfesor} | {self.idEstudiante}"
    
class Notificacion(models.Model):
    descripcion = models.CharField(null=False,max_length=100,verbose_name="Descripcion")
    idEstudiante = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "Notificacion"
        verbose_name_plural = "Notificaciones"
        db_table = "Notificacion"

    def __str__(self):
        return f"ID: {self.id} | Descripcion: {self.descripcion} | {self.idEstudiante}"