#wap that takes input a date and display next date of calendar
day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
if month in (1,3,5,7,8,10):
    if day<31:
        day+=1
    else:
        day=1
        month+=1
elif month in (4,6,9,11):
    if day<30:
        day+=1
    else:
        day=1
        month+=1
elif month==2:
    if (year%4==0 and year%100!=0) or (year%400==0):
        if day<29:
            day+=1
        else:
            day=1
            month+=1
    else:
        if day<28:
            day+=1
        else:
            day=1
            month+=1
else:
    if day<31:
        day+=1
    else:
        day=1
        month=1
        year+=1
print("Next date is:",day,"/",month,"/",year)
