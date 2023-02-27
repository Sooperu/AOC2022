import json
from typing import List
import shared
#Imports a method that pulls the text data from the AOC site
org_list = shared.get_day(4)

#Part 1
count = 0
def is_it_in(l_one:int, l_two:int, r_one:int, r_two:int) -> bool:
    """Checks if the numbers in the ranges are contained in the other range
    """
    if l_one <= r_one and l_two >= r_one and l_one <= r_two and l_two >= r_two:
        return True
    return False

for i in org_list:
    l,r = i.split(',')
    l_one, l_two = map(int, l.split("-"))
    r_one, r_two = map(int, r.split("-"))
    if is_it_in(l_one, l_two, r_one, r_two):
        count += 1
    elif is_it_in(r_one, r_two, l_one, l_two): #Flips the input around so we can check if the other way
        count += 1
print(f'The fully amount of contained assignments is {count}.')


#Part 2
def is_it_somewhat_in(l_one:int, l_two:int, r_one:int, r_two:int) -> bool:
    """Changes the method in the first part to check if ANY of the edges of the range are contained
    in another"""
    if l_one <= r_one and l_two >= r_one or l_one <= r_two and l_two >= r_two:
        return True
    return False

count = 0
for i in org_list:
    l,r = i.split(',')
    l_one, l_two = map(int, l.split("-"))
    r_one, r_two = map(int, r.split("-"))
    if is_it_somewhat_in(l_one, l_two, r_one, r_two):
        count += 1
    elif is_it_somewhat_in(r_one, r_two, l_one, l_two): #Flips the input around so we can check if the other way
        count += 1
print(f'The somewhatin amount of contained assignments is {count}.')