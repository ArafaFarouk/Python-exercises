print ("welcom in the multiplication game: > :) ^-^")

start = int( input( " enter the start number: "))
end = int( input( " enter the end number: "))

for x in range(start,end+1):
    for y in range (1,13):
        print (x, "X" ,y, "=" , x*y)
    print("-"*30)
    
