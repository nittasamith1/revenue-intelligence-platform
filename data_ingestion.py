import pandas as pd
from config import DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH, encoding='ISO-8859-1')
    return df