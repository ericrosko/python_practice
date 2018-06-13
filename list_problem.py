#!/usr/bin/env python3

'''
Author:     Eric Rosko
Date:       June 11, 2018
Description:
File: list_problem.py

'''

import sys # allows me to get command line arguments

def find_largest_with_nested_lists(*items):
    # print("items", items, type(items))
    largest = None
    current = None
    for item in items:
        print("IN LOOP", item, type(item))
        if type(item) is tuple:
            current = find_largest_with_nested_lists(*item)
        else:
            current = item

        if largest is None or largest < current:
            largest = current

    return largest


def find_largest(*items):
    largest = None

    for item in items:
        if type(item) is list:
            sorted_list = sorted(item)
            current = sorted_list[-1]
        else:
            current = item

        if largest is None:
            largest = current
        elif largest < current:
            largest = current

    return largest


if __name__ == "__main__":
    pass
