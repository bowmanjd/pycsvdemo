import csv
from pathlib import Path


inpath = Path("sample.csv")

with inpath.open("r", newline="", encoding="utf-8-sig") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        fullname = f"{row['First name']} {row['Middle name']} {row['Last name']}"
        print(fullname)
