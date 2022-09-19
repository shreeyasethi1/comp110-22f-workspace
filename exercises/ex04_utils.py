"""Ex04 utils."""

__author__ = "730553668"


def all(input:list[int] , one:int) -> bool: 
    """all numbers in the list should be the same as the inputed number.""" 
    i: int = 0
    if len(input) == 0: 
        return False
    while i < len(input): 
        if input[i] == one: 
            i += 1
        else:  
            return False
    return True


def max(input: list[int]) -> int: 
    """selecting the greatest number in the list."""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    largest: int = input[i] 
    while i < len(input) - 1:  
        if largest < input[i + 1]: 
            largest = input[i + 1]
        else:    
            i += 1        
    return largest 


def is_equal(l1: list[int], l2: list[int]) -> bool:  
    """checking that the two lists inputed are the exact same."""
    i: int = 0
    if len(l1) == 0 or len(l2) == 0: 
        return False
    while i < len(l1):  
        if l1[i] == l2[i]: 
            i += 1
        else:  
            return False 
    return True