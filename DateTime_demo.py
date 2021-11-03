import datetime
#print(help(datetime))
""""
today = (datetime.date.today())
now = (datetime.datetime.now())
print(now)

#time.sleep(5)
then = datetime.datetime.now()
print(then)
print((then-now).days)

bd = (datetime.date(2021,11,1))


print((today-bd).days)

print(datetime.datetime.weekday(bd))
"""

# Date class
print(dir(datetime.date))

# Time Class
print(dir(datetime.time))

# Date Time class
print(dir(datetime.datetime))

print("========================")

dt = datetime.date(1991,4,12)
print(dt.strftime("%A,%B,%d,%Y"))

tday = datetime.date.today()
print(tday.strftime("%A,%B,%d,%Y"))

print("No of days on earth: ",(tday-dt).days)

tdelta = datetime.timedelta((tday-dt).days)
print(tdelta + dt)

print("========================")

birth_date = datetime.date(1965,1,31)
print("Day: ",birth_date.strftime("%A,%B,%d,%Y"))

birth_time = datetime.time(15,56,10)
print("Time: ",birth_time.strftime("%H,%M,%S,%p"))

birth_datetime = datetime.datetime(1965,1,31,15,56,10)
print("Date & Time: ",birth_datetime.strftime("%A,%B,%d,%Y    Time = %H,%M,%S,%p"))

print("========================")

current_datetime = datetime.datetime.today()
print("Current date time : ",current_datetime)

print("========================")

# Convert string to date time object

mystring = "8/4/1991"
conv2dt = datetime.datetime.strptime(mystring,"%m/%d/%Y")
print(conv2dt)
print(conv2dt.month)
print(conv2dt.day)
print(conv2dt.year)
print(type(conv2dt))    # Check the object type

print()
conv = conv2dt.strftime("%A,%B,%d,%Y")
print(conv)
print(type(conv))   # Check the object type


