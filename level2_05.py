## Ejercicio 5
frase_ejemplo = "Hola soy Alejandro Valle y soy de Valencia"



def contador(frase): 
    frase_lista = frase.split() # Dividimos la frase en un palabras y se crea una lista con ello
    frase_dict = {} # Creamos el diccionario vacío
    for i in frase_lista: # Iteramos sobre la lista
        if i in frase_dict: # Si la palabra sobre la que estamos iterando está ya en el diccionario, incrementamos con 1 su valor
            frase_dict[i]+=1
        else:
            frase_dict[i]=1 # Si la palabra sobre la que estamos iterando no está en el diccionario, la creamos con valor 1
    
    return frase_dict

print(contador(frase_ejemplo))


