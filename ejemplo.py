#usr/bin/python3
#ejemplo.py programa que usa varios argumentos en la misma opcion 


import argparse

def main(nombres):
  for nombre in nombres:
    print (nombre)
    

if__name__= "__main__":
  parser= argparse.ArgumentParser()
  parser.add_argument('-n', -'nombre', dest='nombre', help= 'nombres de personas', action= 'repeat', required=True)
  args= parser.parse_args()
  nombres= args.nombres
  main(nombres)