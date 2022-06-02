
#Primer ejercicio:
a=5
if (a>0):
    print(a,"Es un real positivo")
elif (a<0):
    print (a, "Es un real negativo")
else:
    print("El numero es igual a cero")


#Segundo ejercicio: 
d=5+3j
b= True
if (type(d)==type(b)):
    print("los tipos son iguales")
else:
    print("los tipos son diferentes")    

#Tercer ejercicio:
for i in range (1,21):
     if i%2 ==0:
         print("El numero", i,"Es par")
     else:
         print("El numero", i,"Es impar")


#Cuarto ejercicio:
for i in range (1,6):
 print(i**3)
