#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    curkey = None
    total = 0

   
    for line in sys.stdin:

        key, val = line.strip().split("\t")
        sys.stdout.write("{},{}\n".format(val, key))
        