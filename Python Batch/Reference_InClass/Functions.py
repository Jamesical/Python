
########################################

def printList(lst):
    for element in lst:
        print(element, end =" ")

#######################################

def printEven(lst):
    for element in lst:
        if element%2 == 0:
            print(element, end=" ")

#######################################

    def countOdd(lst):
    i = 0
    for element in lst:
        if element%2 != 0:
            print(end="a")
    print(i)

#######################################

def max_num_in_list(lst):
    a = max(lst)
    b = min(lst)
    print("The max is:", a)
    print("The min is:", b)
            

lst = [3, 1, 2, 6, 4, 2]

list1 = [1, 2, 3, 4, 5]
list2 = [10, 40, 23, 17, 1]

printList(list1)
print()
printList(list2)

max_num_in_list(lst)


