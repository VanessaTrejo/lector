#! /usr/bin/python3
import argparse
import random


def leer_archivo(path):
                      
    # fh = open(path, "r")
    try: 
        with open(path, "r") as fh:
            texto = fh.read()
            lineas = texto.splitlines()
            texto_limpio = " ".join(lineas)
    except:
        texto_limpio=""
    return texto_limpio



def contar_palabras(texto):
    dicc = dict()                       # se crea un diccionario para facilitar el contar
    # indicamos que cada palabra se diferencia por un espacio " "
    lista_palabras = texto.split(" ")

    for palabra in lista_palabras:
        # ignoraremos los puntos y comas de las palabras
        p = palabra.strip(",.")
        if p in dicc:                   # si existe la palabra, se le sumara
            dicc[p] += 1
        else:                           # si no, se creara
            dicc[p] = 1    
        
    if "" in dicc:
        del(dicc[""])            
    return dicc


 #recibe en stopwords: una cadena de las stopwords
 #recibe en texto: una cadena del texto a limpiar
 #regresa el texto limpio 
def eliminar_stopwords(dp, stopwords): 

    diccionario = {} 

    for (k,v) in dp.items(): 

        if k not in stopwords: 

           diccionario[k] = v 

    return diccionario 
    
def leer_stopwords(archivo): 

    try: 

        with open(archivo,"r") as fh: 

             lineas = fh.readlines() 

             lista  = [p.strip("\n") for p in lineas] 

             set_sw = set(lista) 

    except: 

        set_sw = set() 

    return set_sw     


def imprime_diccionario(dicc, numero):
    #   Crea e imprime un diccionario
    
    
    lista = [(k, v) for k, v in dicc.items() if v >= numero]
    lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0], " = ", tupla[1])
        print(random.choice(lista))
    return


def main(path, numero, stopwords):
    
    texto = leer_archivo(path)
    stopwords = leer_archivo(stopwords)
    #texto = eliminar_stopwords(texto,stopwords)
    dicc = contar_palabras(texto)
    texto = eliminar_stopwords(dicc,stopwords) 
    imprime_diccionario(dicc, numero)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="nombre de archivo",default = "spanish_stopwords.txt", required=False)
    parser.add_argument('-n', '--numero', dest='numero', default = 3, help="numero de palabras", type = int, required=False)
    args = parser.parse_args()
    archivo = args.archivo
    numero = args.numero
    stopwords = args.stopwords
    main(archivo, numero, stopwords)
