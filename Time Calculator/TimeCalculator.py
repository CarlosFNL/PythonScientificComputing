
#Helper function to get PM/AM from the hour string
def get_pm_am(start): 
    pm_am = ''
    for char in start:
        if char.isalpha():
            pm_am = pm_am + char
    return pm_am

#Helper function to get the first number from the hour string
def get_digit_one(start):
    return int(start.split(':')[0])
#Helper function to get the second number (after the :) from the string
def get_digit_two(start):
    temp = start.split(':')[1]
    return int(temp.split(' ')[0])

#Helper function to convert from PM / AM to 24 hours format
def convert_hours(start):
    hour_type = get_pm_am(start)
    digit_one = get_digit_one(start)
    digit_two = get_digit_two(start)
    new_time = ''

    if (digit_one >= 1 and digit_one <=11) and hour_type == 'PM':

        new_time = str(digit_one + 12) + ':'+ str(digit_two)
        return new_time 
    if (digit_one >= 1 and digit_one <= 11) and hour_type == 'AM':
        new_time = str(digit_one ) + ':' + str(digit_two)
        return new_time 
    
    if digit_one == 12 and hour_type == 'AM':
        new_time = str(digit_one-12) + ':' + str(digit_two)
        return new_time
    else:
        new_time = str(digit_one) + ':' + str(digit_two)
        return new_time

#Helper function to convert from 24 Function to PM / AM
def convert_to_pm_am(sum_time):
    digit_one = get_digit_one(sum_time)
    digit_two = get_digit_two(sum_time)
    final_time = ''

    if digit_two <10:
        digit_two ='0' + str(digit_two)
    else:
        digit_two = str(digit_two)

    if digit_one == 0:
        final_time = '12'+':'+digit_two+' '+'AM'
        return final_time
    
    if digit_one >= 1 and digit_one <= 11:
        final_time = str(digit_one) + ':' + digit_two+' '+ 'AM'

    
    else: 
        if digit_one == 12:
            final_time = str(digit_one)+':'+digit_two+' ' + 'PM'
        else:
            final_time = str(digit_one-12)+':'+digit_two+' ' + 'PM'

    return final_time 

#Main function where we set the time, day and number of days
def add_time(start, duration,starting_day= None):
    time_formated = convert_hours(start)
    digit_one = get_digit_one(time_formated)
    digit_two = get_digit_two(time_formated)
    extra_one = get_digit_one(duration)
    extra_two = get_digit_two(duration)
    quote_end =''
    quote_day =''

    days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday':2,
        'thursday':3,
        'friday': 4,
        'saturday':5,
        'sunday':6
    }
  
    # If the number of minutes is greater than 60 we add 1 hour and recalculate the number of minutes minus 60
    if (digit_two + extra_two) >= 60:
        extra_one +=1
        number_of_minutes = (digit_two + extra_two) - 60
        number_of_days = (digit_one + extra_one) // 24
    else:
        number_of_days = (digit_one + extra_one) // 24
        number_of_minutes = digit_two + extra_two
    #  This part is to set the correct format in the number, for example 04 instead of 4
    if number_of_minutes <10:
        number_of_minutes ='0' + str(number_of_minutes)

    added_time = str((digit_one+extra_one)-(24*number_of_days)) +':'+ str(number_of_minutes)
    final_time = convert_to_pm_am(added_time)

    # We have the time set, now we need to check the days

    if starting_day:

        if number_of_days == 0: 
            day_formated = starting_day[0].upper() + starting_day[1:]
            quote_day=', ' + day_formated

        else:
            day_index = days[starting_day.lower()]
            new_day_index = (number_of_days + day_index) % 7

            for key,val in days.items():
                if val == new_day_index:
                    new_day = key
            day_formated = new_day[0].upper() + new_day[1:]
            quote_day = ', '+day_formated

    if number_of_days == 1:
        quote_end = ' (next day)'
    elif number_of_days > 1:
        quote_end= ' ('+str(number_of_days)+' '+'days later'+')'
        
    final_time = final_time + quote_day + quote_end

    return final_time