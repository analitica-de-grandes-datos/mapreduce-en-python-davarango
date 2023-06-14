#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dictionary = {}

for row in sys.stdin:
    fila_separada=row.split(",")
    if   fila_separada[0] in dictionary.keys():
        if dictionary[fila_separada[0]] < int(fila_separada[1]):
            dictionary[fila_separada[0]] = int(fila_separada[1])
    else:
        dictionary[fila_separada[0]] = int(fila_separada[1])

for key in dictionary.keys():
  key_edit=key.strip()
  string_valor=str(dictionary[key])
  print(key_edit  + "\t" + string_valor)