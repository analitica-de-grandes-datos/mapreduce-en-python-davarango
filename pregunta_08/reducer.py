#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    sum = 0
    count = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            sum += val
            count += 1

        else:
       
            if curkey is not None:
  
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, sum/count))

            curkey = key
            sum = val
            count = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, sum/count))