from ejer_6 import ArtefactoElectrico

class Camara(ArtefactoElectrico):

	def __init__(self,marca,modelo,color,megapixeles=12):
		super().__init__(marca,modelo,color)
		self.megapixeles = megapixeles
		self.__zoom = 5

	def foto(self):
		print("sacando foto!")

	def __str__(self):
		return super().__str__() + '\nMegapixeles: {}'.format(self.megapixeles)

	def ver_info(self):
		print("CAMARA")
		super().ver_info() 
		print('Megapixeles: ',self.megapixeles)

	def aumentar_zoom(self):
		if self.__zoom < 10:
			self.__zoom += 2

	def desminuir_zoom(self):
		if self.__zoom > 0:
			self.__zoom -= 2

class Telefono(ArtefactoElectrico):

	def __init__(self,marca,modelo,color,numero):
		super().__init__(marca,modelo,color)
		self.numero = numero

	def llamar(self):
		print("llamando!")

	def cortar(self):
		print("finalizando llamada!")

	def ver_info(self):
		print("\nTELEFONO")
		super().ver_info() 
		print('Número: ',self.numero)


class ReproductorMp3(ArtefactoElectrico):

	def __init__(self,marca,modelo,color,peso='20gr'):
		super().__init__(marca,modelo,color)
		self.peso = peso

	def reproducir(self):
		print("reproduciendo música!")

	def ver_info(self):
		print("\nREPRODUCTOR MP3")
		super().ver_info() 
		print('Peso: ',self.peso)

if __name__ == '__main__':
	camara = Camara('SONY','AK47','PLATA',12)
	telefono = Telefono('SAMSUNG','S10','NEGRO',303456)
	reproductor = ReproductorMp3('SANYO','X23','FUCCIA','50 gr')

	# print(camara)
	camara.ver_info()
	telefono.ver_info()
	reproductor.ver_info()


