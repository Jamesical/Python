
numbers = [1]
for number in numbers:
    print(number, end = " ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(numbers)
i=0
while i<length:
    print(numbers[i])
    i += 1

list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]

list2 = list1

print(list2)

############################

def printList(lst):
    for element in lst:
        print(element)

############################

lst = [3, 1, 2, 6, 4, 2]
printList(lst)


