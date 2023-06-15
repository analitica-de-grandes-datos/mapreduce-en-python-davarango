#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    curkey = None
    data = []

    for line in sys.stdin:

        line = line.strip()

        key, val = line.split("\t")
        val = int(val)
   

        if key == curkey:
        
            data.append(val)
           
        else:
       
            if curkey is not None:
        
                data = sorted(data)
                sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in data)))
                data = []

            curkey = key
            data.append(val)
    data = sorted(data)
    sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in data)))