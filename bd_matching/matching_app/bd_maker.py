from . import models
from pathlib import Path
import os
import csv

BASE_DIR = Path(__file__).resolve().parent.parent

def store_data(path):
    with open(path, "r") as f:
        reader =csv.reader(f)
        first_row = True
        for row in reader:
            if first_row:
                first_row=False
                continue
            bg = models.BoardGame(title = row[0])
            bg.strategy = int(row[1])
            bg.party = int(row[2])
            bg.secret = int(row[3])
            bg.token = int(row[4])
            bg.adventure = int(row[5])
            bg.max_p = int(row[6])
            bg.min_p = int(row[7])
            bg.save()

def check_data():
    data = models.BoardGame.objects.all()
    print(f"size : {len(data)}")
    for i in data:
        print(i.title)

def db_clear():
    data = models.BoardGame.objects.all()
    for i in data:
        i.delete()

def main():
    db_clear()
    store_data(os.path.join(BASE_DIR, "database/bg_datas.csv"), )
    check_data()

if __name__ == "__main__":
    main()