from itertools import count
from operator import le
from pickle import TRUE
from typing import ClassVar

#Dayana Mirle Quintana Moreira
a= int(input("numeros " ))
a1=a+2
a=2*(189-45)
b= a*2
a=a-100
print(a,a1,b)
#4 video
X=46
X=15
x=30
print(x)

x=10-2
x-=5
print(x)

x=10-2
10+2 #no gurada en ninguna variable

y=3 *(4+2)
x=y+2
z=5
x=y-z
print(x)

x=25
x+10 #el resultado seria 35 pero el resultado no esta almacenado en ninguna variable

x=3
y=x+6
x=y-1
print(x)

#video 4

x=150
print(type(X))

x=13.5
print(type(x))

x="hola"
print(type(x))

x= False
print(type(x))

x= True
print(type(x))

x=46
x=1+x
print(int(x))


a="15.25"

print(float(a))

a=10
b=4

suma=a+b
div=b/a
mod=b%a

print(suma)
print(div)
print(mod)

a1=16789
b1=10

mod1=a1&b1

print(mod1)

c1=5
c2=2

di=c1/c2
m=c1%c2
print(m)
print(di)
s=2
c=2
a=4
e=6
modu1=s%c
modu2=a%s
modu3=e%s

print(mod1)
print(modu2)
print(modu3)


A="buen"+"dia"
print(A)

B="dayana"
C="quintana"
ca=B + " " + C
print(ca)
print(ca,len(ca),ca[0])
print(ca[len(ca)-1])

ac=4
bc=10
S=ac<bc
print(S)

ac1="hola"
ac2="adios"

ac3=ac1 == ac2
print(ac3)


ac4=5
ac5=5

ac6=ac4<ac5
print(ac6)


ca="casa"
co="cosa"
re=ca<co

print(re)

ed=20

re=ed>18
print(re)

#video 6

a6=100
b6=5
c6= 100/5

print(float(c6))

s6=7
d6=2

f=7/2
d=7//2
r=7%2
print(float(f))
print(int(d))
print(int(r))

q6="a"
print(type(q6))

A6="tiza"
N6="."

RET=A6+""+N6

print(RET,type(RET))

w6= "hola"
print(len(w6))
print(type(w6))

t="145"
print(int(t))

t1="145"
print(float(t1))

t3=145
print(float(t3))

r="32"
print(str(r))
print(type(r))

y6=1
y7=2

y=1+2!=3
print(y)

o=177
p=2
w=177%2==0
print(w)

m1="nube"
print(m1)
print(len(m1)<=20)

#las variables luego de cada operacion

n=167
k=10
n1=167/10
n2=167//10
n3=167%10

print(n1)
print(n2)
print(n3)

letra="a"
saludo="hola"+ letra
c=saludo[0]
c1=saludo[1+3]
l=len(saludo)
c2=saludo[len(saludo)-1]
print(saludo,letra,type(letra))
print(c,c1,c2)
print(l)

a0="a"
b0="b"
c0=a0<b0
print(c0)

d=1
d1=1!=1
print(d1)

d5="cinta"
d6="canto"

d4=d5>=d6
print(d4)

a12="z"
a13="a"
a14="paz"
c="z"+"a"+"paz"[0]
x=c[0]=="z"
print(c)
print(x)

#operaciones arrojan error

a=11-(4%2+10)
print(a)

#a="30"+2 error ya que el 30 es string y el 2 es int
#print(a)

a="30"+"2" # esta bien ya que los 2 son string

print(a)

#a="h o l a"[len("hola")] error ya que hola tiene 3 posiciones, la posiciones 4 no existe
#   0 1 2 3

#a=len(1234) len es una operacion para string

b="hola"[len("fin")]
print(b)

b1="hola"[11-(4%2+10)]
print(b1)

b2=int ("4")
print(b2)

b3=int(4)
print(b3)

#a=int("z") error ya que int solo permite numero enteros

#a=int("4.") error ya que esta en string

#4<("F") error ya que el signo menor no soporta un datos entero y el otro string

#"palabra"="raama"error error ya que "palabra"no es una variable para guardar

b5="palabra"=="rama"
print(b5)

#video 7

edad=16

if edad>10 and edad<20:
    print("true")
else:
    print("false")

edad=16

if edad>20 and edad<30:
    print("true")
else:
    print("false")

edad=16

if edad>20 or edad<30:
    print("true")
else:
    print("false")

es_cliente=True
print(type(es_cliente))

if es_cliente and edad>18:
    print("true")

else:
    print("false")

print()


#video 8
a=not True
print(a)

a=not(1+2!=3)
print(a)

x=(len("jugar")>5) and (len("jugar")<10)
print(x)

a="alto" [2]=="t" and X
print(x)

a=542913%10!=3 and len("cafe")==3
print(a)

a=a0!=0 or "a"< "y"
print(a)

a= True or int ("50")>=50
print(a)

edad=20
if not (x) or edad%2==0:
    print("True")

else:
    print("False")

es_cli=False
not (es_cli and not (edad<18))
print(es_cli)

#ejercicio 1

n=50

if n>=0 and n<=100:
        print("correcto")

else:
        print("incorrecto")
#
#
#

#ejercicio 2
edad=16

if edad>10 and edad<20:
    print("true")
else:
    print("false")


a=len("naguara")
print("tiene una longitud ",a)

#expresar las siguientes operaciones

n=4
if n%4==0 and n>0:
    print("correcto")

else:
    print("esta mal")

#EL numero es multiplo de 4 y tambien es negativo
#Resouesta: numero %4 == 0 and numero < 0


#Decidiste comprar un auto usado, pero debe cumplir ciertas condiciones: 
# EL kilometraje debe ser menor a 30000 y el modelo debe estar entre 2015 y 2017
#Respuesta: km<30000 and (modelo>=2015 and modelo<=2017)


#Una agrupacion academica tiene ciertos requisitos para cualquier estudiante que
#desea ingresar:
#Debe tener màs de 30% de sus estudios completos y no debe ser miembro de otra
#agrupacion academica en la misma universidad. 
#Respuesta: porcentaje_completo > 30 and not (miembro_agrupacion)


#Una persona pasa frio si es invierno y ademas no tiene calefacciòn ni esta abrigada
#respuesta: es_invierno and not tiene_calefacciòn and not esta_abrigada
# es_invierno and not(tiene_calefaccion or esta_abrigada)



#video 9

cadena="programacion en python"
print(cadena[6])

print(len(cadena))

print(cadena[21])

i=len(cadena)-1
print(i)

print(cadena[len(cadena)-1])
print(cadena[0:10])
print (cadena[10:])
print(cadena[:10])
print(cadena[:13])
print(cadena[:13:2])
print(cadena[::2])
print(cadena[::-1])
print(cadena[-1:])
print(cadena.find("python"))
print(cadena.find("p"))
print(cadena.find("z"))
print(cadena.find("z")==-1)
a="python" in cadena
print(a)

precio="40"
print(int(precio))
print(type(int(precio)))
print(cadena.upper())
print(cadena.lower())
print(cadena)
print("6709".upper())
print(cadena.title())
print(cadena.capitalize())
a="       hola"
print(a.strip())

a="       hola       chao"
print(a.strip())
print(cadena)
print(cadena.count("p"))
print(cadena.count("o"))
print(cadena.replace("python","*****"))
print(cadena.replace("a","_"))
print(cadena.replace("z","i"))

print(cadena.replace("o","-"))

#video 10

cade="si, profe, es cierto... yo me comi la tarea"
print(cade[10])
print(cade[-1])
print(cade[0:9])
print(cade[::3])
print(cade[::-1])
print(cade[4:9])

s="  hola, ¿como estas?"
print(s[::-1])
print(s[len(s)-1])
print(s.count("o"))
print(s.count("hola"))
print(s[-4:])
print(s[15:])
print(s.find("o"))
print(s.strip())
x=s.upper()
if x==s:
    print("True")
else:
    print("false")


print(x)
print(s)
print(s[14:].upper())
print(len(s)%2 !=0)
print(len(s)) 
print(s.replace(" ", "*"))


x="programar en python"
print(x[-1])
print(x[len(x)-1])
cadena1="hola"
print(cadena1.find("2"))
b="a"in "datiles"
print(b)

b1="me gusta programar".find(" ")
print(b1)

b1="me gusta programar".count(" ")
print(b1)

nueva="c"+cadena[1:]
print(nueva)
print(x)

x="hoy es miercoles"
print(x.replace("i","i"))

print(x)

print(x.replace("i","i").replace("e","e"))
print(x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u"))

#video 11

print(45)
a=input("ingrese su edad : ")
print(type(a))

a=int(input("ingrese su edad : "))
print(a)

#video12
a=input("nombre de la cancion favorita : ")
b=int(input("ingrese su edad : "))

print("su cancion favorita es {} y su edad {}".format(a,b))
print(type(a))

precio=float(input("ingrese el precio : "))
total=precio+(precio*0.10)
print("su precio es {}".format(total))

edad=int(input("ingrese su edad : "))
print("su edad es {}".format(edad))

if edad==18:
    print("si es igual a {}".format(edad))

else:
    print("no es igual a 18 , su edad es  {}".format(edad))

n=input(("ingrese su nombre : "))
b=n
print("ahora estas en la matrix ",b)

costo=float(input("ingrese el valor a pagar : "))

valor=costo*0.062
propina=valor*0.1

print("el valor a pagar es {:.2f} y de propina es {:.2f}".format(valor,propina))


dia=int(input("ingrese dia de su nacimiento : "))
mes=(input("ingrese el mes de su nacimiento : "))
anio=int(input("ingrese el año de su nacimiento : "))

print("dia de nacimiento es {} , mes {} y su año {}".format(dia,mes,anio))

fecha=int(input("ingrese su fecha de nacimiento DDMMAAAA : "))

año=fecha%10000
dia=fecha//1000000
mes=(fecha//10000)%100

print("el año es {}, su dia es {} y su mes es {}".format(año,dia,mes))

fecha=input("ingrese su fecha de nacimiento DD//MM//AAAA : ")

dia=fecha[:2]
mes=fecha[2:4]
año=fecha[4:]

print("el año es {}, su dia es {} y su mes es {}".format(dia,mes,año))

capacidad=float(input("capacidad de tanque : "))

km=float(input("km por litro : "))
recorrido=float(input("km totales a recorrer : "))

km_tanque=capacidad*km

print("tanques de conbustible necesario seran {:.2f}".format(km_tanque))

#video 13

capacidad=4
entradas=0.2
porcentaje=0.3
comunes=0.7

dimensiones=float(input("dimensiones del estadio : "))
entradas=int(input("cantidad de personas : "))
escenario=int(input("porcentaje ocupado : "))

gradas=dimensiones*entradas

esce_1=dimensiones*(escenario/100)
disponible=dimensiones-gradas-escenario
total=(disponible*4)+entradas

print("caben {} de personas".format(total))

precio_entrada=float(input("precio de entrada : "))
entra_comun=float(input("entrada comun : "))
print("total de ventas ",(total*porcentaje)*precio_entrada+(total*comunes)*entra_comun)




#video 24
#ejercicio 1
can=0
n=int(input("ingrese un valor : "))

while n!=0:
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
            break
    if primo:
        can=can+1
    n=int(input("ingrese de nuevo : "))

print("primos",can)        

#ejercicio 2

año_ini=int(input("ingrese el año : "))
año_fin=int(input("año final : "))

for año in range (año_ini,año_fin):
    if not año%10==0:
        continue
    if not año%4==0:
        continue
    if año%100!=0 or año%400==0:
        print(año)

#video 25

#video 26

def validar(email):
    carac_bus="@"
    email_va=False
    for c in email:
        if c== carac_bus:
            email_va=True
            break
    return email_va
direccion=input("tu email : ")
if validar(direccion):
    print("direccion valida")
else:
    print("direccion ivalida")
#2
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

#!programa principal
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))

#3
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.
def sumaDigitos(numero):
  suma=0
  while numero!=0:
    digito=numero%10
    suma=suma+digito
    numero=numero//10
  return suma

#!programa principal
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))

#4
# Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

#!programa principal
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")

#5
# Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

#!programa principal
num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))

#6 
# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

#!programa principal
cantidad=0
num=int(input("Número (-1 para cortar): "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")

#7 
# Escribir un programa que pida números positivos al usuario. 
# Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números 
# cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)

#8 
# Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. 
# También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))

#9
# Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:

def coordenadaZ(x,y):
  x=x+10
  y=y+15
  return x+y

#!programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)

#10
# El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. 
# ¿Qué hay que corregir?

def maximo(a,b):
  if x>y:
    return x
  else:
    return y

def minimo(a,b):
  if x<y:
    return x
  else:
    return y

#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

#11 
# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8
#12 
# Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.

def lenUltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad

#13 
# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, 
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío
# Precondición: el formato del nombre de los socios será: nombre apellido. 
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. 
# Si un socio tuviera más de un apellido, el usuario sólo ingresará uno. 
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. 
# En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, 
# la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258

def lenUltimaPalabra(cadena):
   longitud=len(cadena)
   if longitud==0:
       return 0
   cantidad=0
   for i in range(longitud):
       if cadena[i]!=' ':
           cantidad+=1
       else:
           if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
               cantidad=0
   return cantidad

def DNIvalido(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8

def primerosTresDigitos(numero):
   while numero >= 1000:
     numero = numero // 10
   return numero

def obtenerIdentificador(nombre, dni):
   nombre=nombre.strip()
   id=nombre[:nombre.find(" ")]
   id=id+str(lenUltimaPalabra(nombre))
   id=id+str(primerosTresDigitos(dni))
   return id

#programa principal
nombre=input("Nombre del socio: ")
while nombre!="":
   dni=int(input("DNI del socio: "))
   while (DNIvalido(dni)):
      print("Número inválido.")
      dni=int(input("DNI del socio: "))
   print(obtenerIdentificador(nombre,dni))
   nombre=input("Nombre del socio: ")
  
#14 
# Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo 
# la primera letra de cada palabra a mayúscula y las demás letras a minúscula, 
# dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ". 
# Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor 
# esperado ante distintos argumentos.

def titulo(cadena):
    '''
    Recibe una cadena de caracteres y retorna una copia que tiene la
    primera letra de cada palabra en mayúsculas y el resto de las letras
    en minúsculas.
    >>> titulo('esto es una frase')
    'Esto Es Una Frase'
    >>> titulo('ESTO ES UNA FRASE')
    'Esto Es Una Frase'
    >>> titulo('palabra')
    'Palabra'
    >>> titulo('   esto es una frase')
    '   Esto Es Una Frase'
    >>> titulo('esto es una frase   ')
    'Esto Es Una Frase   '
    >>> titulo('esto   es   una   frase')
    'Esto   Es   Una   Frase'
    >>> titulo('')
    ''
    >>> titulo(' ')
    ' '
    >>> titulo('123')
    '123'
    >>> titulo('-1esto 2es 3una 4frase')
    '-1Esto 2Es 3Una 4Frase'
    >>> titulo('esto1 es2 una3 frase4---')
    'Esto1 Es2 Una3 Frase4---'
    '''
    nueva=""
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva

#11 Ejercicios para practicar programación usando estructuras de datos, con Python.

#1
# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
#  Finalizar al ingresar el número 0, el cual no debe guardarse.
# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
# cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
# Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#A
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#B
print("Sumatoria de los números:", sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#C
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")

#2 
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
# con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), 
# ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, 
# "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
# Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), 
# ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# -Agregar pasajeros a la lista de viajeros.
# -Agregar ciudades a la lista de ciudades.
# -Dado el DNI de un pasajero, ver a qué ciudad viaja.
# -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# -Dado el DNI de un pasajero, ver a qué país viaja.
# -Dado un país, mostrar cuántos pasajeros viajan a ese país.
# -Salir del programa.

def agregarPasajeros(pasajeros):
    nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

#programa principal
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")

#3
# Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
# finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, 
# finalizando al ingresar “x”.
# - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
# - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# -Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def cargarNombres(alumnos):
   nombre=input("Nombre: ")
   while nombre!="x":
       alumnos.add(nombre)
       nombre=input("Nombre: ")
   return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)

#4
# Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
# la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). 
# Ejemplo:[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), 
# ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
# ("Jorge Russo", 15, 958, "Mirasol 218")]
# Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente 
# y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
# Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función 
# debe retornar una estructura que contenga cada domicilio una sola vez.

def direcciones(ventas):
   domicilios=set()
   for venta in ventas:
       domicilios.add(venta[3])
   return domicilios

#5
# Escribir un programa que procese strings ingresados por el usuario. 
# La lectura finaliza cuando se hayan procesado 50 strings. 
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
# Ejemplo: "r":5, "%":3, "a":8, "9":1.
# ¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
# incluyendo el valor 0 para las letras que no aparecieron?

contadores={}
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter not in contadores:
           contadores[caracter]=1
       else:
           contadores[caracter]+=1
print("Frecuencia de cada carácter")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
print("Frecuencia de cada letra")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#6
# Crear un programa para gestionar datos de los socios de un club, permitiendo:
# -Cargar información de los socios en un diccionario para acceder por número de socio. 
# Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). 
# El programa debe iniciar con los datos de los socios fundadores ya cargados:
# Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
# Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
# Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
# -Informar cantidad de socios del club.
# -Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
# -Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, 
# para indicar que en realidad ingresaron el 14/03/2018.
# -Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
# -Imprimir el listado de socios completo.

def cargarSocios(socios):
   numero=int(input("Número de socio (0 para cortar): "))
   while numero!=0:
       nombre=input("Nombre y apellido: ")
       fecha=input("Fecha de ingreso (DDMMAAAA): ")
       cuota=input("¿Cuota al día? s/n: ")
       socios[numero]=[nombre,fecha,cuota.lower()=="s"]
       numero=int(input("Número de socio (0 para cortar): "))
   return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
   for numero,datos in socios.items():
       print("-Número:",numero)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formatoFecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

imprimirListado(socios_activos)

#14 Ejercicios para practicar programación usando estructuras de datos, con Python.

#1 

lista=[1, 2, 3, 4]
for elemento in lista:
  print(elemento)
articulos={ 154:["jabon en polvo", "limpieza", True],
            248: ["talco", "cosmetica", False],
            199: ["cera para pisos","limpieza", True] }
for clave, valor in articulos.items():
  print("Codigo: ", clave)
  print("Descripcion: ", valor[0])
  print("Rubro; ", valor[1])
  if valor[2]:
    print("Hay stock")
  else:
    print("Agotado")
  print("-------------")

#2

lista =[1, 2, 3, 4, 4, 6, 7, 7, 8, 0, 9, 9, 9]

for i in range(len(lista)-1):
  if lista[i]==lista[i+1]:
    print(lista[i])

#3
 
def empleadoExiste(empleados, nombre):
  for datos in empleados.values():
    if datos[0]==nombre:
      return True
  return False

empleados= {100: ["BYRON QUINTANA", "Administracion"],
200:["Oriana López", "Gerencia"],
300:["Guadalupe Ríos", "RR.HH"],
400:["Lionel Campos", "Ventas"]}

nombre = input("Nombre de empleados: ")
if not empleadoExiste(empleados,nombre):
  print("El empleado no se encuentra en la nómina")

#4

alumnos= {"121-5": 42752983,
"243-9":  39234110,
"113-8:": 44922182,
"324-1": 39110245 }

legajo= input("Legajo a buscar: ")
if legajo in alumnos.keys():
  print("El DNI es: ", alumnos[legajo])

#5

def cargarDatos(diccionario):
  dni = int(input("DNI: "))
  while dni != 0:
    nombre = input("Nombre:" )
    domicilio = input("Domicilio:" )
    telefono = int(input("Telefono: " ))
    diccionario[dni]=[nombre, domicilio, telefono]
    dni= int(input("DNI: "))
  return diccionario

def imprimirDatos (diccionario):
  for clave, valor in diccionario.items():
    print ("-DNI:",clave, "-Nombre:", valor[0], "-Domicilio:", valor[1], "-Telefono:", valor[2])

clientes= { 44299132:["Gastón Quinteros", "Los Tilios 412", 582119721],
          38110223:["Valeria Gimenez", "Almendros 192",59912834],
          27918006:["Diego Linares", "Las Fresias 881", 51288390] }
clientes= cargarDatos(clientes)
imprimirDatos(clientes)

#6

def cargarMercaderias(mercaderias):
  articulo=[]
  codigo= int(input("codigo: "))
  while codigo !=0:
    descripcion=input("Descripcion: ")
    articulo.append(descripcion)
    rubro=input("Rubro: ")
    articulo.append(rubro)
    mercaderias[codigo]=articulo
    codigo=int(input("codigo: "))
  return mercaderias

productos={}
productos=cargarMercaderias(productos)
for codigo, datos in productos.items():
  print(codigo, "-Descripcion: ", datos[0], "-Rubro", datos[1])

#7

a=[1, 2, 3, 4]
for i in range(len(a)):
  if i==2:
    del a[3]
  print(a[i])

#8

b={"a": [1, 2, 3], "b": [], "c": [8,6], "d": [], "e": [4]}
for clave in b.keys():
  if b[clave]==[]:
    del b[clave]
    