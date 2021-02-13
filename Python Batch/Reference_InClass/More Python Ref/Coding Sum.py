
import random

numbers = []
total = 0

for i in range(20):
    numbers.append(random.randint(0, 100))
    
for number in numbers:
    total += number
    
print("The sum of numbers is", total) 
print(sum(numbers))
