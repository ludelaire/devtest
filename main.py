# HEADER

import datetime
from random import randint
import pandas as pd
from collections import defaultdict, Counter
import time


class Elevator:
    def __init__(self, name, current_floor, call, db_floor, passenger_floor):
        self.name = name
        self.current_floor = current_floor
        self.call = call
        self.db_floor = db_floor
        self.passenger_floor = passenger_floor

    def __str__(self):
        return f'Elevator {self.name} is currently on floor {self.current_floor}'


def generate_db():
    epochs = [randint(1639486363, 1642202527) for x in range(1000)]
    epochs.sort()
    timestamps = [datetime.datetime.fromtimestamp(x) for x in epochs]
    floor_requested = [randint(1, 10) for x in range(1000)]
    data = {'Timestamp': timestamps, 'Floor_requested': floor_requested}
    database = pd.DataFrame(data)
    return database


def most_demanded_floors(database):
    hours = [database.Timestamp[x].hour for x in range(len(database.Timestamp))]
    floors = [database.Floor_requested[x] for x in range(len(database.Floor_requested))]
    floor_counts_per_hour = defaultdict(Counter)
    for hour, floor in zip(hours, floors):
        floor_counts_per_hour[hour][floor] += 1
    mcf_per_hour_with_counts = {}  # Most common floor per hour dictionary, w/ occurrence counts per floor
    for hour, counts in floor_counts_per_hour.items():
        most_common = counts.most_common(1)
        mcf_per_hour_with_counts[hour] = most_common
    '''final = {}
    for k, v in mcf_per_hour_with_counts.items():
        values = v[0][0]
        final[k] = values
    print(values)'''
    extracted_mcfloors = [i[0][0] for i in mcf_per_hour_with_counts.values()]
    mcf_per_hour = dict(zip(mcf_per_hour_with_counts.keys(), extracted_mcfloors))
    return mcf_per_hour
    # mcf_per_hour is the final relational db of the most popular floor per each registered hour, only ints


def move_to_passenger_floor(passenger_floor):
    print('You are currently in floor ' + passenger)


def move_to_db_floor(db_floor):
    pass


if __name__ == '__main__':
    db = generate_db()
    # pd.set_option('display.max_rows', None) -- to see full dataframe after print is used
    mcf_x_hour = most_demanded_floors(db)
