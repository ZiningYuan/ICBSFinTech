"""

Homework 2

"""

from socket import NI_NUMERICHOST
from symbol import comparison
from urllib.parse import _NetlocResultMixinStr


def buy_and_hold(prices, start_index=0, starting_money=100.0):
    """
    Buy and hold strategy


    Parameters:
        prices (list): stock prices
        start_index (positive integer, optional): index from which to start the strategy
        starting_money (float, optional): starting cash position. Defaults to 100.0.

    Returns:
        list containing value of position using buy and hold strategy

    Example use:
    >>> res = buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5])
    >>> [round(x, 1) for x in res]
    [100.0, 75.0, 90.0, 115.0, 125.0]
    >>> [round(x, 2) for x in buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5], start_index=2)]
    [100.0, 100.0, 100.0, 127.78, 138.89]
    """
    # Your code here. Don't change anything above.
    results = []
    base_price = prices[start_index]
    position = starting_money/base_price

    for j in range(len(prices)):
        results.append(position * prices[j])

    i = 0
    while i <= start_index:
        results[i] = 100.0
        i +=1
    
    return results


def moving_average(prices, n):
    """
    Calculates n-period moving average of a list of floats/integers.

    Parameters:
        prices: list of values (ordered in time),
        n: integer moving-average parameter

    Returns:
        list with None for the first n-1 values in prices and the appropriate moving average for the rest

    Example use:
    >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
    >>> [round(m, 2) if m is not None else None for m in ma]
    [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
    >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
    [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
    """
    # Your code here. Don't change anything above.
    ma = []
    for j in range(len(prices)):
        ma.append(sum(prices[(j+1 -n):(j +1)])/n)

    i = 0
    while i < (n-1):
        ma[i] = None
        i +=1
    
    return ma


def compare_mas(ma1, ma2):
    """
    Compare two moving averages.

    Compares values in ma1 and ma2 pairwise to create a list of indicators such that
    - If ma1 > ma2, indicator = 1
    - Otherwise indicator = 0
    - The moving averages may contain None-values in the beginning. If either value is None, the indicator is None

    Parameters:
        ma1 (list): moving average (list of prices)
        ma2 (list): moving average (list of prices)

    Returns:
        list: binary indicators for which moving average value is greater

    Example use:
    >>> p1 = [1, 2, 4, 5]
    >>> p2 = [0, 2.5, 5, 3]
    >>> compare_mas(p1, p2)
    [1, 0, 0, 1]
    >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    >>> p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
    >>> compare_mas(p1, p2)
    [None, None, 1, 1, 1, 0, 0, 0, 1, 1]
    """
    # Your code here. Don't change anything above.
    comp = []
    for i in range(len(ma1)):
        if ma1[i] == None:
            comp.append(None)
        elif ma2[i] == None:
            comp.append(None)
        else:
            if ma1[i] >ma2[i]:
                comp.append(1)
            else:
                comp.append(0)
    
    return comp


def ma_strategy(prices, comparisons, starting_cash=100.0):
    """
    Trade based on moving average crossovers

    Parameters:
        prices: list if stock prices
        comparisons: list of comparisons from compare_mas
        starting_cash (float, optional): Starting cash position, defaults to 100.0.

    Returns:
        list of values of the current position: either cash position or the market value of stock position
    
    We initially hold cash, and buy when we first get a signal to buy.

    More specifically, a change from value 0 to 1 in comparisons signals there's a crossover in moving averages, so we want to buy stock. A move from 1 to 0 signals that we want to sell stock.

    Whenever we trade, we buy with our entire cash position, or sell our entire stock position.
    We will therefore always hold either stock or cash, but never both.
    
    Assume we can hold fractional stock quantities, and there are no transaction fees.

    Example use:
    >>> starting_cash = 1.0
    >>> prices = [2,4,6,5,1]
    >>> cos = [0, 1, 1, 0, 0] # not real indicators, just to illustrate portfolio value when trading
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> values
    [1.0, 1.0, 1.5, 1.25, 1.25]
    >>> starting_cash = 1000.0
    >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    >>> cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
    """
    # Your code here. Don't change anything above.
    cash = []
    ## initalise 
    cash_left = starting_cash
    position = 0
    market_value= 0
    total = cash_left + market_value

    ## define buying , selling and hold
    def buying(cash_left, position, current_price):
        position = cash_left/current_price
        market_value = position * current_price
        cash_left = 0
        new_total = cash_left + market_value
        return  position, market_value, cash_left, new_total

    def selling(cash_left, position, current_price):
        cash_left = position * current_price
        position = 0
        market_value = 0
        new_total = cash_left + market_value
        return position, market_value, cash_left, new_total

    def hold(cash_left, position, current_price):
        market_value = current_price * position
        new_total = cash_left + market_value
        return position, market_value, cash_left, new_total        
    
    #buy or sell, buy = 1, sell= 0 
    buy_sell = []
    for i in range(len(comparisons)- 1):
        if comparisons[i] == None and comparisons[i+1] == None:
            buy_sell.append(None)

        elif comparisons[i] == None and comparisons[i+1] == 1:
            buy_sell.append(None)
        
        elif comparisons[i] == None and comparisons[i+1] == 0:
            buy_sell.append(None)
    

        elif comparisons[i] != None and comparisons[i+1] != None:
            if comparisons[i] != comparisons[i+1]:
                if comparisons[i+1] == 1:
                    buy_sell.append(1)
                else:
                    buy_sell.append(0)
            else:
                buy_sell.append(2)  
         
        
    #run the strategy
    cash.append(total)

    for i in range(len(buy_sell)):
        if buy_sell[i] == None:
            cash.append(total)
        elif buy_sell[i] == 0:
            if position == 0:
                position, market_value, cash_left, total = position, market_value, cash_left, total
                cash.append(total)
            else:
                position, market_value, cash_left, total = selling(cash_left, position, prices[i+1])
                cash.append(total)
        elif buy_sell[i] == 1:
            position, market_value, cash_left, total = buying(cash_left, position, prices[i+1])
            cash.append(total)
        elif buy_sell[i] == 2:
            position, market_value, cash_left, total = hold(cash_left, position, prices[i+1])
            cash.append(total)

    return cash
    

def gallery(visits, option=2):
    """
    Produce summary statistics of gallery visits.

    Parameters:
        visits: list of visits (see also HTML instructions):
            Each visit is a tuple (room number (str), visitor number (str), time (str)) (all elements are integers in string format)
            Each visitor starts outside any room, and they leave all rooms in the end.
            The visits are not necessarily in order.
        option (int, optional): determines what to return, see below
            
    Returns:
        a list containing tuples for each room (sorted in increasing number by room number (1, 2, 3, ...)):
        - if option = 0, (room number, number of unique visitors)
        - if option = 1, (room number, number of unique visitors, average visit time)
        - if option = 2, (room number, number of unique visitors, average visit time, highest total time spent in the room by a single visitor)
        - the average visit time is rounded to integer value.

    Example use:
    >>> visits = [('0', '0', '20'), ('0', '0', '25'), ('1', '1', '74'), ('1', '1', '2')]
    >>> gallery(visits)
    [('0', 1, 5, 5), ('1', 1, 72, 72)]
    >>> gallery(visits, 0)
    [('0', 1), ('1', 1)]
    >>> gallery(visits, 1)
    [('0', 1, 5), ('1', 1, 72)]
    >>> gallery(visits, 1)[0]
    ('0', 1, 5)
    >>> visits = [('15', '3', '61'), ('15', '3', '45'), ('6', '0', '91'), ('10', '4', '76'), ('6', '0', '86'), ('6', '4', '2'), ('10', '1', '47'), ('6', '3', '17'), ('6', '4', '41'), ('15', '3', '36'), ('6', '2', '97'), ('15', '4', '58'), ('6', '0', '16'), ('10', '2', '21'), ('10', '4', '75'), ('6', '0', '76'), ('15', '4', '50'), ('10', '1', '64'), ('6', '3', '3'), ('15', '3', '35'), ('6', '2', '96'), ('10', '2', '35'), ('10', '2', '77'), ('10', '2', '48')]
    >>> gallery(visits)
    [('6', 4, 24, 65), ('10', 3, 15, 43), ('15', 2, 8, 17)]
    """
    # Create a nested dictionary so the input is organised 
    to_dict = {}
    for key, subkey, value in visits:
        to_dict.setdefault(key, {}).setdefault(subkey, []).append(value)
        
    # count the number of unique visitors
    for key_value in to_dict.keys():
        cnt_visitors = 0
        for key, value in to_dict[key_value].items():
            cnt_visitors +=1 
        to_dict[key_value]['no_uniq_vis'] =cnt_visitors
    
    ##standard option 0 result: room number, number of unique visitors
    result = []
    for i in to_dict:
        k = (i, to_dict[i].get(list(to_dict[i])[-1]))
        result.append(k)
        def sorter(item):
            first_ele  = int(item[0])
            return(first_ele)
    result = sorted(result, key =sorter)      
    
    ## option 1 result: room number, number of unique visitors, average visit time

        
    #calculate average visiting time for one room
    for key_value in to_dict.keys():
        times = []
        for key, value in to_dict[key_value].items():
            try:
                if int(key) <= 50:
                    times = times + value
            except:
                pass
        to_dict[key_value]['visting_times'] =times
        to_dict[key_value]['total_vis'] = len(times)/2
        
        
     
    
            
    result_op1 = []
    for i in to_dict:
        sum = 0
        list_times = to_dict[i].get(list(to_dict[i])[-2])
        for j in range(len(list_times)):
            if j %2 == 0:
                sum = sum + abs(int(list_times[j])- int(list_times[j+1]))
        k2 = (i, to_dict[i].get(list(to_dict[i])[-3]), round(sum/to_dict[i].get(list(to_dict[i])[-1])))
        result_op1.append(k2)
    
    result_op1 = sorted(result_op1, key = sorter)         
    
    ## option 2 result: room number, number of unique visitors, average visit time, highest total time spent in the room by a single visitor
    result_op2 = []
    
    for key_value in to_dict.keys():
        time_spent_ind = []
        max_ts = 0
        for key, value in to_dict[key_value].items():
            try:
                if int(key) <= 50:
                    time_spent = 0
                    for n in range(len(value)):
                        if n % 2 == 0:
                            ts = abs(int(value[n])- int(value[n+1]))
                            time_spent += ts
                    time_spent_ind.append(time_spent)
            except:
                pass
        max_ts = max(time_spent_ind)
        to_dict[key_value]['longest_times'] = max_ts
        
   
    for i in to_dict:
        sum = 0
        list_times = to_dict[i].get(list(to_dict[i])[-3])
        for j in range(len(list_times)):
            if j %2 == 0:
                sum = sum + abs(int(list_times[j])- int(list_times[j+1]))
        k3 = (i, to_dict[i].get(list(to_dict[i])[-4]), round(sum/to_dict[i].get(list(to_dict[i])[-2])),to_dict[i].get(list(to_dict[i])[-1]) )
        result_op2.append(k3)    
    
    result_op2 = sorted(result_op2, key = sorter)      


    if option == 0:
        return result

    elif option == 1:
        return result_op1
    
    elif option == 2:
        return result_op2
        
def reverse_engineer(seq):
    """
    Reverse engineer an input sequence
    
    Parameters:
        seq - list of strings
    
    Returns:
        list of values corresponding to each letter present in the sequences (smallest possible values)
        (in alphabetical order)
    
    Example use
    >>> reverse_engineer(["a", "ab", "c", "a", "ab", "ac"])
    [2, 4, 5]
    >>> reverse_engineer(["b", "bc", "ab", "bc", "b", "abc", "b"])
    [3, 1, 2]
    >>> reverse_engineer(["a", "b", "d", "c", "a", "ab"])
    [6, 9, 11, 10]
    >>> reverse_engineer(['c', 'ce', 'd', 'c', 'ce', 'd', 'c', 'a', 'ce', 'cd', 'b', 'ce', 'c', 'd', 'ce', 'c', 'a', 'd', 'ce', 'c', 'cde', 'c', 'b', 'ce', 'd', 'ac', 'ce', 'd', 'c', 'ce', 'cd', 'ce', 'a', 'bc', 'd', 'ce', 'c', 'd', 'ce', 'c', 'cde', 'a', 'c', 'ce', 'df', 'b', 'c', 'ce', 'd', 'c', 'ace', 'cd', 'ce', 'c', 'd', 'ce', 'b', 'c', 'ad', 'ce', 'c'])
    [17, 23, 3, 7, 6, 91]
    """
    # Your code here. Don't change anything above.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    variables = []  
    for ele in seq:
        for char in ele:
            if char not in variables:
                variables.append(char)
    Length = len(sorted(variables))
    first_var = variables[0]

    distance = {}
    distance.setdefault(first_var, {})
    subkey = variables[1:]

    for char in subkey:
        for i in range(len(seq)):
            if len(seq[i]) >1 and first_var in seq[i] and char in seq[i]:
                ind = i
                distance[first_var].setdefault(char, []).append(ind)       
                
    def to_alpha(seq):
        alphabet_only = ""
        for ele in seq:
            for char in ele:
                alphabet_only += char
        return alphabet_only

    def find_ratio(subkey):
        ratio = []
        for char in subkey:
            first_inx =int(distance.get(first_var, {}).get(char)[0]) 
        
            slice_seq = seq[:first_inx+1]
            alpha = to_alpha(slice_seq)
            count_small = 0
            count_current = 0
            for i in alpha:
                if i == first_var:
                    count_small +=1
                elif i == char:
                    count_current +=1
            times = count_small/count_current
            ratio.append(times)
        return ratio

    for i in range(len(subkey)):
        distance[first_var][subkey[i]] = find_ratio(subkey[i])[0]
    i = 1
    numeric= [0] * len(variables)
    numeric[alphabet.index(first_var)] = i


    def test(variables, distance, first_var, i):
        for j in range(1,len(variables)):
            inx = alphabet.index(variables[j])
            test_value = distance.get(first_var, {}).get(variables[j]) * i
            if test_value.is_integer() == False or test_value ==0 :
                i +=1
                numeric[alphabet.index(first_var)] = i
                return test(variables, distance, first_var, i)
            else:
                numeric[inx] = test_value
        return numeric
    
    numeric = test(variables, distance, first_var, i)
    result = [int(item) for item in numeric]
    

    # Still figuring out what could be done to solve the case when there is no clear relationship detected but I run out of time
    # Can I come to your office hours and check with you when I finish?
    # Thank you!

    return result