#(d,m,y)
# write a program to create 2 date tuples and find the number of days b/w the 2 dates

from datetime import date
date1=date(2023,9,10)
date2=date(2026,9,15)
print("Number of days b/w the given dates=",(date2-date1).days)
