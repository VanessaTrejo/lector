#!/usr/bin/python3
import argparse
import lector
import os

def escribir_archivo(archivo,texto):
  '''recibe el nombre de un archivo a crear o midificar y recibe un texto a insertar en el archivo creado'''
  with open(archivo,"w", encoding="UTF-8") as fh:
    fh.write(texto)
  return

def main(folder, inicia, termina, salida):
    '''Ingresa el folder con la carpeta a buscar, despues por medio de un inicia y termina previamente ingresados, buscara todos los archivos que contengan esas especificaciones
     salida es el nombre del nuevo archivo a crea.
    '''
    listado_tmp = os.listdir(folder)
    listado_txt = [archivo for archivo in listado_tmp if archivo.endswith(termina)]
    listado_episodios = [archivo for archivo in listado_txt if archivo.startswith(inicia)]
    ''' un endwith y startswith para encontrar el principio y final de una palabra, se guardan los comunes en una lista'''
    lista = []
    for archivo in listado_episodios:
      texto = lector.leer_archivo(os.path.join(folder,archivo))
      lista.append(texto)
    '''se lee cada uno de los archivos con un for y llamando al lector.py y se agregan los archivos leidos a una lista'''
    textote = "\n".join(lista)
    escribir_archivo(salida, textote)
    '''se manda a llamar a escribir archivo'''
    
    

if __name__ == "__main__":
    '''Argumentos iniciales, se piden 4 por defecto'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--folder', dest='folder', help ="nombre de folder", required =True)
    parser.add_argument('-i', '--inicia', dest='inicia', help ="nombres de textos", required=True)
    parser.add_argument('-t', '--termina', dest='termina', help ="extencion del texto", required=True)
    parser.add_argument('-o', '--salida', dest='salida', help ="nombres de textos", required=True)
    args = parser.parse_args()
    folder = args.folder
    inicia = args.inicia
    termina = args.termina
    salida = args.salida
    main(folder, inicia, termina, salida)