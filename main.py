# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
from random import randint
import pandas as pd


def generate_db():
    epochs = [randint(1639486363, 1642202527) for x in range(100)]
    epochs.sort()
    timestamps = [datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in epochs]
    floor_requested = [randint(1, 10) for x in range(100)]
    data = {'Timestamp': timestamps, 'Floor requested': floor_requested}
    db = pd.DataFrame(data)
    return db


if __name__ == '__main__':
    db = generate_db()
    print(db)
