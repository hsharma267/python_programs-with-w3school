# Python Dates

import datetime
print("-- Python Dates --")


x = datetime.datetime.now()
print(x)

print("-- Date Output --")

print("-- Date example --")
print(x.year)
print(x.strftime("%A"))

print("-- Create Date Object --")
y = datetime.datetime(2020, 11, 28)
print(y)
print("-- The strftime() method --")
y = datetime.datetime.now()
print(y.strftime("%a"))  # days, short version
print(y.strftime("%A"))  # days, full version
print(y.strftime("%b"))  # months, short version
print(y.strftime("%B"))  # months, full version
print(y.strftime("%y"))  # years, short version
print(y.strftime("%Y"))  # years, full version
print(y.strftime("%M"))  # Minutes
print(y.strftime("%S"))  # Sceonds
print(y.strftime("%I"))  # hours, 12 hours
print(y.strftime("%H"))  # hours, 24 hours
print(y.strftime("%p"))  # AM/PM
print(y.strftime("%x"))  # Local version of date
print(y.strftime("%X"))  # Local version of time
