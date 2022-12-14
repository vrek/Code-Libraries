"""This is a collection of handy math functions"""
import math

def is_prime(number):
    """This tests if a number is prim 
    Output is boolean, True if number is prime False if it is not
    """
    if isinstance(number) is not int:
        raise TypeError("The input to this method must be a int")
    if number > 1:
        if number == 2:
            return True
        for i in range(2, math.floor(math.sqrt(number)+1)):
            if (number % i) == 0:
                return False
            return True
    return False


def calculate_change(cost, money_paid):
    """Returns the amount of change from a purchase
    Input is a list, Returns a list
    list is in format[100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]"""
    amount_paid = money_paid[0]*100+money_paid[1]*50+money_paid[2]*20+money_paid[3]*10+money_paid[4]*5+money_paid[5]*1\
        +money_paid[6]*0.25+money_paid[7]*0.10+money_paid[8]*0.05+money_paid[9]*0.01
    change = amount_paid - cost
    return change
