def calculatePoints(w: list, d: list):
    points = 0
    for num in w:
        if num in d: 
            points += 1
    return points

with open('data.txt') as f:
    points = {}
    for i, scratcher in enumerate(f.readlines()):
        _, numbers = scratcher.split(':')
        winners, drawn = numbers.split('|')
        points[i+1] = [1, calculatePoints(winners.split(), drawn.split())]
    print(points, end="\n\n")
    for i in range(1, max(list(points.keys())) + 1):
        for j in range(i + 1, i + points[i][1] + 1):
            points[j][0] += points[i][0]
    print(points)
    print(sum(list(map(lambda x: x[0], points.values()))))
