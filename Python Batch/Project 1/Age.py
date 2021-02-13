#Travis Saulat Python Programming Assignment Age 1/22/2021 DUE:1/29/2021

age1=int(input("What is your age, first individual?: "))
age2=int(input("What is your age, second individual?: "))
age3=int(input("What is your age, third individual?: ")) #simple inputs for data converting to ints because of run issues

high = 0
low = age1

#######################################

if age1 > high:
    high = age1
    
elif age1 < low:      
    low = all          
    print(low)          

#######################################

if age2 > high:
    high = age2
    
elif age2 < low:
    low = age2
    print(low)

#######################################

if age3 > high:
    high = age3
    
elif age3 < low:
    low = age3
    print(low)

#######################################

print("\nThe oldest person is", high,end=' years old.')
print("\nThe youngest person is", low, end=' years old.')
