'''Conditional Structures
The marks obtained by a student in 3 different subjects are input by the
user. Python program should calculate the average marks obtained in 3
subjects and display the grade. The student gets a grade as per the
following rules:
Average Grade
90-100 O
80-89 A
70-79 B
60-69 C
40-59 D
0-39  F'''

mark1=int(input("sub1(out of 100): "))
mark2=int(input("sub2(out of 100): "))
mark3=int(input("sub3(out of 100): "))

avg = int((mark1+mark2+mark3)/3)

if 100>=avg>=90:
	print("Grade obtained: O")
elif 89>=avg>=80:
	print("Grade obtained: A")
elif 79>=avg>=70:
	print("Grade obtained: B")
elif 69>=avg>=60:
	print("Grade obtained: C")
elif 59>=avg>=40:
	print("Grade obtained: D")
elif 39>=avg>=0:
	print("Grade obtained: F")
