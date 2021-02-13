#Travis Saulat Fucntions 

####################################################

def add(a, b): #addition fucntion that takes inputs from "main"
    """Function that adds the two inputs""" #adds a description for the help function
    c = a+b
    print("\nThe addition is:", c)

def mul(a, b): #multiplication function that takes inputs from "main"
    """Function that multiplies the two inputs"""
    c = a*b
    print("\nThe multiplication is:", c)

###################################################

while 1==1: #for invalid input 

    d = input("Addition or Multiplication?(a or m): ")
    print()

    if d == "a": #addition function call block
        a = int(input("Enter an interger to add: "))
        b = int(input("Enter another interger to add: "))
        add(a, b)
        break
        

    elif d == "m": #multiplication function call block
        a = int(input("Enter an interger to multiply: "))
        b = int(input("Enter another interger to multiply: "))
        mul(a, b)
        break #needed for 
        

    else:
        print("\nINVALID INPUT!\n")
        continue #this repeats the prompts for a wrong input

help(add)
help(mul)


