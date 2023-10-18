'''Control structures
Floyd's triangle is a right-angled triangular array of natural numbers as
shown below:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Write a python program to print the Floyd’s triangle'''

i=1
for x in range(0,5):
	for y in range(x+1):
		print(i, end=" ")
		i+=1
	print("")
