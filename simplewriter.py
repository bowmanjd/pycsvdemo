import csv
from pathlib import Path


outpath = Path("out/output.csv")
outpath.parent.mkdir(exist_ok=True)  # ensure the "out" directory exists

with outpath.open("w", newline="", encoding="utf-8-sig") as outfile:
    writer = csv.DictWriter(outfile, ["First", "Last"])
    writer.writeheader()
    new_row = {"First": "Jane", "Last": "Smith"}
    writer.writerow(new_row)
