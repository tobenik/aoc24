STRUMBERS = ['zero', 'one', 'two', 'three', 'four', 
             'five', 'six', 'seven', 'eight', 'nine']

def extract_numbers(line):
    numbers = []

    for i in range(len(line)):
        if line[i].isdigit():
            numbers.append(int(line[i]))
            break
        else:
            start_of_strumber = list(map(  line[i:].startswith, STRUMBERS))
            if any( start_of_strumber ):
                numbers.append(start_of_strumber.index(True))
                break

    for i in range(1, len(line)+1):
        if line[-i].isdigit():
            numbers.append(int(line[-i]))
            break
        else:
            start_of_strumber = list(map(  line[-i:].startswith, STRUMBERS))
            if any( start_of_strumber ):
                numbers.append(start_of_strumber.index(True))
                break

    print(numbers)
    return numbers[0] * 10 + numbers[1]

with open('data.txt', 'r') as f:
    data = f.read().splitlines()
    numbers = []
    
    for line in data:
        numbers.append( extract_numbers(line) )
    
    print(numbers)
    print( sum( numbers ) )