from django.db import models
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
# Create your models here.

class Juego(TimeStampedModel, SoftDeletableModel):
	id_juego				= models.CharField(max_length=50)
	nombre_juego 			= models.TextField(max_length=50)
	tipo_juego 				= models.DateTimeField(max_length=20)
	plataformajuego 		= models.DateTimeField(max_length=20)
	def __str__(self):
		return self.id_juego
