import pandas as pd
import datetime as dt

def rfm_analysis(df):
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

    rfm = df.groupby('Customer ID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'Invoice': 'nunique',
        'Revenue': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']

    rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1,2,3,4])
    rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4])

    rfm['RFM_Score'] = rfm[['R_score','F_score','M_score']].sum(axis=1)

    return rfm