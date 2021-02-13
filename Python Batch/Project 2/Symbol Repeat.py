#Travis Saulat Symbol Improved 

c = int(input("Enter number of rows for pyramid(int): "))

for i in range(1,c+1):
    for j in range(1,i+1): #nested for loop since the row needs repeated as well
        print("&", end=' ')  #as the row needs repeated and a value added
    print()

################################################################

#This is just the top portion but the for loop is just reversed causing a
#pyramid type symbol just to show of for understanding to get project request
#remove everything below these comments

for p in reversed(range(c)):
    for q in reversed(range(p)):
        print("&", end=' ')
    print()



