#!/usr/bin/python3
   # python3 concatenar.py -a [path archivo a concatenar] -a [url archivo a concatenar] -a [n archivo a concatenar] -o [archivo nuevo condocuemntos #concatenados]

import argparse
import lector

def main(archivo,output):
    guarda = []
    files = open(output, "w")
    for nombre in archivo:
        lee = lector.leer_archivo(nombre)
        guarda.append(lee)
    for caso in guarda:
        files.write(caso)
    files.close()
    concatenado = lector.leer_archivo(output)
    print(concatenado)
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo', action="append", required=True)
  parser.add_argument('-o','--output',dest='output',help='salida de archivo', required=True)
  args=parser.parse_args()
  archivo=args.archivo
  output=args.output
  main(archivo,output)
  #Grabar archivo python text file tf8     