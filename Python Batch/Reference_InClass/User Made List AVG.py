#Travis Saulat AVG lists

def createList(input1, lst):
    for a in range(0, input1):
        c = int(input("What do you want in the list: "))
        lst.insert(a, c)

################################################

def printList(lst):
    for a in lst:
        print(a, end=" ")

################################################

def avg(lst, num):
    avg = sum(lst)//len(lst)
    
    for a in lst:
        if a > avg:
            num +=1
    return num

################################################
        
lst = []
num = 0

input1 = int(input("How long do you want your list?: "))
print(end ="\n")

createList(input1, lst)
print()

num = avg(lst, num)
print("There are", num, "above the average in your list")

