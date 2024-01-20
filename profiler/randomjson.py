import json
import random

import randomstring


def random_json_util(depth=3, max_children=3):
    if depth <= 0:
        return randomstring.random_string(random.randint(1, 10))
    result = {}
    for _ in range(random.randint(1, max_children)):
        key = randomstring.random_string(random.randint(1, 10))
        value = random_json_util(depth - 1, max_children)
        if random.choice([True, False]):
            result[key] = value
        else:
            result[key] = [value]
    return result


def random_json(rows, depth, max_children, path):
    data = []
    for _ in range(rows):
        random_row = random_json_util(depth, max_children)
        data.append(random_row)
    json_string = json.dumps(data)
    with open(path, 'w+') as json_file:
        json_file.write(json_string)
