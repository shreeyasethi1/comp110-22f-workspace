"""Ex04 utils."""
__author__ = "730553668"

def all(input:list[int] , one:int) -> bool:
    i: int = 0
    while i < len(input):
        if input[i] == one:
            i += 1
        else: 
            return False
    return True


def max(input: list[int]) -> int: 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    largest: int = input[i] 
    while i < len(input) - 1: 
        if largest < input[i + 1]:
            largest = input[i + 1]
        else: 
        #elif input[i] > input[i + 1]:
            #largest = input[i]   
            i += 1        
    return largest 

def is_equal(l1: list[int], l2: list[int]) -> bool:
    i: int = 0
    while i < len(l1): 
        if l1[i] == l2[i]:
            i += 1
        else: 
            return False 
    return True