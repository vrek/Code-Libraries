"""This is a collection of handy math functions"""
import math

def is_prime(number):
    """This tests if a number is prime
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
    Input cost is a float, money_paid is a list, Returns a list
    list is in format[100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]"""
    change = []
    amount_paid = money_paid[0]*100+money_paid[1]*50+money_paid[2]*20+money_paid[3]*10+money_paid[4]*5+money_paid[5]*1\
        +money_paid[6]*0.25+money_paid[7]*0.10+money_paid[8]*0.05+money_paid[9]*0.01
    change_amount = amount_paid - cost
    change [0] = change_amount // 100
    change_amount = change_amount - (change[0]*100)
    change [1] = change_amount // 50
    change_amount = change_amount - (change[1]*50)
    change [2] = change_amount // 20
    change_amount = change_amount - (change[2]*20)
    change [3] = change_amount // 10
    change_amount = change_amount - (change[3]*10)
    change [4] = change_amount // 5
    change_amount = change_amount - (change[4]*5)
    change [5] = change_amount // 1
    change_amount = change_amount - (change[5]*1)
    change [6] = change_amount // 0.25
    change_amount = change_amount - (change[1]*0.25)
    change [7] = change_amount // 0.10
    change_amount = change_amount - (change[1]*0.10)
    change [8] = change_amount // 0.05
    change_amount = change_amount - (change[8]*0.05)
    change [9] = change_amount // 0.01
    change_amount = change_amount - (change[9]*0.01)
    return change
