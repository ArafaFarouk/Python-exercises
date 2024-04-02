# even_odd game
# 0 is even i need slove this problem (" ok good")

while True:
    print("welcom  in even_odd game")
    number = input("Enter a number... And i will tell you if even or odd ! ")
  
        
    if number == 'x':
        print("closing game")
        print("thanks ...")
        break   
    try:
        number = int(number)
        if number == 0:
            print("can not devid by zero")
        elif number % 2 == 0 :
            print("Even number")
        else:
            print("Odd number")
    except ValueError  :
            print("please enter anumaric number")
    print ("-"*20)     
#-----------------------------------------------------#

print("enter 'x' for exit")

while True:
    inp = input("enter a number: ")
    if inp == 'x':
        break
   
    try :
        number = float(inp)
    except ValueError:
        print("enter a numaric number: ")
    else:
        if number == 0:
            print("can not devid by zero")
            
        test = number % 2
        if test == 0:
            print(" even number")
        elif test == 1:
            print("odd number")
        else:
            print("is very strange.")
        
