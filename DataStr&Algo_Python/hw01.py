# -*- coding: utf-8 -*-
"""
Homework 1
"""

#####
# Wind chill calculator
#####


from typing import no_type_check_decorator


def wind_chill(temp, wind_speed, a=13.12, b=0.6215, c=-11.37, d=0.16, e=0.3965):
    """
    Converts temperature and wind speed into wind-chill index.

    Formula: wci = a + b*T + c*W^d + e*T*W^d, where T is temperature and W is wind speed

    Parameters:
        temp: temperature in Celsius
        wind_speed: wind speed in km/h
        
        The following constants have default values specified above.
        You don't need to include them in function calls.
        
        a: constant with default value
        b: constant with default value
        c: constant with default value
        d: constant with default value
        e: constant with default value

    Returns:
        Wind chill index.
        If wind speed is lower than 5, return the temperature.
        Otherwise, return the index according to the formula, rounded to integer value

    Example use:
    >>> wind_chill(10, 0)
    10
    >>> wind_chill(-10, 20)
    -18
    >>> wind_chill(-20, 30) + 1
    -32
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if wind_speed < 5:
        return temp
    else:
        WCI = a + b * temp + c * (wind_speed ** d) + e * temp* (wind_speed ** d)
        return(round(WCI))


#####
# A brainteaser
#####


def the_35_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: (positive) integer

    Returns:
        - For n divisible by both 3 and 5, return '35'; otherwise:
        - For n divisible by 3, return '3'
        - For n divisible by 5, return '5'
        - Otherwise, return None.

    Example use:
    >>> the_35_teaser(9)
    '3'
    >>> the_35_teaser(95)
    '5'
    >>> the_35_teaser(300)
    '35'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if n % 3 == 0 and n % 5 == 0:
        return '35'
    elif n % 3 == 0 and n % 5 != 0:
        return '3'
    elif n % 3 != 0 and n% 5 == 0:
        return '5'


def the_35_looper(n):
    """
    Prints the first n values of the_35_teaser starting from 1
    
    Note you may call the function the_35_teaser
    
    Parameters:
        n: (positive) integer
    
    Example use:
    >>> the_35_looper(15)
    None
    None
    3
    None
    5
    3
    None
    None
    3
    5
    None
    3
    None
    None
    35
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for i in range(1, n+1):
        if i % 3 != 0 and i% 5 != 0:
            print("None")
        else:
            print(the_35_teaser(i))
    

#####
# Date string conversion: slash-date format to dash-date format
#####



def date_conversion(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format" as specified in the HW instructions

    Assume input is in American date ordering (month-day-year) -> convert to European ordering (day-month-year).
    Assume that two-digit years are in the past century (1923-2022 is "past century", before or after is not).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999.

    Parameters:
        date_string: string date in "US slash format", eg, 12/8/16, 1/12/1898, 1/1/25 (we assume valid dates)

    Returns:
        string date in "scientific dash format", eg, 08-12-2016, 12-01-1898, 01-01-1925

    Example use:
    >>> print(date_conversion('12/8/16'))
    08-12-2016
    >>> print(date_conversion('01/12/1898'))
    12-01-1898
    >>> print(date_conversion('11/5/25'))
    05-11-1925
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    o_day, o_month, o_year = date_as_list[1],date_as_list[0],date_as_list[2]
    if len(o_day) == 1:
        n_day = '0'+ o_day
    else:
        n_day = o_day
    
    if len(o_month) == 1:
        n_month = '0'+ o_month
    else:
        n_month = o_month
    
    if len(o_year) == 2:
        if int(o_year) <=22:
            n_year = "20" + o_year
        else:
            n_year = "19" + o_year
    else:
        n_year = o_year

    result = n_day + "-" + n_month + "-" + n_year
    return result
    

##### 
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format"

    Valid dates are as follows:
    - US date ordering (month-day-year).
    - Two-digit years are in the past century (1923-2022 is "past century", before or after is not).
    - The year of the date is in either range 00 - 99 or 1000 - 9999
    - An actual date that has occurred or will occur

    Parameters:
        date_string: string date in "US slash format", eg, 12/8/16, 1/12/1898, 1/1/25 (DO NOT assume every input is a valid date)

    Returns:
        if input is valid: return string date in "dash" format, eg, 08-12-2016, 12-01-1898, 01-01-1925
        if input would be valid in European date ordering, print a message for the user and return the default return value None. 
            - For example, if the input is 16/3/2021, your function should then print out "Not a valid date. Did you mean to input 3/16/2021?" and return None.
        if input is not valid: print "Not a valid date." then return the default return value None

    Example use:
    >>> print(date_conversion_robust('12/8/16'))
    08-12-2016
    >>> print(date_conversion_robust('1/12/1898'))
    12-01-1898
    >>> date_conversion_robust('1/1/25')
    '01-01-1925'
    >>> print(date_conversion_robust('16/3/2021'))
    Not a valid date. Did you mean to input 3/16/2021?
    None
    >>> print(date_conversion_robust('2/29/2017'))
    Not a valid date.
    None
    >>> date_conversion_robust('131/2/1928')
    Not a valid date.
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if type(date_string) == str: 
        try:
            date_as_list = date_string.split('/')  # Use this to split slash format string into a list
            o_day, o_month, o_year = date_as_list[1],date_as_list[0],date_as_list[2] 
            if len(o_year) == 2:
                if int(o_year) <=22:
                    n_year = "20" + o_year
                else:
                    n_year = "19" + o_year
            else:
                n_year = o_year
        
            try:
                if 0 < int(o_day)<32 and 0<int(o_month) < 32 and 1000 < int(n_year) < 10000:
                    if int(o_month) < 13 and int(o_day) < 32:
                        new_date =  date_conversion(date_string)
                        if int(n_year) % 4 != 0 and o_month == "2" and int(o_day) > 28:
                            print("Not a valid date.")
                            return None
                        elif int(o_month) in [1,3,5,7,8,10,12] and int(o_day) > 31:
                            print("Not a valid date.")
                            return None
                        elif int(o_month) in [4,6,9,11] and int(o_day) > 30:
                            print("Not a valid date.")
                            return None                           
                        else:
                            return new_date
                    elif int(o_month) < 32 and int(o_day) < 13:
                        if int(n_year) % 4 != 0 and o_day == "2" and int(o_month) > 28:
                            print("Not a valid date.")
                            return None
                        elif int(o_day) in [1,3,5,7,8,10,12] and int(o_month) > 31:
                            print("Not a valid date.")
                            return None
                        elif int(o_day) in [4,6,9,11] and int(o_month) > 30:
                            print("Not a valid date.")
                            return None     
                        else:
                            print("Not a valid date. Did you mean to input "+ o_day+ "/" + o_month +"/"+ o_year+"?")
                            return None
                    else:
                        print("Not a valid date.")
                        return None
                else:
                    print("Not a valid date.")
                    return None
            except ValueError:
                print("Not a valid date.")
                return None
        except IndexError:
            print("Not a valid date.")
            return None
    else:
        print("Not a valid date.")
        return None
        

    


def comparison_function(value):
    """
    Comparison function for counting_sort
    
    Parameter:
        value - integer
        
    Returns:
        ??? such that comparisons of return values work as described
    
    Example use:
    >>> comparison_function(99) > comparison_function(18783479)
    True
    >>> comparison_function(123) > comparison_function(321)
    False
    >>> comparison_function(1789) > comparison_function(96861)
    True
    """
    value_str = str(value)
    num_digits = []

    def count_digit(value,int):
        # input: value - a string, int - an integer
        cnt = 0
        for i in value:
            if i == str(int):
                cnt+= 1
            else:
                pass
        return cnt
    
    for num in reversed(range(10)):
        num_digit = count_digit(value_str, num)
        num_digits.append(num_digit)
    
    norm = int(value_str)

    return (num_digits, norm)
    

def counting_sort(items):
    """
    Sorts a list of integers by counting different digits.
    
    Parameters:
        items - list of positive integers
        
    Returns:
        sorted copy of items
        
    Example use:
    >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
    [1111, 3, 333, 41, 241, 53, 73, 19, 29, 98, 9999]
    >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
    [111, 19, 119, 911, 919, 1199, 999]
    >>> counting_sort([1234, 4321, 3214, 2413])
    [1234, 2413, 3214, 4321]
    """
    # Please do NOT edit this function.
    return sorted(items, key=comparison_function)
