import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.extract import extract_function
import pandas as pd

def transform_function():
    df = extract_function()
    df["RESTAURANTOPENDATE"] = pd.to_datetime(df["RESTAURANTOPENDATE"], errors="coerce")
    df[["NAME", "ADDRESS1", "ADDRESS2", "CITY", "STATE", "POSTALCODE", "PHONENUMBER", "GEOCODESTATUS", "PERMITID"]].astype(str)
    return df
