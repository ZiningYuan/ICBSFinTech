def middle_of_three(a, b, c):
    """
    Returns the middle one of three numbers a,b,c
    Examples:
    >>> middle_of_three(5, 3, 4)
    4
    >>> middle_of_three(1, 1, 2)
    1
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if a < b:
        lower = a
        upper = b
    else:
        lower = b
        upper = a
    if c < lower:
        lowest = c
        middle = lower
        biggest = upper
    else: 
        lowest  = lower
        if c > upper:
            biggest = c
            middle = upper
        else:
            biggest = upper
            middle = c
    return middle


def sum_up_to(n):
    """
    Returns the sum of integers from 1 to n
    
    Examples:
    >>> sum_up_to(1)
    1
    >>> sum_up_to(5)
    15
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    sum = 0 
    for i in range(n+1):
        sum  = sum + i
    return sum


def square_root_heron(x, epsilon=0.01):
    """
    Find square root using Heron's algorithm

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_heron(20)
    >>> print(y, c)
    4.47 4
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW
    
    guess = x/2 # Make initial guess
    cnt = 0
    # Loop until squared value of guess is close to x
    while abs(guess*guess - x) >= epsilon:
        guess = (guess + x/guess)/2 # Update guess using Heron's formula
        cnt = cnt +1
    return round(guess, 2), cnt # replace the dots with the final number of iterations


def square_root_bisection(x, epsilon=0.01):
    """
    Find square root using bisection search

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_bisection(20)
    >>> print(y, c)
    4.47 9
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW

    low = 0.0
    high = max(1.0, x) # Why are we doing this? What would happen for x=0.5?
    guess = (low + high)/2 # First guess at midpoint of low and high
    cnt = 0
    while abs(guess*guess - x) >= epsilon:
        if guess*guess < x:
            low = guess # update low
        else:
            high = guess # update high
        guess = (low+high)/2 # new guess at midpoint of low and high
        cnt = cnt +1
    return round(guess, 2), cnt

