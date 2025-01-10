
year = input('Tell me a year: ')
year = int(year)


if year % 4 != 0:
   print("This year is not a leap year!")
elif (year % 4 == 0) and (year % 100 != 0):
    print("This year is a leap year!")
elif (year % 4 ==0) and (year % 100 == 0) and (year % 400 != 0):
    print("This year is not a leap year!")
else:
    print("This year is a leap year")
    
