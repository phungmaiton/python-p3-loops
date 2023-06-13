#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i = i - 1

    print("Happy New Year!")


def square_integers(int_list):
    squared_list = list()
    for int in int_list:
        squared = int * int
        squared_list.append(squared)
    return squared_list


def fizzbuzz():
    i = 0
    while i < 100:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
