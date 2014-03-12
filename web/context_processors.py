import datetime

def Edicion(request):
	fecha_edicion = datetime.datetime.now()
	return {'fecha_edicion': fecha_edicion}