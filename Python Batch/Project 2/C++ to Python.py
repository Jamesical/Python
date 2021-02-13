#Travis Saulat C++ to Python 1/29/2021 DUE: 2/5/2021 
r = int(input("Input number of rows for your diamond: ")) 


for i in range(0, r+1):
        
        for j in range(0, r-i):
            print(" ", end="")

            
        for j in range(0, 2*i-1):  ##issue here
            print("*", end = "")
        print()
           
            
for p in range(r-1, 0, -1):
        
    for f in range(0, r-p):
        print(" ", end="")

   
    for f in range(0, 2*p-1):
        print("*", end="")
    print()

