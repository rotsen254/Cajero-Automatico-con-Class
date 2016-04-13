class Ahorro:

	v = False

	def __init__(self):
		self.__clave = 1234
		self.__dinero = 2500
		self.encendido = False
		self.__valido = False
		


	def encender(self):
		if (self.encendido == False):
			self.encendido = True
	
	def apagar(self):
		if (self.encendido == True):
			self.encendido = False
	
	def validar_cuenta(self):
		if (self.encendido == True):
			clave = int(raw_input("Introduzca su clave: "))
			if(self.__clave == clave):
				self.__valido = True
				self.v = True
				print "Acceso permitido"
			else:
				print "Clave invalida"

	def validar_cuenta_ing(self):
		if (self.encendido == True):
			clave = int(raw_input("Enter your password: "))
			if(self.__clave == clave):
				self.__valido = True
				self.v = True
				print "Access granted"
			else:
				print "key invalidates"

	def cambiar_clave(self):
		if (self.encendido == True):		
			if (self.__valido == True):			
				clave = int(raw_input("Introduzca su nueva clave: "))
				clave_nueva = int(raw_input("Confirme su nueva clave: "))
				if( self.__clave != clave and clave == clave_nueva):
					self.__clave = clave_nueva
					print "Su nueva clave es: " 
					print self.__clave

	def cambiar_clave_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):			
				clave = int(raw_input("Enter your new password: "))
				clave_nueva = int(raw_input("Confirm your new password: "))
				if( self.__clave != clave and clave == clave_nueva):
					self.__clave = clave_nueva
					print "Your new password is: " 
					print self.__clave
								
				else:				
					print "Failed to change password"

	def consultar_saldo(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				print "Clave: ", self.__clave
				print "Saldo: "+str(self.__dinero)+"bsf"

	def consultar_saldo_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				print "code: ", self.__clave
				print "residue: "+str(self.__dinero)+"bsf"

	def retirar(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				opcion = int(raw_input("Seleccione la cantidad que desea retirar: \n(1)500bsf\n(2)300bsf\n(3)200bsf\n(4)100bsf\n(5)50bsf\n(6)Escribir catidad\n"))
				if (opcion > 0 and opcion < 7):
					if (opcion == 1 and self.__dinero >= 500):
						self.__dinero = self.__dinero - 500
			
					if (opcion == 2 and self.__dinero >= 300):
						self.__dinero = self.__dinero - 300

					if (opcion == 3 and self.__dinero >= 200):
						self.__dinero = self.__dinero - 200

					if (opcion == 4 and self.__dinero >= 100):
						self.__dinero = self.__dinero - 100

					if (opcion == 5 and self.__dinero >= 50):
						self.__dinero = self.__dinero - 50

					if (opcion == 6):
						dinero = int(raw_input("Ingrese la cantidad que desea retirar:\n"))

						if(self.__dinero >= dinero and dinero > -1):
							self.__dinero = self.__dinero - dinero

						else:
							print "Saldo insuficiente/Error en el monto"
							return

					ticket = int (raw_input("Seleccione una opcion:\n(1)Imprimier ticket presione\n(2)Para mostrar por pantalla presione\n"))
					if (ticket == 1):
						print "Ya puede retirar el ticket"	
						return 

					if (ticket == 2):
						print "Su saldo es de: "+ str(self.__dinero)+"bsf"
						return 

					else:
						print "Error al seleccionar una opcion"

				else:
					print "Error al seleccionar una opcion"

	def retirar_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				opcion = int(raw_input("Select the amount you wish to withdraw: \n(1)500bsf\n(2)300bsf\n(3)200bsf\n(4)100bsf\n(5)50bsf\n(6)Write amount\n"))
				if (opcion > 0 and opcion < 7):
					if (opcion == 1 and self.__dinero >= 500):
						self.__dinero = self.__dinero - 500
					
					if (opcion == 2 and self.__dinero >= 300):
						self.__dinero = self.__dinero - 300
		
					if (opcion == 3 and self.__dinero >= 200):
						self.__dinero = self.__dinero - 200
		
					if (opcion == 4 and self.__dinero >= 100):
						self.__dinero = self.__dinero - 100
		
					if (opcion == 5 and self.__dinero >= 50):
						self.__dinero = self.__dinero - 50
		
					if (opcion == 6):
						dinero = int(raw_input("Enter the amount you wish to withdraw:\n"))
		
						if(self.__dinero >= dinero and dinero > 0):
							self.__dinero = self.__dinero - dinero

						else:
							print "Insufficient balance/Error in the mount"
							return

					ticket = int (raw_input("Select an option:\n(1)Print ticket press\n(2)To display the screen press\n"))
					if (ticket == 1):
						print "You can remove the ticket"	
						return 
		
					if (ticket == 2):
						print "Your balance is: "+ str(self.__dinero)+"bsf"
						return 

					else:
						print "Failed to select an option"

				else:
					print "Failed to select an option"

class Corriente:
	
	v = False
	
	def __init__(self):
		self.__clave = 1221
		self.__dinero = 1800
		self.encendido = False
		self.__valido = False


	def encender(self):
		if (self.encendido == False):
			self.encendido = True
	
	def apagar(self):
		if (self.encendido == True):
			self.encendido = False
	
	def validar_cuenta(self):
		if (self.encendido == True):
			clave= int(raw_input("Introduzca su clave: "))
			if(self.__clave == clave):
				self.__valido = True
				self.v = True
				print "Acceso permitido"
			else:
				print "Clave invalida"

	def validar_cuenta_ing(self,clave):
		if (self.encendido == True):
			clave = int(raw_input("Enter your password: "))
			if(self.__clave == clave):
				self.__valido = True
				self.v = True
				print "Access granted"
			else:
				print "key invalidates"

	def cambiar_clave(self):
		if (self.encendido == True):		
			if (self.__valido == True):			
				clave = int(raw_input("Introduzca su nueva clave: "))
				clave_nueva = int(raw_input("Confirme su nueva clave: "))
				if( self.__clave != clave and clave == clave_nueva):
					self.__clave = clave_nueva
					print "Su nueva clave es: " 
					print self.__clave

	def cambiar_clave_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):			
				clave = int(raw_input("Enter your new password: "))
				clave_nueva = int(raw_input("Confirm your new password: "))
				if( self.__clave != clave and clave == clave_nueva):
					self.__clave = clave_nueva
					print "Your new password is: " 
					print self.__clave
								
				else:				
					print "Failed to change password"

	def consultar_saldo(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				ticket = int (raw_input("Seleccione una opcion:\n(1)Imprimier ticket presione\n(2)Para mostrar por pantalla presione\n"))
				if(ticket == 1):
					print "Ya puede retirar el ticket"	
					return 

				if (ticket == 2):
					print "Su saldo es de: "+ str(self.__dinero)+"bsf"
					return 

				else:
					print "Error al seleccionar una opcion"

	def consultar_saldo_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				ticket = int (raw_input("Select an option:\n(1)Print ticket press\n(2)To display the screen press\n"))
				if (ticket == 1):
					print "You can remove the ticket"	
					return 
		
				if (ticket == 2):
					print "Your balance is: "+ str(self.__dinero)+"bsf"
					return 

				else:
					print "Failed to select an option"

		
	def retirar(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				opcion = int(raw_input("Seleccione la cantidad que desea retirar: \n(1)500bsf\n(2)300bsf\n(3)200bsf\n(4)100bsf\n(5)50bsf\n(6)Escribir catidad\n"))
				if (opcion > 0 and opcion < 7):
					if (opcion == 1 and self.__dinero >= 500):
						self.__dinero = self.__dinero - 500
			
					if (opcion == 2 and self.__dinero >= 300):
						self.__dinero = self.__dinero - 300

					if (opcion == 3 and self.__dinero >= 200):
						self.__dinero = self.__dinero - 200

					if (opcion == 4 and self.__dinero >= 100):
						self.__dinero = self.__dinero - 100

					if (opcion == 5 and self.__dinero >= 50):
						self.__dinero = self.__dinero - 50

					if (opcion == 6):
						dinero = int(raw_input("Ingrese la cantidad que desea retirar:\n"))

						if(self.__dinero >= dinero and dinero > -1):
							self.__dinero = self.__dinero - dinero

						else:
							print "Saldo insuficiente/Error en el monto"
							return

					ticket = int (raw_input("Seleccione una opcion:\n(1)Imprimier ticket presione\n(2)Para mostrar por pantalla presione\n"))
					if (ticket == 1):
						print "Ya puede retirar el ticket"	
						return 

					if (ticket == 2):
						print "Su saldo es de: "+ str(self.__dinero)+"bsf"
						return 

					else:
						print "Error al seleccionar una opcion"

				else:
					print "Error al seleccionar una opcion"

	def retirar_ing(self):
		if (self.encendido == True):		
			if (self.__valido == True):
				opcion = int(raw_input("Select the amount you wish to withdraw: \n(1)500bsf\n(2)300bsf\n(3)200bsf\n(4)100bsf\n(5)50bsf\n(6)Write amount\n"))
				if (opcion > 0 and opcion < 7):
					if (opcion == 1 and self.__dinero >= 500):
						self.__dinero = self.__dinero - 500
					
					if (opcion == 2 and self.__dinero >= 300):
						self.__dinero = self.__dinero - 300
		
					if (opcion == 3 and self.__dinero >= 200):
						self.__dinero = self.__dinero - 200
		
					if (opcion == 4 and self.__dinero >= 100):
						self.__dinero = self.__dinero - 100
		
					if (opcion == 5 and self.__dinero >= 50):
						self.__dinero = self.__dinero - 50
		
					if (opcion == 6):
						dinero = int(raw_input("Enter the amount you wish to withdraw:\n"))
		
						if(self.__dinero >= dinero and dinero >-1):
							self.__dinero = self.__dinero - dinero
						
						else:
							print "Insufficient balance/Error in the mount"
							return

					ticket = int (raw_input("Select an option:\n(1)Print ticket press\n(2)To display the screen press\n"))
					if (ticket == 1):
						print "You can remove the ticket"	
						return 
		
					if (ticket == 2):
						print "Your balance is: "+ str(self.__dinero)+"bsf"
						return 

					else:
						print "Failed to select an option"

				else:
					print "Failed to select an option"
			
			
#Principal



print "Bienvenido al cajero automatico del Banco El Imperio"
print "Introduzca su tarjeta de credito o debito"
print "Su tarjeta sera retenida mientras realiza su operacion, se le avisara cuando la pueda retirar"
idioma= int(raw_input("Seleccione un idioma/Select a language:\n(1)Espa#ol\n(2)Ingles\n"))
if(idioma > 0 and idioma < 3):
	if (idioma == 1):
		tipo = int(raw_input("Seleccione el tipo de cuenta:\n(1)Cuenta de Ahorro\n(2)Cuenta Corriente\n"))
		if(tipo > 0 and tipo < 3):
			if(tipo == 1):
				cajero = Ahorro()
				cajero.encender()
				cajero.validar_cuenta()
				if(cajero.v == True):
					operacion = int(raw_input("Seleccione la operacion que desea realizar:\n(1)Retirar\n(2)Cambiar clave\n(3)Consultar Saldo\n"))
					if(operacion > 0 and operacion < 4):
						if(operacion == 1):
							cajero.retirar()
						if(operacion == 2):
							cajero.cambiar_clave()
						if(operacion == 3):
							cajero.consultar_saldo()
					else:
						print "Error al seleccionar una opcion"
		
			if(tipo == 2):
				cajero = Corriente()
				cajero.encender()
				cajero.validar_cuenta()
				if(cajero.v == True):
					operacion = int(raw_input("Seleccione la operacion que desea realizar:\n(1)Retirar\n(2)Cambiar clave\n(3)Consultar Saldo\n"))
					if(operacion > 0 and operacion < 4):
						if(operacion == 1):
							cajero.retirar()
						if(operacion == 2):
							cajero.cambiar_clave()
						if(operacion == 3):
							cajero.consultar_saldo()
					else:
						print "Error al seleccionar una opcion"
		
		else:
			print "Error al seleccionar una opcion"


	if (idioma == 2):
		tipo = int(raw_input("Select the type of account:\n(1)Savings account\n(2)Current account\n"))
		if(tipo > 0 and tipo < 3):
			if(tipo == 1):
				cajero = Ahorro()
				cajero.encender()
				cajero.validar_cuenta_ing()
				if(cajero.v == True):				
					operacion = int(raw_input("Select the operation to perform:\n(1)Remove\n(2)Change Password\n(3)Check balance\n"))
					if(operacion > 0 and operacion < 4):
						if(operacion == 1):
							cajero.retirar_ing()
						if(operacion == 2):
							cajero.cambiar_clave_ing()
						if(operacion == 3):
							cajero.consultar_saldo_ing()
					else:
						print "Failed to select an option"
		
			if(tipo == 2):
				cajero = Corriente()
				cajero.encender()
				cajero.validar_cuenta_ing()
				if(cajero.v == True):
					operacion = int(raw_input("Select the operation to perform:\n(1)Remove\n(2)Change Password\n(3)Check balance\n"))
					if(operacion > 0 and operacion < 4):
						if(operacion == 1):
							cajero.retirar_ing()
						if(operacion == 2):
							cajero.cambiar_clave_ing()
						if(operacion == 3):
							cajero.consultar_saldo_ing()
					else:
						print "Failed to select an option"
		
		else:
			print "Failed to select an option"
else:
	print "Failed to select the language"
print "Puede retirar su tarjeta"
cajero.apagar()
