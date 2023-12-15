import urllib3
http = urllib3.PoolManager()
resp = http.request('GET', 'https://adventofcode.com/2023/day/3/input',
                    headers={
                        'Cookie': 'session=53616c7465645f5fb1e8527b305b6798d1d77893b2c0e98409f1191ab92ac914fb0ee37d588a14a8469433d14fa414e8d819d5fc2664579fe6ec388a3e525c90'
                    })
data = resp.data.decode('utf-8').split('\n')

import math

# Given a string and an index returns number(s) touching index
def get_numbers(string: str, index: int):
    numbers = []
    curr_index = index
    if string[curr_index].isdigit():
        number = ""
        # Get intial and left side
        while curr_index >= 0 and string[curr_index].isdigit():
            number = string[curr_index] + number
            curr_index -= 1
        curr_index = index + 1
        # Get right side
        while curr_index <= len(string) and string[curr_index].isdigit():
            number += string[curr_index]
            curr_index += 1
        numbers.append(int(number))
    else:
        left_index = index - 1
        right_index = index + 1
        
        left_number = ""
        # Get intial and left side
        while left_index >= 0 and string[left_index].isdigit():
            left_number = string[left_index] + left_number
            left_index -= 1
        if left_number: numbers.append(int(left_number))
    
        right_number = ""
        # Get intial and right side
        while right_index < len(string) and string[right_index].isdigit():
            right_number += string[right_index]
            right_index += 1
        if right_number: numbers.append(int(right_number))

    return numbers

gear_indices = []

for line in data:
    if line:
        gear_indices.append( [i for i, sym in enumerate(line) if sym == "*"] )


max_row_index = len(data) - 1
max_column_index = len(data[0]) - 1
gear_ratios = []

for i, line in enumerate(gear_indices):
    for gear in line:
        parts_in_contact = []
        
        if i > 0:
            parts_above = get_numbers(data[i-1], gear)
            [parts_in_contact.append(part) for part in parts_above]
        if i < max_row_index:
            parts_below = get_numbers(data[i+1], gear)
            [parts_in_contact.append(part) for part in parts_below]
        if gear > 0 and data[i][gear-1].isdigit():
            parts_left = get_numbers(data[i], gear - 1)
            [parts_in_contact.append(part) for part in parts_left]
        if gear < max_column_index and data[i][gear+1].isdigit():
            parts_right = get_numbers(data[i], gear + 1)
            print(parts_right)
            [parts_in_contact.append(part) for part in parts_right]
        
        if len(parts_in_contact) == 2:
            gear_ratios.append(math.prod(parts_in_contact))

print(sum(gear_ratios))
        