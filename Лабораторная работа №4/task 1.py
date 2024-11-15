import json

# TODO решите задачу

def task() -> float:
    sum = 0
    with open('input.json', 'r') as file:
        data = json.load(file)
        for elem in data:
            sum += elem['score'] * elem['weight']
    return round(sum, 3)


print(task())
