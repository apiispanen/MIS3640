import time
from time import gmtime, strftime
print(strftime("%a, %d %b %y %H:%M:%S", gmtime()))
print(' {} days since Epoch.'.format(int(time.time())))

#trial 2
years = time.time()/60/60/24/365.25
days = years*365 
hours = days*24 
minutes = hours*60
seconds = minutes*60


year = years +1970
day = (year-int(year))*365.25
hour = (day-int(day))*24 + 12
minute = (hour-int(hour))*60
month = (year-int(year))*12+1

year=int(year)
month = int(month)
day=int(day)
hour=int(hour)
minute=int(minute)

print(years, days, hours, seconds, time.time())
print(year, month, ' Day #:', day, ' Time:',hour,':',minute)

#trial 3
current = time.time()
second2 = current %60
minute2 = (current//60)%60
hour2 = (current//60)//60 %24
day2 = (current//60)//60 %24

print('It has been %d days, at %d:%d:%d' %(day2, hour2, minute2,second2))
