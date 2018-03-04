from random import uniform
from time import sleep

small_timeout_lower = 2
small_timeout_upper = 3

big_timeout_lower = 6
big_timeout_upper = 7

page_timeout = 10;

def small_timeout():
    sleep(uniform(small_timeout_lower, small_timeout_upper))

def big_timeout():
    sleep(uniform(big_timeout_lower, big_timeout_upper))

def page_timeout():
    return page_timeout