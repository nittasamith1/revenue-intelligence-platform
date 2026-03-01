import matplotlib.pyplot as plt

def monthly_revenue_trend(df):
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('Month')['Revenue'].sum()
    
    monthly.plot(figsize=(10,5))
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()