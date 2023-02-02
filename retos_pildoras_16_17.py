#imprime numeros impares del 1 al 100 usando while

i=1
while i < 100:
    print(i, end=", ")
    i=i+2
    
#------------//------------------
#Contraseña mínimo 8 caracteres, sin espacio en blanco, permite máximo 3 intentos

import os
os.system("cls")
tryes=0

print("\n\t\t\t\t\tPROGRAMA QUE VALIDA CONTRASEÑA\n")
print("Contraseña mínimo 8 caracteres, sin espacio en blanco")
def validate_password(password):
    if len(password) < 8:
        return "La contraseña debe tener mas de 8 Caracteres"
    if ' ' in password:
        return "La contraseña no puede tener espacios en blanco"
    return None
 

while True and tryes<3:
    password = input("Digite la contraseña: ")
    error = validate_password(password)
   
    if error is None:
       
        break
    else:
        print(error)
        tryes=tryes+1
        
if tryes<3:
     print("Contraseña Valida")
else:
    print("Excedio el numero de intentos")
    
    
#----------------------------//---------------------------------

#valida que email tenga @, dominio y termine .com .net .org

def validate_email(email):
    if '@' not in email:
        return "Email debe tener '@'."
    if email.endswith('@.com') or email.endswith('@.net') or email.endswith('@.org'):
        return "Email debe terminar en ''dominio'.com', ''dominio'.net', or ''dominio'.org'."
    if email.endswith('.com') or email.endswith('.net') or email.endswith('.org'):
        return None
   
    return "Email debe terminar en '.com', '.net', or '.org'."

while True:
    email = input("Ingrese el email: ")
    error = validate_email(email)
    if error is None:
        print("Email es valido")
        break
    else:
        print(error)
        


#-------------------//----------------------

#pide números infinitamente. Los números introducidos deben ser cada vez mayores 
#El programa finalizará cuando se introduce un número menor que el anterior.

num1=int(input("Introduce un número: "))
num2=int(input(f"Introduce un número mayor que {num1} : "))
while num2>num1:
    num1=num2
    num2=int(input(f"Introduce un número mayor que {num1} : "))
print()
print(f"{num2} No es mayor que {num1}")

#-------------------//----------------------
#pide números positivos indefinidamente. 
# El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos

numero=int(input("Digite un número : "))
suma=0

while numero>0:
    suma=suma+numero
    numero=int(input("Digite un número : "))
    
print("La suma de los números positivos digitados es: ", suma)

    

