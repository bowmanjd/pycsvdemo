"""Python CSV handling demo."""

__version__ = "0.1.0"

import csv
from pathlib import Path


def transform():
    """Filters and transforms each row, with output to a separate file."""
    inpath = Path("sample.csv")
    outpath = Path("out/transformed.csv")
    args = {"newline": "", "encoding": "utf-8"}
    with inpath.open("r", **args) as infile, outpath.open("w", **args) as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, ["Firstname", "Lastname", "Username"])

        writer.writeheader()

        for row in reader:
            if row["Role"] == "Student":
                new_row = {
                    "Firstname": row["First name"],
                    "Lastname": row["Last name"],
                    "Username": f"{row['Last name']}{row['First name']}".lower(),
                }
                writer.writerow(new_row)


if __name__ == "__main__":
    transform()
