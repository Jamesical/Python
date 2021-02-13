
import random

numbers = []
for i in range(9):
    numbers.append(random.randint(0, 100))

length = len(numbers)
start = length // 3
stop = length // 3 * 2
middle = numbers[start:stop]

print(numbers)
print("The middle is ", middle)
