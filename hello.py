'''Write a python program that accepts seconds as input of type integer. The
program should convert seconds in hours, minutes and seconds. Output
should like this :
Enter seconds: 12200'''

time = int(input("enter time in seconds: \n"))

hour = time/3600
minute = (time%3600)/60
sec = (time%3600)%60

print(int(hour),":",int(minute),":",int(sec))
