# Pedir el radio de un círculo y calcular su área. A=PI*r^2.

# radio_usuario= input("Dime el radio del circulo")
# radio_int = int(radio_usuario)
# pi= 3.14
# resultado=(pi*radio_int)**2
# print("El Resultado del area es {}".format(resultado))

# Pedir el radio de una circunferencia y calcular su longitud.

# pi_doble=3.14*2
# user_radio = input("introduce el radio de una circunferencia")
# radio_int= int(user_radio)
# resultado= radio_int * pi_doble
# print("la longitud de la circunferencia es {}".format(resultado))

# Pedir dos números y mostrar la suma.
# numero1= int(input("Introduce 1 numero\n"))
# numero2= int(input("Introduce otro numero\n"))

# resultado= numero1 + numero2
# print("El resultado de la suma es {}".format(resultado))

# Pedir 3 números y mostrar la multiplicación entre ambos (a*b*c)

# numero1= int(input("Introduce 1 numero\n"))
# numero2= int(input("Introduce otro numero\n"))
# numero3= int(input("Introduce un tercer numero\n"))

# resultado= numero1 *numero2 * numero3
# print("El resultado de la multiplicacion es {}".format(resultado))

# Pedir el nombre y la edad de una persona y mostrar: Juancito tiene 5 anios

# nombre= input("Introduce un usuario\n")
# edad=input("introduce una edad \n")

# print("{} tiene {} años".format(nombre,edad))


# 14.Diseña una aplicación que muestre las tablas de multiplicar del 1 al 10.


# for x in range(1,11):
#  table = [1,2,3,4,5,6,7,8,9,10]
#  for y in table:
#      result = x*y
#      print("{}x{} = {}".format(x,y,result))

# 15.Realizar un programa que nos pida un número n, y nos diga cuantos números hay
# entre 1 y n

# newNumber = int(input("Introduce un numero"))
# result = newNumber - 1
# print("Entre {} y 1 hay {} numeros".format( newNumber,result))


# 16.Realizar un programa que cuente la cantidad de números pares desde 1 hasta un
# número ingresado por el usuario.
# newNumber = int(input("Introduce un numero"))
# countNum = 0
# for x in range(1,newNumber+1):

#    if(x % 2 == 0 ):
#     countNum += 1
# print("El numero de pares es {}".format(countNum))

# 17.Realizar un programa que cuente la cantidad de números pares entre 2 ingresados
# por el usuario y además muestre la suma de dichos números pares.
# from functools import reduce


# newNumber1 = int(input("Introduce un numero"))
# newNumber2 = int(input("Introduce un numero"))
# numbers = []
# for x in range(newNumber1,newNumber2+1):
#     if x % 2 == 0:
#         numbers.append(x)
# totalSum = reduce(lambda x,y :x+y,numbers)
# print("El numero de pares es {} y la sumatoria es {}".format(len(numbers),totalSum))


# 18.Realizar un juego del ahorcado en Python. El juego es de a 2 personas. El verdugo y
# el ahorcado. Siempre serán palabras de 6 caracteres. En caso de ser menos, las
# ultimas letras serán guiones.


# 19.Pedir tres notas numérica entera entre 1 y 10, y mostrar dicha nota de la forma:
# uno, dos, tres...realizarlo con for e if


# 20.Realizar un programa que calcule todos los múltiplos de 3 entre 2 números
# ingresados por el usuario.


# newNumber1 = int(input("Introduce un numero"))
# newNumber1 = int(input("Introduce un numero"))
# newNumber2 = int(input("Introduce un numero"))
# totalCount = 0
# for x in range(newNumber1,newNumber2+1):
#     if x % 3 == 0:
#         totalCount += 1

# print("El numero de pares es {} ".format(totalCount))

# 21.Realizar un programa que sume los números ingresados por teclado mientras que el
# numero ingresado no sea un 0.


# countTotal = 0
# while True:
#     num = int(input("Introduce un numero"))
#     countTotal += num
#     if num == 0:
#         break
# print("El numero acumulado es {}".format(countTotal))

# 22.Realizar un programa que multiplique los números ingresados por teclado mientras
# que el número ingresado no sea un 0.


# countTotal = 0
# while True:
#     num = int(input("Introduce un numero"))
#     countTotal *= num
#     if num == 0:
#         break
# print("El numero acumulado es {}".format(countTotal))


# 23.Realizar una calculadora con menú. El menú contendrá las 4 operaciones básicas y
# una opción para salir. Al salir del programa se mostrara el resultado final del
# calculo.



# 24.Dibuja un cuadrado de n elementos de lado utilizando *.

# Objetos Numeros a Numeros Romanos y a la vez de Romanos a Numeros.

# class RomanoEnteroObj:
#     def __init__(self):
     
#      self.numero_dic =  { 1:"I",2:"II", 3:"III", 4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX", 10: "X"}
#      self.roman_dic =  { "I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10}
#     def Obten_Romano(self, letra):
        
#         print(self.roman_dic.get(letra))
    
#     def Obten_Entero(self,number):
        
        
#         print(self.numero_dic.get(number))
        
# test = RomanoEnteroObj()
# print(test.Obten_Entero(10))
# print(test.Obten_Romano('I'))

# import itertools 
  


  


# class SubConjObj():
#         def __init__(self):
#             self.subConjunto =[1,2,3,4,5]
        
#         def getSubconjunto(self):
#                 return list(itertools.combinations(self.subConjunto, 2)) 
        
# test = SubConjObj()
# print(test.getSubconjunto())
      



# class Inv():
#      def __init__(self,cadena):
#          self.cadena = cadena
     
#      def voltear_cadena(self):
#          res = self.cadena.split()
#          tt =reversed(res)
#          print(' '.join(tt))
         
       
# test = Inv("Esta es mi cadena")
# print(test.voltear_cadena())


# class Triangule():
#      def __init__(self,base,altura):
#          self.base = base
#          self.altura = altura
     
#      def Area(self):
#        print(f'El area de un triangulo es {(self.base * self.altura) / 2}')
         
       
# test = Triangule(4,5)
# print(test.Area())




# class Circulo():
#      def __init__(self,radio):
#          self.valorPi  =3.14
#          self.radio= radio
     
#      def Area(self):
#         resultado=(self.valorPi * int(self.radio))**2
#         print('El area de un circulo es {}'.format(resultado))
#      def Perimetro(self):
#          resultado = (self.valorPi * (self.radio*2)) 
#          print('El perimetor del circulo es {}'.format(resultado))  
       
# test = Circulo(10)
# print(test.Area())
# print(test.Perimetro())

