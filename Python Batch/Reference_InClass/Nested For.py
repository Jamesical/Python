#Travis Saulat Nested For Loop 1/25/2021

c = int(input("Enter Value: "))


for i in range(1,c+1):
    for j in range(1,i+1): #nested for loop since the row needs repeated as well
        print(j, end=' ')  #as the row needs repeated and a value added
        
    print()

for i in range(5,c+1 ):
    for j in range(1, i+1): #nested for loop since the row needs repeated as well
        print(j, end=' ')  #as the row needs repeated and a value added
     
    print()    

    
