#This is a test code program
import sys


def main():
    """
    if len(sys.argv) != 3:
        print 'usage: .\wordcount.py {--count | --topcount} file'
        sys.exit(1)

        option = sys.argv[1]
        filename = sys.argv[2]
        if option == '--count':
            print_words(filename)
        elif option == '--topcount':
            print_top(filename)
        else:
            print 'unknown option' + option
            sys.exit(1)
"""
    ### Reading the file
    filename = 'alice.txt'
    f = open(filename, 'rU')
    lines = f.readlines()
    linesclean = []
    #for i in lines:
    lines = lines.


    print lines,

    return
if __name__ == '__main__':
    main()
