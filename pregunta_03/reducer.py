#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list = []

for fila in sys.stdin:
  fila_separada = fila.split(",")
  list.append((fila_separada[0],fila_separada[1]))
  list.sort(key=lambda x: x[1])

for tuple in list:
  sys.stdout.write(tuple[0] + "," + str(tuple[1])) 