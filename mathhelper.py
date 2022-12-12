"""This is a collection of handy math functions"""
import math

def is_prime(number):
    if number > 1:
        for i in range(2, math.floor(math.sqrt(number)+1)):
            if(number % i) == 0:
                return False
        else:
            return True
    return False

def calculate_change(cost, amount_paid):  
    change = amount_paid - cost
