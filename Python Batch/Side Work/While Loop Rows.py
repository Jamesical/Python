#Travis Saulat Multiplication Tables 1/27/2021

i = 1   #while needs precalled variables :(
j = 1

inp1 = int(input("Choose length of table: ")) #Let's you choose the size
inp2 = int(input("Choose width of table: "))  #of the table

while j <= inp1:
    i = 1 #####This here resets the i so now the j is +1 making it 2*1 -> 2*2 -> 2*3 and so on 
    
    while i <= inp2: #this run the loop 13 times and acts as a factor of 1-12
        print(j*i, end=' ')  #EX: j*1 -> j*2 -> j*3
        i = i+1
    j = j+1
    print("\n\n")

  







 
