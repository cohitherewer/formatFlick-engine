import os
import random

import randomstring
import csv


def random_csv(rows, cols, path):
    with open(path, 'w+') as file:
        writer = csv.writer(file)
        headers = [f"Column_{i}" for i in range(1, cols + 1)]
        writer.writerow(headers)
        for x in range(rows):
            row = [randomstring.random_string(random.randint(1, 10)) for _ in range(1, cols + 1)]
            writer.writerow(row)


