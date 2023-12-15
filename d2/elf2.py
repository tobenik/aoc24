import urllib3
import math

http = urllib3.PoolManager()

resp = http.request('GET', 'https://adventofcode.com/2023/day/2/input',
                    headers={'Cookie': 'session=53616c7465645f5fb1e8527b305b6798d1d77893b2c0e98409f1191ab92ac914fb0ee37d588a14a8469433d14fa414e8d819d5fc2664579fe6ec388a3e525c90'})

powers = []

for line in resp.data.decode('utf-8').split('\n'):
    if line:
        _, game_data = line.split(':')
        draws = list(map(str.strip, game_data.replace(';', ',').split(',')))
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for draw in draws:
            number, color = draw.split(' ')
            if minimums[color] < int(number):
                minimums[color] = int(number)
        powers.append(math.prod(list(minimums.values())))
            
print(sum(powers))