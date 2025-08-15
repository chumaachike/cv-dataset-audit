import json
import pathlib
import pandas as pd

p = pathlib.Path("./generated_reports")
p.mkdir(parents=True, exist_ok=True)

def to_json(records, filename, dirpath=p):
    
    filename = str(filename)
    if not filename.lower().endswith(".json"):
        filename += ".json"
        print(f"Note: '.json' extension added. The file will be saved as {filename}")

    filepath = pathlib.Path(dirpath) / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)

    
    with filepath.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False, default=str)



def to_csv(records, filename, dirpath=p):
    if not filename.endswith(".csv"):
            filename += ".csv"
            print(f"Warning: .json extension added to the file name. The file will be saved as {filename}")
    filepath = pathlib.Path(dirpath) / filename
    pd.DataFrame(records).to_csv(filepath, index=False)
    
    
