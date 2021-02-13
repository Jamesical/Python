#Travis Saulat Python Programming Assignment: Exam Student 1/22/2021 DUE:1/29/2021

held = float(input('How many classes have been held?: '))                 #series of inputs for the questions
atte = float(input('How many classes have you attended?: '))
temp = float(input('What is your current temperature in Farenheit: '))

total = (atte/held)*100
#print(total) used to test what the total is for the if statement

if total < 75:

    print("\nYou are NOT allowed to attend the exam because your attendence is", round(total,2),'% and your temperature is', temp, end=' degress Farenheit')

else:
        
        print("\nYou are allowed to attend the exam because your attendence is", round(total,2),'% and your temperature is', temp, end=' degress Farenheit')
        






          
