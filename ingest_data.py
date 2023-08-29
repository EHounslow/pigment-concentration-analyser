import pandas as pd

def ingest_data(input_file):
    return pd.read_csv(input_file, header = 10)