# main.py
from pathlib import Path
import pandas as pd
import json
import argparse
from scan import scan
from utils import to_json, to_csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rootdir", type=Path, required=True)
    parser.add_argument("--json")
    parser.add_argument("--csv")
    args = parser.parse_args()
    records = scan(args.rootdir)
    
    if args.json:
        to_json(records, args.json)
    if args.csv:
        to_csv(records, args.csv)
    if not args.json and not args.csv:
        print(f"Scanned {len(records)} records. Use --json/--csv to save a report.")


if __name__ == "__main__":
    main()
