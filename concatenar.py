
   # python3 concatenar.py -a [path archivo a concatenar] -a [url archivo a concatenar] -a [n archivo a concatenar] -o [archivo nuevo condocuemntos #concatenados]

import argparse
import lector
import ejemplo

def escribir_archivo(archivo,texto):
    with open(archivo,"w") as fh:
         fh.write(texto)
    return                 

listado=[]


def main(archivos,output):
    for archivo in archivos:
        print(archivo)
        texto = lector.leer_archivo(archivo)
        listado.append(texto)
    textote = " " .join(listado)
    escribir_archivo(output,textote)
   

if __name__ == "__main__": 
     parser = argparse.ArgumentParser()
     parser.add_argument('-a', '--archivo', dest='archivos', help="nombres de archivos", action="append", required=True)
     parser.add_argument('-o', '--output', dest='output', help="archivo de salida", required=True)
     #parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
     args = parser.parse_args()
     archivos = args.archivos
     output = args.output
     main(archivos,output)        