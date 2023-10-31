"""
modulo de lectura de palabra aleatoria
desde fichero texto
"""
import random

def lectura():
    try:
        lista_palabras=[]
        with open('File_palabras.txt','r') as file :
            lista_palabras=file.readlines()
            
        return lista_palabras[random.randint(0, len(lista_palabras)-1)]

    except Exception as err :
        return(err)

