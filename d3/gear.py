import urllib3

http = urllib3.PoolManager()

resp = http.request('GET', 'https://adventofcode.com/2023/day/3/input',
                    headers={
                        'Cookie': 'session=53616c7465645f5fb1e8527b305b6798d1d77893b2c0e98409f1191ab92ac914fb0ee37d588a14a8469433d14fa414e8d819d5fc2664579fe6ec388a3e525c90'
                    })
        
def is_symbol(char: str):
    if char.isdigit() or char == ".":
        return False
    return True

def spot_qualifies(l1: list, l2: list, l3: list, index: int, width: int):
    max_index = len(l1)
    l1_allows = any( map( is_symbol, l1[max(index-1, 0) : min(index+width+1, max_index)] ) )
    l2_allows = any( map( is_symbol, l2[max(index-1, 0) : min(index+width+1, max_index)] ) )
    l3_allows = any( map( is_symbol, l3[max(index-1, 0) : min(index+width+1, max_index)] ) )
    return l1_allows or l2_allows or l3_allows

def get_number(string: str):
    number = ""
    for char in string:
        if not char.isdigit():
            break
        number += char
    return number

part_numbers = []
data = resp.data.decode('utf-8').split('\n')
max_index = len(data)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        is_digit = char.isdigit()
        is_first_digit = j==0 or not line[j-1].isdigit()
        
        if is_digit and is_first_digit:
            num = get_number(line[j:])
            part_counts = spot_qualifies( data[max(0, i-1)], line, data[min(i+1, max_index)], j, len(num) )
            if part_counts:
                part_numbers.append(int(num))


print(sum(part_numbers))