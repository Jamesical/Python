#Travis Saulat Hexademical Calc 1/29/2021 DUE: 2/5/2021

input1 = int(input("What is your decimal number: "))
rem_store =[] #need somewhere to store the remainders for the conversion

convert_string = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
#above is for each possible character in hexadecimal

hexa = "" #preps for printing final product

if input1 > 0:
    while input1 > 0: #once the input cant be divided anymore the loop is finised
        rem_store.append(input1%16) #to convert take the remainder and correlate it with a character
        input1 = input1//16         #then take the amount you can divide and divide it again and repeat until you cant
        
    for i in rem_store[::-1]:  #thank you AndroX this is for a REVERSE like string/for function to print the characters
        hexa = hexa + convert_string[i]
else:
    hexa = 0 #in case they type zero 
        

print("You decimal number is", hexa, "in hexadecimal.")

