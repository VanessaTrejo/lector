#! /usr/bin/python3

import argparse
import lector

def leer_archivo(path):
                       
    try: 
        with open(path, "r") as fh:
            texto = fh.read()
            lineas = texto.splitlines()
            texto_limpio = " ".join(lineas)
    except:
        texto_limpio=""
    return texto_limpio


def contar(archivo,stopwords_url):
    texto = lector.leer_archivo(archivo)
    #dicc = dict()                       # se crea un diccionario para facilitar el contar
    #dicc2 = dict()
    lista_palabras = texto.split(" ")
    total = lista_palabras
    stopwords = lector.leer_stopwords(stopwords_url)
    #palabras_clave = texto.split(" ")
    dpc = dict() #dicc.palabras clave
    dps = dict() #dicc.palabras stopwords
    
    for palabra in lista_palabras:
        # ignoraremos los puntos y comas de las palabras
        p = palabra.lower().strip(",.")
        if p in stopwords:                   #es stopwords?
           if p in dps:                      #ya existe?
              dps[p] += 1                    #agregamos 1
           else:                             # si no, se creara
              dps[p] = 1                     #inicial con 1  
        else:
           if p in dpc:                       #ya existe?
              dpc[p] += 1                    #agregamos 1
           else:
              dpc[p] = 1                     #creamos con 1   
  
  
    print(len(dps),"Palabras stropwords") #imprime el numero de stopwords
    print(len(dpc),"Palabras clave") #imprime las palabras clave
    print(len(total),"Palabras totales") #escribe las palabras totales en el archivo         
    return total
 
 
def main(archivo,minimo,archivo_stopwords):
    texto = leer_archivo(archivo)
    texto = contar(archivo, archivo_stopwords)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)  
    parser.add_argument('-m', '--minimo', dest='minimo', default = 3, help="minimo de palabras repetidas", type = int, required=False)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="nombre de archivo",default = "stopwords.txt", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    stopwords = args.stopwords
    main(archivo, minimo, stopwords)  