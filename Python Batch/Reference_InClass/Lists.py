#Travis Saulat Lists 2/1/2021

#Lists can have mixed values, int - string - float - object 

list1= list() # create empty list
list2= list([2,3,4]) #create list with elements 2,3,4
list3= list(["red", "green", "blue"]) #create list with strings 
list4= list(range(3,6)) # create list with elements 3,4,5
list5= list("abcd") #create list with characters a,b,c

list1 = [] #same as list()
list2 = [2,3,4]

#print(list1)
#print(list2)
#print(list3)
#print(list4)
#print(list5)

int_list = [1, 2, 3, 4, 5]
#1 has an index value of 0 and 2 has an index value of 1 and so on
#print(int_list[0])
#print(int_list[-1])

#len(list1)
#max(list1)
#min(list1)
#sum(list2) #various function to use with lists

#random.shuffle(list2)

#my_var = 2
#my_list = [2, "red", 2.0, my_var, "Red", 8//4] 
#print(my_list.count("Red")) #finds the number of 2's in the list *****VERY USEFUL******

#list_sum = [1,101]
#sum(list_sum)
#avg

#my_list  = [1, 2, 3]
#new_element = 10

#my_list.append(new_element) #append always adds the element to the end
#my_list.append(20)

#my_list = [1, 2, 3, 4]
#print(my_list)
#print(my_list.pop()) #shows the last value that it will delete
#print(my_list)

#my_list = [1, 2, 3, 4]
#my_list.insert(2, "Yo") #requires two parameters the index and replacement value

#print(my_list)

#my_list = [1, 2, 3, 4, 2, 3, 4, 5, 1, 1, 3]
#my_list.remove(2)
#print(my_list)

#my_list.sort


# the + operator adds two lists together ---> ORDER IS IMPORTANT
# the * operator duplicates lists
# the :

#list1 = [2,3]
#list2 = [1,9]
#list3 = 2*list1
#list4 = list3[2:4] #[start:stop before]
#print(list4)


#list1 = [2, 3, 5, 2, 33, 21]
#2 in list1

#2.5 in list1

#List_name = [x for x in range(START, STOP, STEP)]

#listx = [jo for jo in range(101, 0, -2)] #makes a list with ints 1-10 
#print(listx)

#list1 = [j for j in range(0, 5)]
#print(list1)

#list2 = [.5* x for x in list1]
#print(list2)

mul = 1

for i in range(1, 10):
    mul = 5*i
    print(mul)

list5 = [x for x in range(5, 55, 5)]
print(list5)


numbers = [1]
for number in numbers:
    print(number, end = " ")

numbers = [1, 2, 3, 4]
length = len(numbers)
i=0
while i<length:
    print(numbers[i])
    i += 1
         

















