#Travis Saulat Greast Common Divisor 1/27/2021

in1 = int(input("Please enter an integer: "))
in2 = int(input("Please enter another integer: ")) #simple input need two variables

i = 1

while(i <= in1 and i <= in2):
    if (in1%i == 0 and in2%i == 0): #the highest combination of '0's
        GCD = i                     #will be the GCD '%' essential 
    i = i+1

    
print("The greated common divisor is: ",GCD)




    

    
