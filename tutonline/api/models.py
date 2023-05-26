from django.db import models

# Create your models here.

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
    fotoPerfil = models.ImageField(null=True, verbose_name="Foto de perfil", default='../img/usuarios.png')
        
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        db_table = "Profesor"
    def __str__(self):
        return f"Rut: {self.rutProf} | Nombre profesor: {self.nombreProf} {self.apellidoPaternoProf} {self.apellidoMaternoProf}"

class Estudiante(models.Model):
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
    fotoPerfil = models.BinaryField(null=True, verbose_name="Foto de perfil")
    saldo = models.DecimalField(null=False,max_digits=10,decimal_places=2, default=0)

    class Meta:
        db_table = "Estudiante"
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
    def __str__(self):
        return f"Rut: {self.rutEst} | Nombre estudiante: {self.nombreEst} {self.apellidoPaternoEst} {self.apellidoMaternoEst}"

class Profesion(models.Model):
    codigoVerificador = models.CharField(primary_key=True, null=False, max_length=100,verbose_name="Codigo verificador")
    institucion = models.CharField(null=False, max_length=30, verbose_name="Institucion")
    profesion = models.CharField(null=False, max_length=30,verbose_name="Profesion")
    anioEgreso = models.DateField(verbose_name="Anio de egreso")
    tituloValidado = models.CharField(null=True, max_length=9,verbose_name="Titulo validado")
    rutProf = models.ForeignKey(Profesor,on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "Profesiones"
        db_table = "Profesion"
    def __str__(self):
        return f"Codigo verificador: {self.codigoVerificador} | Institucion: {self.institucion} | Profesion: {self.profesion} | Anio de egreso: {self.anioEgreso} | ¿Titulo Validado?: {self.tituloValidado} | {self.rutProf}"

class Descripcion(models.Model):
    descripcionTutor = models.CharField(null=False, max_length=100,verbose_name="Descripicion del tutor")
    rutProf = models.ForeignKey(Profesor,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "Descripciones"
        db_table = "Descripcion"

    def __str__(self):
        return f"ID: {self.id} | Descripcion del tutor: {self.descripcionTutor} | {self.rutProf}"
    
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
    rutProf = models.ForeignKey(Profesor, on_delete=models.CASCADE,null=False)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
        db_table = "Clase"
    def __str__(self):
        return f"{self.rutProf} | Fecha: {self.fecha} | Hora: {self.hora} | Modalidad: {self.modalidad} | ID asignatura: {self.idAsignatura}"

class Publicacion(models.Model):
    titulo = models.CharField(null=False,max_length=30,verbose_name="Titulo de la publicacion")
    descripcionPublicacion = models.CharField(null=False,max_length=100,verbose_name="Descripcion de la publicacion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de la publicacion")
    hora = models.TimeField(auto_now_add=True, verbose_name="Hora de la publicacion")
    rutEst = models.ForeignKey(Estudiante,on_delete=models.CASCADE,null=False)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE,null=False)
    
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
        db_table = "Publicacion"

    def __str__(self):
        return f"ID: {self.id} | Fecha: {self.fecha} | Hora: {self.hora} | {self.rutEst} | ID asignatura: {self.idAsignatura}"
    
class Comentario(models.Model):
    comentario = models.CharField(null=False,max_length=50,verbose_name="Comentario")
    valoracion = models.IntegerField (null=False,verbose_name="Valoracion",default=1)
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha del comentario")
    rutEst = models.ForeignKey(Estudiante,on_delete=models.CASCADE,null=False)
    rutProf = models.ForeignKey(Profesor,on_delete=models.CASCADE, null=False)
   
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        db_table = "Comentario"

    def __str__(self):
        return f"ID: {self.id} | Valoracion: {self.valoracion} | Fecha: {self.fecha} | {self.rutEst} | {self.rutProf}"
    
class ClaseAgendada(models.Model):
    rutProf = models.ForeignKey(Profesor,on_delete=models.CASCADE, null=False)
    rutEst = models.ForeignKey(Estudiante,on_delete=models.CASCADE,null=False)
    idClase = models.ForeignKey(Clase,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Clase Agendada"
        verbose_name_plural = "Clases Agendadas"
        db_table = "ClaseAgendada"

    def __str__(self):
        return f"ID: {self.id} | {self.rutProf} | {self.rutEst}"
    
class Notificacion(models.Model):
    descripcion = models.CharField(null=False,max_length=100,verbose_name="Descripcion")
    rutEst = models.ForeignKey(Estudiante,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = "Notificacion"
        verbose_name_plural = "Notificaciones"
        db_table = "Notificacion"

    def __str__(self):
        return f"ID: {self.id} | Descripcion: {self.descripcion} | {self.rutEst}"