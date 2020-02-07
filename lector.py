#!/usr/bin/python3
import argparse

def leer_archivo( archivo ):
    #fh = open(archivo,"r") # r = reading: lectura 
    try:
      with open(archivo, "r") as fh:
        texto = fh.read() 
        lineas = texto.splitlines()  
        texto_limpio = " ".join(lineas) 
    except:
      texto_limpio=""
      
    return texto_limpio

def contar_palabras( texto ):
    palabras = texto.split(" ") 
    dp = dict() 
    for palabra in palabras: 
        p = palabra.strip(",.") 
        if p in dp: 
           dp[p]+= 1
        else: 
          dp[p] = 1 
    if "" in dp:
      del(dp[""])
    return dp
def imprime_diccionario( dp, minimo):
    lista = [ (k,v) for k,v in dp.items() if v >= minimo ]
    lista_ordenada = sorted(lista, key = lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
      print(tupla[0],"= ",tupla[1])
    return

def main( archivo ):
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    imprime_diccionario(dip,minimo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help=
"nombre de archivo", required=True)
    parser.add_argument('-m', '--minimo', dest='minimo', help=
"minimo de palabras repetidas", required=False, type=int)
    args = parser.parse_args()
    minimo= args.minimo
    archivo = args.archivo
    #./lector.py -a /tmp/episodio4.txt
    #archivo = "/tmp/episodio4.txt"
    main(archivo)
