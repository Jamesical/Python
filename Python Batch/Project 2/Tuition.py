#Travis Saulat Tuition Cost 1/29/2021 DUE 2/5/2021

tuition = float(input("Please enter the tuition cost: "))
increment= int(input("Please enter the increment: "))

total = tuition
tuition = tuition*2 #client request until double the tuition so here it is for the loop
i = 0

while(total <= tuition):

    total = total + (total * (increment*.01)) #add total amount and the increment
    i = i+1                                   #the .01 is to make increment into a percent for the maths
    
    #print (i)
    #print (total, end="\n\n") testing for the unseen during creation
    

    
print(round(total, 2), "is the total and it will take", i, "years.")
