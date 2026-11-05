from datetime import date

year=int(input("enter your year:"))
month=int(input("enter your month:"))
day =int(input("enter your day:"))
today=date.today()
current_year = today.year
current_month = today.month
current_day = today.day

year = current_year - year
month= current_month - month
date_difference= current_day - day

if day < 0:
    month -= 1
    current_day +=30
if day < 0:
    year -= 1
    month +=12

total_days = (year*365+ month*30+ date_difference)
print(year, month, date_difference)
print(total_days)