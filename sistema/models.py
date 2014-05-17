from django.db import models

# ** Creo que el modelo User tiene todo lo que necesito para manejar las cuentas de los Agentes (Ventas, Recepcion, Captura, Admins)

# Este será el modelo principal, contendrá la informacion principal de cada prospecto/cliente del sistema
class Empresa(models.Model):
	agente = models.ForeignKey(User) # El agente al que pertenece esta empresa
	razonsocial = models.CharField(max_length=250, blank=True, null=True) # La razon social de la empresa
	nombre = models.CharField(max_length=140, blank=True, null=True) # El nombre comercial de la empresa
	pagweb = models.CharField(max_length=90, blank=True, null=True) # La página web de la empresa
	expo = models.ForeignKey(Expo) # Si el prospecto se obtuvo a traves de una Expo, seleccionarla
	status = models.ForeignKey(Status) # El status en que se encuentra el prospecto
	creado = models.SmallIntegerField(default=self.agente) # El agente que creo esta empresa, cuando se da de alta deber ser el mismo que el agente, pero si esta empresa se traspasa a otro agente, este campo no debe cambiar para saber quien lo creo
	fingreso = models.DateTimeField(auto_now_add=True, null=True) # La fecha en que se ingresó
	factualizado = models.DateTimeField(auto_now=True, null=True) # La fecha en que se actualizó esta empresa, esta tambien se debería de actualizar cuando se actualiza un modelo hijo
	sttdir = models.BooleanField(default=True) # Se mostrará o no en el directorio de proveedores
	patrodir = models.BooleanField(default=False) # Está patrocinado en el directorio de proveedores
	imglogodir = models.ImageField(upload_to='img/dir/logos/', blank=True, null=True) # El logo de la empresa para el directorio de proveedores
	imgpatrodir = models.ImageField(upload_to='img/dir/patro/', blank=True, null=True) # El anuncio patrocinado en el directorio de proveedores
	giros = models.ManyToManyField(Giro) # Esta sera la relacion para agregar los giros necesarios de cada empresa


class Sucursal(models.Model):
	empresa = models.ForeignKey(Empresa) # La empresa a la que pertenece esta sucursal
	agente = models.ForeignKey(User) # El agente que tiene la sucursal, tal vez no lo use ya que otros agentes deben poder ver esta sucursal
	nombre = models.CharField(max_length=100, default="Matriz") # El nombre de la sucursal
	dir = models.CharField(max_length=100, blank=True) # Calle y num
	col = models.CharField(max_length=50, blank=True) # Colonia
	cp = models.CharField(max_length=10, blank=True) # Codigo Postal
	telvtas = models.CharField(max_length=15, blank=True, null=True) # Telefono del dpto de Ventas, este es el telefono que se mostrara en el directorio de proveedores
	emailvtas = models.CharField(max_length=80, blank=True, null=True) # Email del dpto de Ventas, este es el email que se mostrara en el directorio de proveedores
	pais = models.ForeignKey(Pais) # Siempre debe estar preseleccionado México
	edo = models.ForeignKey(Estado) # Siempre deben estar precargados todos los estados de México
	cd = models.ForeignKey(Ciudad) # Se cargaran las ciudades del estado que se seleccione
	fingreso = models.DateTimeField(auto_now_add=True, null=True) # Fecha en que se ingreso
	factualizado = models.DateTimeField(auto_now=True, null=True) # Fecha en que se actualizo


class Contacto(models.Model):
	empresa = models.ForeignKey(Empresa) # La empresa a la que pertenece este contacto
	agente = models.ForeignKey(User) # El agente al que pertenece este contacto actualmente
	sucursal = models.ForeignKey(Sucursal) # La sucursal a la que pertenece este contacto
	nombre = models.CharField(max_length=200, blank=True, null=True) # El nombre del contacto
	puesto = models.CharField(max_length=80, blank=True, null=True) # El puesto del contacto
	movil = models.CharField(max_length=15, blank=True, null=True) # Su número de movil
	tel1 = models.CharField(max_length=15, blank=True, null=True) # Telefono 1
	tel2 = models.CharField(max_length=15, blank=True, null=True) # Telefono 2
	email1 = models.EmailField(max_length=80, blank=True, null=True) # Email 1
	email2 = models.EmailField(max_length=80, blank=True, null=True) # Email 2
	creado = models.SmallIntegerField(default=self.agente) # El agente que creo este contacto, igual que en las Empresas, este campo se debe de mantener fijo si el agente cambia
	fingreso = models.DateTimeField(auto_now_add=True, null=True) # La fecha en que se ingresó
	factualizado = models.DateTimeField(auto_now=True, null=True) # La fecha en que se actualizó este contacto, al actualizarse este modelo tambien deberia de actualizar a su Empresa
	sttboletine1 = models.BooleanField(default=False) # El status en el boletin del email 1
	sttboletine2 = models.BooleanField(default=False) # El status en el boletin del email 2


class Seguimiento(models.Model):
	empresa = models.ForeignKey(Empresa) # La empresa a la que pertenece el seguimiento
	agente = models.ForeignKey(User) # El usuario al que pertenece el seguimiento
	contacto = models.ForeignKey(Contacto) # A que contacto se le dio el seguimiento
	tipo = models.ForeignKey(TipoSeg) # Tipo de Seguimiento (Visita, llamada, Email, etc)
	fecha = models.DateTimeField(auto_now_add=True) # Esta es la fecha en la que se da de alta el seguimiento, puede ser editada por el usuario solo cuando se inserta el registro
	aviso = models.DateTimeField() # Este aviso se usara si el agente desea recibir un aviso a futuro
	comentario = models.TextField() # El comentario del seguimiento
	stt = models.BooleanField() # Define si ya se completo el seguimiento o aun esta pendiente (se usara para avisos a futuro y llamadas entrantes)
	tiponum = models.SmallIntegerField() # Este campo llevara un contador ascendente por empresa, agente y tipo, se usara para mostrar en la agenda con colores distintos las primeras visitas
	creado = models.SmallIntegerField(default=self.agente) # El agente que creo este registro de seguimiento, debe permanecer intacto despues de insertado


# En este modelo se registrarán las llamadas entrantes de las personas que llaman para pedir informes
class Recepcion(models.Model):
	contacto = models.CharField(max_length=100, blank=True, null=True)
	empresa = models.CharField(max_length=60, blank=True, null=True)
	tel = models.CharField(max_length=30, blank=True, null=True)
	email = models.CharField(max_length=80, blank=True, null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	pais = models.ForeignKey(Pais) # Siempre debe estar preseleccionado México
	edo = models.ForeignKey(Estado) # Siempre deben estar precargados todos los estados de México
	cd = models.ForeignKey(Ciudad) # Se cargaran las ciudades del estado que se seleccione
	periodico = models.BooleanField() # Este campo y todos los booleanos siguientes solo se usan para la pregunta de como se enteron de nosotros y son solo checkbox's
	correo = models.BooleanField()
	boletin = models.BooleanField()
	mapa = models.BooleanField()
	buscador = models.BooleanField()
	recomendacion = models.BooleanField()
	visita = models.BooleanField()
	redsocial = models.BooleanField()
	otros = models.BooleanField()
	agente = models.ForeignKey(User) # El usuario al que se le asigno la llamada entrante (En este listado solo debe haber Usuarios del grupo de Ventas)
	empresa = models.SmallIntegerField() # El pk final con el que se registro o se encontro en el modelo de Empresa, para tener la relacion


class Etiqueta(models.Model):
	suscriptor = models.ManyToManyField(Contacto) # Aqui cada agente podrá seleccionar sus contactos (la idea es que puedan ver en la lista 'Empresa' - 'Contacto') y ahi seleccionen a quien les llegara la revista fisicamente


# En este modelo llevare un registro de los correos que tengo agregados en el boletin
class Boletin(models.Model):
	contacto = models.ForeignKey(User) # El num de Contacto
	email = models.CharField(max_length=80, unique=True) # El correo electronico del contacto, no puede haber correos repetidos en esta lista, todos deben ser unicos


class Status(models.Model):
	nombre = models.CharField(max_length=30)


class Expo(models.Model):
	nombre = models.CharField(max_length=50)


class Pais(models.Model):
	nombre = models.CharField(max_length=50)


class Estado(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)


class Ciudad(models.Model):
	nombre = models.CharField(max_length=100)
	edo = models.ForeignKey(Estado)


class TipoSeg(models.Model):
	nombre = models.CharField(max_length=30)


class Giro(models.Model):
	nombre = models.CharField(max_length=200)