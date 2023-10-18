'''List
Write a python program to
 Find the sum and average of given numbers using lists
 Display elements of list in reverse order
 Find the minimum and maximum elements in the lists'''

l = []
add = 0
maxi = 0
mini = 100
count = int(input("enter no of elements in list: "))

for x in range(0,count):
	element=int(input("enter the number: "))
	l.append(element)
	add += element
	
	if maxi<element:
		maxi = element
	if mini>element:
		mini = element
	
print("Sum of all elements: ",add," and average: ",(add/count),"\n")

print("reversed list is [",end="")
for x in range(0,count):
	print(l[count-x-1],end=", ")
print("]\n")
	
print("smallest num in list is: ",mini," and greatest is: ",maxi)
