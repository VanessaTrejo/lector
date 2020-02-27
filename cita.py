#!/usr/bin/python3
import lector
import contar_palabras
import argparse



def obtenCita(texto,inicio,conteo):
  lista=texto.split(" ")
  longitud=len(lista)
  if((inicio+conteo)<longitud):
    lista_palabras=lista[inicio:inicio+conteo]
    cita=" ".join(lista_palabras)
  else:
    cita=""
  return cita


def main(archivo,inicio,conteo, archivo_stopwords):
  texto=lector.leer_archivo(archivo)
  cita=obtenCita(texto,inicio,conteo)
  print("cita: ", cita)
  stopwords = lector.leer_stopwords(archivo_stopwords)
  contar_palabras.main(cita,stopwords)

if __name__ == "__main__":
  parser= argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo',help="nombre de archivo",required=True)
  parser.add_argument('-s', '--stopword', dest='stopword',help='archivo txt de stopwords', required=True)
  parser.add_argument('-i', '--inicio', dest='inicio',help='inicio del rango', required=True, type= int)
  parser.add_argument('-f', '--fin', dest='fin',help='final del rango', required=True, type= int)
  args= parser.parse_args()
  archivo = args.archivo
  stopwords = args.stopword
  inicio = args.inicio
  cuenta = args.fin
  main(archivo,stopwords,inicio, cuenta)
    

  
