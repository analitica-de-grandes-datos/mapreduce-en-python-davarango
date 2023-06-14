#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for row a in sys.stdin:
  fila_separada=row.split(",")
  sys.stdout.write(fila_separada[3]+","+fila_separada[4]+ "\n")