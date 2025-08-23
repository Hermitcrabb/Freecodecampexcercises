# Time Calculator without using any library

def add_time(start, duration,day=''):
    s1 = start.split() #splited to '3:10', 'AM or PM'
    t1 = s1[0] #time value stored as 3:10
    ampm = s1[1] #stores AM or PM string

    h1,m1 = map(int,t1.split(":")) #separated the variable to 3:10 to 3,10

    h2,m2 = map(int,duration.split(":")) #similar to line 6

    if ampm.upper() == "PM" and h1 !=12:
        h1 +=12
    elif ampm.upper() == "AM" and h1 ==12:
        h1 = 0
    

    minute = m1+m2
    extra_hour = minute // 60
    final_minute = minute %60
    total_hour = h1+h2 + extra_hour

    days_passed = total_hour //24
    total_hours = total_hour%24 

    new_ampm = 'AM'
    display_hour = total_hours
    if total_hours >=12:
        new_ampm = 'PM'
        if total_hours >12:
            display_hour = total_hours - 12
    if display_hour == 0:
        display_hour = 12
    
    if day:
        weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day_index = weekdays.index(day.capitalize())
        # check for extra time if any cros the midnight mark
        total_days_for_day = days_passed
        if (h1+h2+extra_hour)%24 <h1:
            total_days_for_day +=1
        new_day_index = (day_index + days_passed) % 7
        new_day = weekdays[new_day_index]
    
    if day:
        if days_passed + ((h1+h2+extra_hour)%24 <h1) ==1:
            day_info = f"{new_day} (next day)"  
        elif days_passed + ((h1+h2+extra_hour)%24 <h1) > 1:
            total_days_later = days_passed + ((h1+h2+extra_hour)%24 <h1) 
            day_info = f"{new_day} ({days_passed} days later)"
        else:
            day_info = day
        new_time = f"{display_hour}:{final_minute:02d} {new_ampm}, {day_info}"
    else:
        if days_passed ==1:
            new_time=f"{display_hour}:{final_minute:02d} {new_ampm} (next day)"
        elif days_passed >1:
            new_time = f"{display_hour}:{final_minute:02d} {new_ampm} ({days_passed} days later)"
        else:
            new_time = f"{display_hour}:{final_minute:02d} {new_ampm}"
    return new_time


print(add_time('8:16 PM', '466:02', 'tuesday'))  



