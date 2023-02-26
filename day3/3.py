#First part, takes the data file given from the AOC site and then splitsi and strips the file 
#of its extra components into a single list with each string in an index.
import requests
from typing import List
import json

headers = {
    'cookie': 'session=53616c7465645f5fb6650b7a7797453d6ab65881f84067c512d4764eb835a13e17de8bbd5ab3b013a88b59e97bd91eeed063140bab6a770528c5549259ae6c58'
}
x = requests.get('https://adventofcode.com/2022/day/3/input', headers=headers)
text = str(x.text)
data = text.strip().split('\n')


def let_to_num(letter:str) -> int:
    num = ord(letter)
    if num >= ord('A') and num<= ord('Z'):
        return num - ord('A') + 27
    elif num >= ord('a') and num <= ord('z'):
        return num - ord('a') + 1
    else: 
        raise Exception()

#Part 1    
def compare(str1:str, str2:str) -> str:
    for i in str1:
        for j in str2:
            if i == j:
                return i
    raise Exception()

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
print(f'Priority is {priority}')

#Part2 
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

#print(json.dumps(list(divide_chunks(data, 3))))

def compare3(str1:str, str2:str, str3:str) -> str:
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