#wap that takes input a date and display next date of calendar
day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
#function to check leap year
def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False
def next_date(d, m, y):
    month_days = [31, 28 + is_leap_year(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    d += 1  
    
    if d > month_days[m - 1]:  
        d = 1
        m += 1  
        
        if m > 12:  
            m = 1
            y += 1  
         
    return d, m, y
next_day, next_month, next_year = next_date(day, month, year)
print(f"The next date is: {next_day}/{next_month}/{next_year}")