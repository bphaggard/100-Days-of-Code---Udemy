import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() #output is integer. Monday = 0, Tuesday = 1 etc

#Our own datetime
day_of_birth = dt.datetime(year=1989, month=2, day=17)
print(day_of_birth)