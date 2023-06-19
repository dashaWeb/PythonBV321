

day_start = 20
month_start = 3
year_start = 2023

# 20 + 28 + 31 => 79
month = month_start
month -= 1
days_start = 0
if month == 11:
    days_start+=30
    month-=1
if month == 10:
    days_start+=31
    month-=1
if month == 9:
    days_start+=30
    month-=1
if month == 8:
    days_start+=31
    month-=1
if month == 7:
    days_start+=31
    month-=1
if month == 6:
    days_start+=30
    month-=1
if month == 5:
    days_start+=31
    month-=1
if month == 4:
    days_start+=30
    month-=1
if month == 3:
    days_start+=31
    month-=1
if month == 2:
    if year_start % 4 == 0 or year_start % 400 == 0 and year_start % 100 !=0:
        days_start+=29
    else:
        days_start+=28
    month-=1
if month == 1:
    days_start+=31
    month-=1

days_start += day_start
print(days_start)

# 31 + 30 + 31 + 28 + 31 + 15 ==> 166 
day_end = 15
month_end = 6
year_end = 2023
month = month_end
month -= 1
days_end = 0
if month == 11:
    days_end+=30
    month-=1
if month == 10:
    days_end+=31
    month-=1
if month == 9:
    days_end+=30
    month-=1
if month == 8:
    days_end+=31
    month-=1
if month == 7:
    days_end+=31
    month-=1
if month == 6:
    days_end+=30
    month-=1
if month == 5:
    days_end+=31
    month-=1
if month == 4:
    days_end+=30
    month-=1
if month == 3:
    days_end+=31
    month-=1
if month == 2:
    if year_end % 4 == 0 or year_end % 400 == 0 and year_end % 100 !=0:
        days_end+=29
    else:
        days_end+=28
    month-=1
if month == 1:
    days_end+=31
    month-=1
days_end+=day_end
print(days_end)
