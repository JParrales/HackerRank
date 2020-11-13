#!/bin/python3

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        return leap
    else:
        if year % 4 == 0:
            leap = True
                
    return leap

year = int(input())