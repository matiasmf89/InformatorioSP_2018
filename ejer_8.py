from ejer_7 import Telefono,Camara,ReproductorMp3

class Celular(Telefono,Camara,ReproductorMp3):
	def __init__(self,marca,model,color,numero):
		super().__init__(marca,model,color,numero)
		self.lista_contactos = list()

	def ingersar_mensaje(self):
		self.mensaje = input('Mensaje: ')

	def enviar_mensaje(self):
		print('Enviando mensaje: ',self.mensaje)

	def ingresar_contacto(self):
		nombre = input('Nombre: ')
		numero = input('Número: ')
		contacto = (nombre,numero)
		self.lista_contactos.append(contacto)

	def ver_lista_contactos(self):
		print('\nLISTA DE CONTACTOS')
		for i in self.lista_contactos:
			print(i)

celular = Celular('SAMSUNG','S10','NEGRO',303456)


print(celular)


celular.foto()
celular.reproducir()
celular.llamar()
celular.cortar()
celular.ingersar_mensaje()
celular.enviar_mensaje()
celular.ingresar_contacto()
celular.ingresar_contacto()
celular.ingresar_contacto()
celular.ver_lista_contactos()