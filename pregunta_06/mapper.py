#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        columns = line.split('   ')
        
        sys.stdout.write("{}\t{}".format(columns[0],columns[2]))