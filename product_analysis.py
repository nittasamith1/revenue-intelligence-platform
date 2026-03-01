def top_products(df, n=10):
    top = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(n)
    return top