import os

import randomcsv
import randomjson
from src.formatflick.formatflick import formatflick as ffe
import time
import matplotlib.pyplot as plt
import numpy as np

destination = os.path.join(os.getcwd(), "profiler", "random_files")


def get_custom_path(_path):
    return os.path.join(destination, _path)


def csv_to_json_profiler():
    total_rows = 10
    total_cols = 10
    timing_data = np.zeros((total_rows, total_cols))
    for rows in range(1, total_rows + 1):
        for cols in range(1, total_cols + 1):
            count = 10
            temp = []
            while count > 0:
                source_path = get_custom_path("randomcsv.csv")
                randomcsv.random_csv(rows, cols, source_path)
                dest_path = get_custom_path("randomresult.json")
                obj = ffe(source_path, dest_path)
                start_time = time.time_ns()
                obj.convert()
                end_time = time.time_ns()
                count -= 1
                temp.append(end_time - start_time)
            temp.sort()
            std_time = temp[5]
            timing_data[rows - 1, cols - 1] = std_time
    rows, cols = np.meshgrid(np.arange(1, total_rows + 1), np.arange(1, total_cols + 1))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surface = ax.plot_surface(rows, cols, timing_data, cmap='viridis')
    fig.colorbar(surface)

    # Set axis labels
    ax.set_xlabel('Rows')
    ax.set_ylabel('Cols')
    ax.set_zlabel('Execution Time (ms)')

    plt.show()


def json_profiles():
    pass
    # total_rows, total_depth, total_max_children = 10, 10, 10



if __name__ == "__main__":
    csv_to_json_profiler()
