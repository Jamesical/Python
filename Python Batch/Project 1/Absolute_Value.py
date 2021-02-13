#Travis Saulat Python Programming Assignment Absolute Value 1/22/2021 DUE:1/29/2021

num = int(input("Choose a number, any interger number: "))

if num < 0:
    num = num*-1
    print("The absoulute value is", num)

elif num > 0:
    print("The absoulute value is",num)

else:
    print("The absoulute value is",0)

    #if it is negative multiply by neg one to make it positive
    #if it is not less than or greater than 0 its gotta be 0
    #so that is what gets printed
