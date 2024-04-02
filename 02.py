# Avarege game
# problem solving input for exit ("ok good")

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
