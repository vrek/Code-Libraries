"""This is a collection of handy math functions"""
import math

def is_prime(number):
    if number > 1:
        for i in range(2, math.floor(math.sqrt(number)+1)):
            if(number % i) == 0:
                return True
        else:
            return False
    else: 
        return False

def calculate_change(cost, amount_paid):
    pass
