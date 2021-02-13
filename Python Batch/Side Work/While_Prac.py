#Travis Saulat While Loop Practice SUMMATION FACTORIAL 1/26/2021 

summ = 0 #placeholder for the sum
facts = 1#place holder for the product

i = 1 #variables for the loops
j = 1

num = int(input("Enter an integer(SUMM): ")) #input for summatipns 

while i <= num:         #loop for dynamic summantion/factorials
    summ = summ+i
    i = i+1
    
print(summ)


num2 = int(input("\n\nEnter an integer(FACT): "))

while j <= num2:
    facts = facts*j #note the '*'
    j = j+1

print(facts)

