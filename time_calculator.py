def add_time(start, duration, starting_day=None):
    try:
        start_time, period = start.split()
        start_hour, start_minute = start_time.split(':')
    except:
        return 'Error: Make sure the time you put in fits this format: HH/MM AM or PM'

    duration_hour, duration_minute = duration.split(':')

    hour = int(start_hour) + int(duration_hour)
    minute = int(start_minute) + int(duration_minute)
    if period == "PM":
        hour += 12

    hour += minute // 60
    minute %= 60

    days_later = hour // 24
    hour %= 24

    if hour < 12:
        period = "AM"
        if hour == 0:
            hour = 12
    else:
        period = "PM"
        if hour > 12:
            hour -= 12
    
    new_time = f'{hour}:{minute:02d} {period}'

    if starting_day:
        starting_day = starting_day.lower().capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        days_index = days.index(starting_day)
        days_index += days_later
        while days_index > 6:
            days_index -= 7
        day = days[days_index]
        new_time += f', {day}'
        
    if days_later == 1:
        new_time = new_time + f' (next day)'
    elif days_later > 1:
        new_time = new_time + f' ({days_later} days later)'

    return new_time
