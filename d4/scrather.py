
def calculatePoints(w: list, d: list):
    points = 1
    for num in w:
        if num in d: 
            points *= 2
    return points // 2

with open('data.txt') as f:
    data = f.readlines()
    totalPoints = 0
    for scratcher in data:
        _, numbers = scratcher.split(':')
        winners, drawn = numbers.split('|')
        totalPoints += calculatePoints(winners.split(), drawn.split())
    print(totalPoints)
        
