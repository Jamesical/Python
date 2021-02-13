#Travis Saulat 1/22/2021 DUE:1/29/2021
#MASTER CODE FOR FIRST PROJECT - Contains and runs each once
#in one run - in the same order as assigned - this is not meant
#for test but easy storage and reference


#1 Travis Saulat Python Programming Assignment: Exam Student 1/22/2021 DUE:1/29/2021

print("-Exam Attendence Python Program-\n")
held = float(input('How many classes have been held?: '))                 #series of inputs for the questions
atte = float(input('How many classes have you attended?: '))
temp = float(input('What is your current temperature in Farenheit: '))

total = (atte/held)*100
#print(total) used to test what the total is for the if statement

if total < 75:

    print("\nYou are NOT allowed to attend the exam because your attendence is", round(total,2),'% and your temperature is', temp, end=' degress Farenheit\n\n\n\n')

else:
        
    print("\nYou are allowed to attend the exam because your attendence is", round(total,2),'% and your temperature is', temp, end=' degress Farenheit\n\n\n\n')
        

##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################

#2 Travis Saulat Python Programming Assignment Grades 1/22/2021 DUE:1/29/2021

print("-Exam Marks to Grade Python Program-\n")
mark = int(input('What were your marks?: '))

if (mark >= 90):
    print("Excellent\n\n\n\n")

elif (mark >=80):
    print("Very Good\n\n\n\n")

elif (mark >= 70):
    print("Good\n\n\n\n")

elif (mark >= 45):
    print("You can do better\n\n\n\n")

elif (mark >= 25):
    print("Are you OK\n\n\n\n")

else:
    print("what is wrong with you\n\n\n\n")
    

           
    #code just goes down the list and knocks them off one by one
    #then at the ends it has to be a certain set of values
    #so there is an else (less typing)

##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################

#3 Travis Saulat Python Programming Assignment Age 1/22/2021 DUE:1/29/2021

print("-Highest and Lowest Age Python Program-\n")
age1=int(input("What is your age, first individual?: "))
age2=int(input("What is your age, second individual?: "))
age3=int(input("What is your age, third individual?: ")) #simple inputs for data converting to ints because of run issues

high = 0
low = age1

#######################################

if age1 > high:
    high = age1
                                    #ifs and elifs just check each value since there are a limited amount
elif age1 < low:      
    low = age1          

#######################################

if age2 > high:
    high = age2
    
elif age2 < low:
    low = age2

#######################################

if age3 > high:
    high = age3
    
elif age3 < low:
    low = age3

#######################################

print("\nThe oldest person is", high,end=' years old.')
print("\nThe youngest person is", low, end=' years old\n\n\n\n')

##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################

#4 Travis Saulat Python Programming Assignment Absolute Value 1/22/2021 DUE:1/29/2021

print("-Absolute Value Calculator Python Program-\n")
num = int(input("Choose a number, any integer number: "))

if num < 0:
    num = num*-1
    print("The absoulute value is", num,'\n\n\n\n')

elif num > 0:
    print("The absoulute value is",num,'\n\n\n\n')

else:
    print("The absoulute value is 0\n\n\n\n")

    #if it is negative multiply by neg one to make it positive
    #if it is not less than or greater than 0 its gotta be 0
    #so that is what gets printed

##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################

#5 Travis Saulat Python Programming Assignment Neg Pos 1/22/2021 DUE:1/29/2021

print("-Negative/Positive Integer Test Python Program-\n")
num = int(input("Choose a number, any interger number: "))

if num < 0:
    
    print("The number is negative\n\n\n\n")

elif num > 0:
    print("The number is positive\n\n\n\n")

else:
    print("The number is 0\n\n\n\n")

    #for comments see "Absolute_Value.py

##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################
##############################################################################################################################################################################

#6 Travis Saulat Python Programming Assignment C++ Code to Python 1/22/2021 DUE:1/29/2021

print("-C++ Code to Python, Python Program-\n")
num = int(input("Enter an interger: "))

if num > 0:
    print("You entered a positive integer:", num)

elif num < 0:
    print("You entered a negative integer", num)

else:
    print("You entered 0")

print("\nThis line is always printed\n\n\n\n")


#I have done this same code three times in the last 10 minutes its just an
#if, elif then else statment
