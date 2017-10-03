
#Session 2

#1.1
x = 5
pi = 3.1415926535
print((4/3)*pi*(x**2))

#1.2

disc = .40
cover = 24.95
quantity = 60
gross = ((1-disc) * cover) * (quantity) +3 + (quantity - 1) *.75
print('The total cost for 60 copies is ${:.2f}.'.format(gross))


#1.3

start_time_hr = 6 + 52 / 60
easy_pace_hr = (8 + 15 / 60 ) / 60
tempo_pace_hr = (7 + 12 / 60) / 60
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print('Breakfast time is {:02d}:{:02d}:{:02d}.'.format(
    int(breakfast_hr), 
    int(breakfast_min), 
    int(breakfast_min)))

    
#  1.4
perc = (89-82)/82*100
print("The percentage of the increase is {:04.1f}%.".format(perc))




