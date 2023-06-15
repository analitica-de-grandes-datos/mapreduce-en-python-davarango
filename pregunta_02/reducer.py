#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    max = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
           
            if val > max:
                max = val
        else:
           
            if curkey is not None:
               
                sys.stdout.write("{}\t{}\n".format(curkey, max))

            curkey = key
            max = val

    sys.stdout.write("{}\t{}\n".format(curkey, max))
    