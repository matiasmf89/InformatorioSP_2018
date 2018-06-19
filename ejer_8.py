from ejer_7 import *

class Celular(Telefono,Camara,ReproductorMp3):
	def __init__(self,marca,model,color,numero):
		super().__init__(marca,model,color,numero)

	def mensajear(self):
		self.mensaje = input('Ingrese mensaje: ')
		print('enviando mensaje')

	def filmar(self):
		print("filmando")

	
celular = Celular('SAMSUNG','S10','NEGRO',303456)

# celular.mensajear()

celular.reproducir()
celular.subir_volumen()

celular.ver_info()


# print(__name__)