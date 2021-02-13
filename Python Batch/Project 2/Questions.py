#Travis Saulat Random Quiz 1/29/2021 DUE 2/5/2021

import random

quest = int(input("How many questions do you want? " ))
i = 0
r = 0
w = 0

while (i < quest):
    i=i+1

    a= random.randint(1,10)
    b= random.randint(1,10)
    ans = a - b

    print(i, ") ", a, " - ", b, "=", end=' ')

    input1 = int(input())

    if(input1 == ans):
        r = r+1
    else:
        w = w+1
    #print(input1, ans, r, w) used for unseen variable testing
        
print("You had", r, "out of",quest,"correct.")
print("Your grade for this practice is", ((r/quest)*100), "%")
    

    
    
    
    
