#!/usr/bin/env python3
"""
profiling to find bottleneck
tìm nút thắt cổ chai
sử dụng cProfile

sử dụng 

"""
import cProfile
import random
import math
import sys
import functools
import tempfile
import pstats

def cprofile_me(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        file = tempfile.mktemp()
        profiler = cProfile.Profile()
        profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(file)
        metrics = pstats.Stats(file)
        metrics.strip_dirs().sort_stats('time').print_stats(100)
    return wraps

@cprofile_me
def run_function(function, numbers):
    for number in numbers:
        function(number)


def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True


def is_prime_sqrt(number):
    if number < 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for value in range(2, max_range):
        if number % value == 0:
            return False
    return True


def is_prime_optimal(number):
    if number in [2, 3, 5]:
        return True
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number < 2: 
        return False
    if number < 49:
        return True
    if (number %  7) == 0 or (number % 11) == 0 or (number % 13) == 0 or (number % 17) == 0 or \
       (number % 19) == 0 or (number % 23) == 0 or (number % 29) == 0 or (number % 31) == 0 or \
       (number % 37) == 0 or (number % 41) == 0 or (number % 43) == 0 or (number % 47) == 0:
        return False
    
    if number < 2809:
        return True
    
    max_range = int(math.sqrt(number)) + 1
    for value in range(53, max_range, 2):
        if number % value == 0:
            return False
    return True


if __name__ == "__main__":
    numbers = [80909548, 64284912, 32561271, 59635875, 43704113, 42511163, 7564624, 62719360, 29119365, 49141585]
    run_function(is_prime_basic, numbers)
    run_function(is_prime_sqrt, numbers)
    run_function(is_prime_optimal, numbers)
