import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def revenue_forecast(df):
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('Month')['Revenue'].sum()
    monthly.index = monthly.index.to_timestamp()

    model = ARIMA(monthly, order=(1,1,1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=3)
    return forecast