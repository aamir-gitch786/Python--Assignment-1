'''3. Write a python program to convert given number of days to a measure of time given in
years, weeks and days. For example 375 days is equal to 1 year 1 week and 3 days
(ignore leap year).'''

days = int(input("Enter number of days :"))
year = days//365
week = (days-(year*365))//7
day = (days-(year*365 + week*7))
print(f"{days} days is equal to {year} year  {week} week and {day} days")