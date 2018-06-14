from ejer_7 import *

class Celular(Telefono,Camara,ReproductorMp3):
	def __init__(self,marca,model,color,numero):
		super().__init__(marca,model,color,numero)



celular = Celular('SAMSUNG','S10','NEGRO',303456)


print(__name__)