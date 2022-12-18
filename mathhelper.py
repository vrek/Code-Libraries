"""This is a collection of handy math functions"""
import math

def is_prime(number):
    """This tests if a number is prime
       Output is boolean, True if number is prime False if it is not
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("The input to this method must be a int")
    if number > 1:
        if number == 2:
            return True
        if number >2 and number % 2 == 0:
            return False
        max_divisor = math.floor(math.sqrt(number))
        for i in range(3, max_divisor+1, 2):
            if (number % i) == 0:
                return False
        return True
    return False


def calculate_change(cost, money_paid):
    """Returns the amount of change from a purchase
    Input cost is a float, money_paid is a list, Returns a list
    list is in format[100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]"""
    change = []
    change_list = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    amount_paid = sum([money_paid[i]*change_list for i, change_type in enumerate(change_list)])
    change_amount = amount_paid - cost
    for i, change_type in enumerate(change_list):
        change += change_amount // change_type
        change_amount -= change[i] * change_type
    return change

def list_primes(max_value):
    """Returns a list of prime number upto the max_value"""
    if isinstance(max_value, bool) or not isinstance(max_value, int):
        raise TypeError("The input to this method must be a int")
    number = 2
    prime_list = []
    while number <= max_value:
        if is_prime(number):
            prime_list.append(number)
        number += 1
    return prime_list

def count_primes(min_value, max_value):
    """Returns an int of the number of primes between min_value and max_value"""
    if isinstance(max_value, bool) or not isinstance(max_value, int):
        raise TypeError("The input to this method must be a int")
    if isinstance(min_value, bool) or not isinstance(min_value, int):
        raise TypeError("The input to this method must be a int")
    guess = 2
    prime_count = 0
    for guess in range(min_value, max_value):
        if is_prime(guess):
            prime_count += 1
    return prime_count
