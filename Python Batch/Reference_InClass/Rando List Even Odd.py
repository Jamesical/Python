
import random

numbers = []
for i in range(20):
    numbers.append(random.randint(0, 100))
    
odd = []
even = []

for number in numbers:
    if number % 2 == 0:
      even.append(number)
    else:
      odd.append(number)
      
print("The odd numbers: ", odd)
print("The even numbers: ", even)
print(len(odd) + len(even))
