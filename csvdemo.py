"""Python CSV handling demo."""

__version__ = "0.1.0"

import argparse
import csv
import sys
from pathlib import Path


def transform(
    infilename, outfilename, inencoding="utf-8-sig", outencoding="utf-8-sig",
):
    """Filters and transforms each row, with output to a separate file."""
    inpath = Path(infilename)
    outpath = Path(outfilename)
    args = {"newline": ""}
    inargs = {"encoding": inencoding, **args}
    outargs = {"encoding": outencoding, **args}
    with inpath.open("r", **inargs) as infile, outpath.open("w", **outargs) as outfile:
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


def run(args=None):
    """Execute as command line script."""
    if not args:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "inputfile", help="read from this CSV file",
    )
    parser.add_argument(
        "outputfile", help="save to this CSV file",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        default="utf-8-sig",
        help="character encoding of input and output files",
    )
    parser.add_argument(
        "-ie", "--inputencoding", help="character encoding of input file",
    )
    parser.add_argument(
        "-oe", "--outputencoding", help="character encoding to use for output file",
    )
    args = parser.parse_args(args)

    inputencoding = args.inputencoding or args.encoding
    outputencoding = args.outputencoding or args.encoding

    transform(args.inputfile, args.outputfile, inputencoding, outputencoding)


if __name__ == "__main__":
    run()
