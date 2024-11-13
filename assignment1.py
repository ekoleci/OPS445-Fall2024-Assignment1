#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by Enco Koleci.
No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. 
I have not shared this python script with anyone or anything except for submission for grading. 
I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.

Author: Enco Koleci
Semester: Fall 2024
Description: Assignment 1, OPS445
'''

import sys

def day_of_week(date_str: str) -> str:
    """Calculate the day of the week for a given date (DD/MM/YYYY).
    
    Based on Tomohiko Sakamoto's algorithm. Uses a predefined monthly offset to identify 
    the weekday index, which corresponds to a day in the 'week_days' list.
    """
    day_num, month_num, year_val = (int(part) for part in date_str.split('/'))
    week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    monthly_offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    
    # Set the year for Jan and Feb to match Sakamoto's algorithm.
    if month_num < 3:
        year_val -= 1

    # calculate the  index for weekday.
    weekday_index = (year_val + year_val//4 - year_val//100 + year_val//400 + monthly_offset[month_num] + day_num) % 7  
    return week_days[weekday_index]

def leap_year(year_val: int) -> bool:
    """Check if a given year is a leap year (returns True) or not (returns False)."""
    return (year_val % 4 == 0 and year_val % 100 != 0) or (year_val % 400 == 0)

def mon_max(month_num: int, year_val: int) -> int:
    """Determine the maximum number of days in a month, taking leap years into account."""
    # February requires daouble check, as it may have 28 or 29 days.
    if month_num == 2:
        return 29 if leap_year(year_val) else 28

    # Standard days in each month.
    days_in_month = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return days_in_month.get(month_num, 30)  

def after(date_str: str) -> str:
    '''
    after() -> Returns the next day in DD/MM/YYYY string format.
    
    Accepts a date string, increments the day by one, and adjusts the month and year 
    if the end of a month or year is reached.
    '''
    day_num, month_num, year_val = (int(part) for part in date_str.split('/'))
    day_num += 1  # Move to the next day
    
    # If day reaches the maximum of the month, we are gonna decrease the month.
    if day_num > mon_max(month_num, year_val):
        day_num = 1
        month_num += 1
        
        # If month goes more than  December, decrease the year.
        if month_num > 12:
            month_num = 1
            year_val += 1

    return f"{day_num:02}/{month_num:02}/{year_val}"

def before(date_str: str) -> str:
    """Return the date for the previous day, in DD/MM/YYYY format."""
    day_num, month_num, year_val = (int(part) for part in date_str.split('/'))
    day_num -= 1  # Move to the previous day

    # If day day below 1, move to the last day of the previous month.
    if day_num < 1:
        month_num -= 1
        
        # If month goes below January, reset to December of the previous year.
        if month_num < 1:
            month_num = 12
            year_val -= 1
        day_num = mon_max(month_num, year_val)

    return f"{day_num:02}/{month_num:02}/{year_val}"

def print_usage():
    """Display usage instructions to the user and terminate the program."""
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date_str: str) -> bool:
    """Validate date format (DD/MM/YYYY) and check if it falls within a valid range."""
    try:
        day_num, month_num, year_val = (int(part) for part in date_str.split('/'))
        return 1 <= month_num <= 12 and 1 <= day_num <= mon_max(month_num, year_val)  
    except ValueError:
        return False  # If parsing fails, the date is invalid

def day_iter(start_date: str, days: int) -> str:
    """
    Calculate a new date by moving 'days' forward or backward.
    Returns the final date in DD/MM/YYYY format.
    - start_date: the initial date as a string in DD/MM/YYYY format
    - days: the number of days to move; positive for forward, negative for backward
    """
    curr_date = start_date
    for _ in range(abs(days)):
        curr_date = after(curr_date) if days > 0 else before(curr_date)
    return curr_date

if __name__ == "__main__":
    # Verify that the arguments are provided.
    if len(sys.argv) != 3:
        print_usage()
    
    input_date, shift_value = sys.argv[1], sys.argv[2]

    #check if input_date is a valid date and shift_value is an integer
    if not valid_date(input_date) or not shift_value.lstrip('-').isdigit():
        print_usage()

    shift_value = int(shift_value)  #convert to integer
    final_date = day_iter(input_date, shift_value)
    # Output.
    print(f'The target date is {day_of_week(final_date)}, {final_date}.')
