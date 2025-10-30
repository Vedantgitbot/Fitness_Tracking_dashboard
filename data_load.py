import pandas as pd

def load_raw_data(filepath):
    
    df = pd.read_csv(filepath, sep=',', header=None)
    print(f" Loaded raw data: {df.shape[0]} rows")
    return df


data = load_raw_data("Data/Activity.csv")  

