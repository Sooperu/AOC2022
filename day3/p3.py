#First part, takes the data file given from the AOC site and then splitsi and strips the file 
#of its extra components into a single list with each string in an index.
import requests
from typing import List
import json
import os

a = os.environ['AOC']
headers = {
    'cookie': f'session={a}'
}
x = requests.get('https://adventofcode.com/2022/day/3/input', headers=headers)
text = str(x.text)
data = text.strip().split('\n')

def let_to_num(letter:str) -> int:
    """ Creating functions that does the what the problem is asking 
    let_to_num takes in a character and turns that into a number"""
    num = ord(letter)
    if num >= ord('A') and num<= ord('Z'):
        return num - ord('A') + 27
    elif num >= ord('a') and num <= ord('z'):
        return num - ord('a') + 1
    else: 
        raise Exception()

def compare(str1:str, str2:str) -> str:
    """Part 1, compare twos strings together 
    returns the character that they matched on"""
    for i in str1:
        for j in str2:
            if i == j:
                return i
    raise Exception()

#This for loop compares and sums the priority of the individual character
priority = 0 
for d in data:
    length = len(d)
    half_length = int(length/2)
    first_half = ''
    second_half = ''
    i = 0
    while i < length:
        if i < half_length:
            first_half += d[i]
            i += 1
        elif i >= half_length:
            second_half += d[i]
            i += 1
        else:
            raise Exception('invald')
    priority += let_to_num(compare(first_half,second_half))
print(f'Priority is {priority}.')


def divide_chunks(l:List[str], n:int) -> List[List[str]]:
    """Takes in a list and divides it into chunks of n"""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def compare3(str1:str, str2:str, str3:str) -> str:
    """Part 2, compares 3 strings together and returns the character
    that is matched in all 3"""
    for i in str1:
        for j in str2:
            for k in str3:
                if i == j and i == k:
                    return i
    raise Exception()

group3 = divide_chunks(data, 3)
newprior = 0
for i in group3:
    a,b,c = i
    newprior += let_to_num(compare3(a,b,c))
print(f'New priority is {newprior}.') 