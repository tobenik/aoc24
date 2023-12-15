
def extract_number(text):
    numbers = []
    for char in text:
        try:
            numbers.append(int(char))
        except ValueError:
            pass
    return numbers[0] * 10 + numbers[-1]
        

with open('data.txt', 'r') as f:
    data = f.read()
    numbers = []
    for line in data.split('\n'):
        numbers.append(extract_number(line))
    print( sum(numbers) )
