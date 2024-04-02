# the main games by oop

class Games :
    def __init__(self):
        print("Welcome in the main game: :)^-^")
        print ("choice your game from our collection")
        print ("press{1} : play Even_odd game")
        print ("press{2} : play Avarege game")
        print ("press{3} : play Multiplication  game")
        print("press{x} : for exit ")

        self.Choices()

#---get choice from user---#
    def Choices (self):
        while True:
            choice = input("Enter your choice: ")
            if choice == 'x':
                print(" bay bay ...^-^")
                break
            else:
                try :
                    choice = int(choice)
                    if choice == 1:
                        self.Even_odd_game()
                    elif choice == 2:
                        self.Avarege_game()
                    elif choice == 3:
                        self.Multiplication_game()
                    else:
                        print("please choice between ( 1,2,3)") 

                except ValueError:
                    print("please enter anumaric value ") 
                

              
# --- define game 1 logic ---#
    def Even_odd_game(self):
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

# ---define game 2 logic---#
    def Avarege_game(self):

        print ("enter 'x' for exit: ")
        count =input ("how many number would you like to sum : ")
        curent_count = 0
        summ = 0
        if count == 'x':
            print("thanks...")
            quit 
        else:  
            count = float(count)
            while curent_count < count:
                number = float (input("enter a number:  "))
                summ += number
                curent_count +=1

            print ("sum of all numbers =" , summ)
            print ("Avarege = ", summ / count)



# ---define game 3 logic---#
    def Multiplication_game(self):
        start = int( input( " enter the start number: "))
        end = int( input( " enter the end number: "))

        for x in range(start,end+1):
            for y in range (1,13):
                print (x, "X" ,y, "=" , x*y)
            print("-"*30)
            

Game = Games()
    
    
        
