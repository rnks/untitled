

import sys

def Hello(name):

        if name == 'Alice':
            print('Working in Alice mode )))')
            name = name + '???'
            name = name + '!'
            print ('Hello', name)
        else:
            print(name + "Does not exist!")



def main():
    Hello(sys.argv[1])




main()