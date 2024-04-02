import os
import time


def rocket():
    top = 20 
    while True:
        print('\n'* top)
        print('       /\     ')
        print('       ||     ')
        print('       ||     ')
        print('       ||     ')
        print('     ((||))     ')
        time.sleep(0.1)
        os.system('cls')
        top -= 1
        if top < 0:
            top = 20 


rocket()

     
        