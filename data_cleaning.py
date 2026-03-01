import pandas as pd

def clean_data(df):
    df = df.dropna(subset=['Customer ID'])
    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]

    df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate'],
    format="%d-%m-%Y %H:%M"
)
    df['Revenue'] = df['Quantity'] * df['Price']

    df = df.drop_duplicates()
    return df