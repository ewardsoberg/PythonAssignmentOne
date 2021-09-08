import math
from functools import reduce
import time


# 1.	Write a Python function to calculate the sum of a list of numbers.

test_list = [55, 878, 596, 601, 170, 624, 904, 988, 98, 529, 646, 692, 556, 127, 794, 488]


def sum_list(int_list) -> list:  # Takes a list of integers and return the total sum of the list
    if type(int_list) != list:
        raise TypeError('Must be of type list with integers or floats')
    for x in int_list:
        if type(x) not in [int, float]:
            raise TypeError('List is not only integers or floats')
    return sum(int_list)


sum_list_lambda = lambda a_list: (reduce(lambda a, b: a + b, a_list))  # Same as function sum_list(), but with lambda

print(f'Result of function sum_list: {sum_list(test_list)}')
print(f'Result of function sum_list_lambda: {sum_list_lambda(test_list)}')

# 2.	Write a Python function to convert an Integer to a string in any base


def int_to_str(x):
    if type(x) not in [int, float]:
        raise TypeError('Please insert a int or float')
    return str(x)


int_to_str_lambda = lambda x: str(x)  # Same as function int_to_str(), but with lambda

print(f'Result of function int_to_str: {int_to_str(8)}, {type(int_to_str(8))}')
print(f'Result of function int_to_str_lambda: {int_to_str_lambda(8)}, {type(int_to_str_lambda(8))}')

# 3.	Write a Python function of to recursively calculate the sum

test_list_2 = [1, 2, [3, 4], [5, 6]]


def sum_recur(x):  # Takes a list of integers and return the total sum of the list using recursion
    total = 0
    for item in x:
        try:
            total += item
        except TypeError:
            total += sum_recur(item)
    return total


sum_recur_lambda = lambda x: sum(map(sum_recur_lambda, x))\
                   if isinstance(x, list) else x  # Same as function sum_list(), but with lambda


print(f'Result of function sum_recur: {sum_recur(test_list_2)}')
print(f'Result of function sum_recur_lambda: {sum_recur_lambda(test_list_2)}')

# 5.	Write a Python function to solve the Fibonacci sequence using recursion


def recur_fib(n):  # Fibonacci using recursion, to run a sequence of 40 takes 37.842175006866455 seconds.....
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


def generator_fib(n):  # Fibonacci using generator, to run a sequence of 40 takes 0.0 seconds.
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


lambda_fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                              range(n-2), [0, 1])  # Fibonacci using lambda, to run a sequence of 40 takes 0.0 seconds.

start1 = time.time()
for i in range(30):
    recur_fib(i)
last_number_rec = recur_fib(29)
end1 = time.time()
total_rec = (end1-start1)
print(f'Last number in seq of 30 in recur_fib() is: {last_number_rec} and took: {total_rec} seconds')

start2 = time.time()
last_number_gen = list(generator_fib(30))
end2 = time.time()
total_gen = (end2-start2)
print(f'Last number in seq of 30 in generator_fib() is: {last_number_gen[-1]} and took: {total_gen} seconds')


# 6.	Write a Python function to get the sum of a non-negative integer.

test_num = 345


def sum_of_int(num):  # Loops trough a str(number), for every x in number adds int(x) to the total sum.
    total = sum(int(digit) for digit in str(num))
    return total


sum_int_lambda = lambda num: sum(int(digit) for digit in str(num)) # Same as function sum_of_int(), but with lambda


print(f'Total sum of {test_num} is: {sum_of_int(test_num)}')

# 11.	Write a Python function to find the greatest common divisor (gcd) of two integers.


def g_c_d(x, y):  # Uses the inbuilt gcd function in the math module to return the greatest common divisor of x, y
    return math.gcd(x, y)


g_c_d_lambda = lambda x, y: math.gcd(x, y)  # Same as function c_g_d(), but with lambda


print(f'Result of function g_c_d: {g_c_d(10, 20)}')
print(f'Result of function g_c_d_lambda: {g_c_d_lambda(10, 20)}')
