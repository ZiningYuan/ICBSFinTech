from token import RIGHTSHIFT


def recursive_fibonacci(n):
    """
    Assumes that n is an int >= 0
        returns Fibonacci of n
    
    Example use:
    >>> recursive_fibonacci(2)
    1
    >>> recursive_fibonacci(5)
    5
    >>> recursive_fibonacci(8)
    21
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def merge_sort(L):
    """
    Sort the input list using the merge sort algorithm.
    
    Parameters:
        L is an unsorted list
        
    Returns:
        L sorted in increasing order
    
    Examples:
    >>> merge_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> merge_sort([1, 13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if len(L) <2:
        return L[:]
    else:
        middle = len(L)//2
        left = L[:middle]
        right = L[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists into one
    
    Parameters: 
        left and right are sorted lists
    
    Returns a single sorted list.
    
    Example use:
    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    # YOUR CODE BELOW
    # DON'T CHANGE ANYTHING ABOVE
    result = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i == len(left):
        while j < len(right):
            result.append(right[j])
            j+=1
    else:
        while i < len(left):
            result.append(left[i]) 
            i +=1   
    return result


    

def check_sorted(L):
    """
    Uses looping to check whether a list is sorted or not (could be increasing or decreasing).
    Examples:
    >>> check_sorted([3, 6, 48, 24, 51, 262, 119])
    False
    >>> check_sorted([748, 623, 424, 414, 74, 2])
    True
    >>> check_sorted([1, 2, 3])
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    i = 0 
    if L[i] <= L[i+1]:
        while i < len(L)-1:
            if L[i] <= L[i+1]:
                i +=1
                continue
            else:
                return False
    else:
         while i < len(L)-1:
            if L[i] >= L[i+1]:
                i +=1
                continue
            else:
                return False       
    return True


def longest_sorted(L):
    """
    Uses looping to return the longest sorted sequence in a list (ascending).
    Examples:
    >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
    [1, 9, 13, 15]
    >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
    [8, 20, 38, 43, 85]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    
    return ...