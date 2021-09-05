#ejercicios de funciones
#%%
#ejercicio 2  
def cadena(nombre):
    print("hola "+nombre)
    return 
cadena(input("ingrese un nombre "))

#%%
#ejercicio 3
def factorial (n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value
print(factorial(3))  
print(factorial(20))
#%%
#ejercicio 5

def CA():
    radio = int(input("ingrese radio: "))
    pi = 3.1415
    return pi * (radio*radio)
  
area = CA()
    
def CV(area):
    al = int(input("altura del cilindro: "))
    return area * al

print(CV(area))


#%%

def media():
    lista = (2,4,6,8,12)

    return sum(lista)/len(lista)

  

print(media())


#%% #Ejercicios de condicionales
#ejercicio 2

password="POO"
contraseña=input("introduzca contraseña :")

if (contraseña.lower()==password.lower()):
        print("contraseña coincide")
        
else:
            print ("la contraseña no coincide")
            
            
#%%
#ejercicio 10
Veg=['Pimiento','Tofu']
NoVeg=['Peperoni','Salmón','Jamón']

while True:
    tipo_de_pizza=input("ingrese una opción (Vegetariana: ,","o",",No Vegetariana: )")
    
    if tipo_de_pizza.lower()=="Vegetariana".lower():
                  print(Veg)
                  break
    if tipo_de_pizza.lower()=="No vegetariana".lower():
                  print(NoVeg)
                  break
    else:         print("opcion inválida")
    
#%% #Ejercicios de listas.
# ejercico 4 numeros de loteria primitiva 
ganadores = []

for i in range(8):
        ganadores.append(int(input("Introduce un número ganador: ")))
        ganadores.sort()
print("Los números ganadores son " + str(ganadores))

# ejercicio 8 alfabeto 

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfa), 1, -1):
    if i % 3 == 0:
        alfa.pop(i-1)
print(alfa)

#%%
# ejercicio 8 

palabra = input("Introduce una palabra: ")
palabraReves = palabra
palabra = list(palabra)
palabraReves = list(palabraReves)
palabraReves.reverse()
if palabra == palabraReves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")  
    
#%% ejercico 13

A = input("Introduce una muestra de números separados por comas: ")
A = A.split(',')
n = len(A)
for i in range(n):
    A[i] = int(A[i])
A = tuple(A)
sum = 0
sumsq = 0
for i in A:
    sum += i
    sumsq += i**2
pro = sum/n
des = (sumsq/n-pro**2)**(1/2)
print('La media es', pro, ', y la desviación típica es', des)  

#%% ejercicios de diccionarios

#ejercico 1 monedas

divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
if divisa.title() in divisa:
    print(divisa[divisa.title()])
else:
    print("La divisa no está.")
    
    
#%% #ejercicio 3 frutas  
    
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))

if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")    
