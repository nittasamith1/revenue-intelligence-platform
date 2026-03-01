from src.data_ingestion import load_data
from src.data_cleaning import clean_data
from src.eda import monthly_revenue_trend
from src.rfm_analysis import rfm_analysis
from src.product_analysis import top_products
from src.forecasting import revenue_forecast
from src.churn_model import churn_prediction

def main():
    df = load_data()
    df = clean_data(df)

    print("Running EDA...")
    monthly_revenue_trend(df)

    print("Running RFM...")
    rfm = rfm_analysis(df)

    print("Top Products:")
    print(top_products(df))

    print("Revenue Forecast:")
    print(revenue_forecast(df))

    print("Churn Model:")
    churn_prediction(rfm)

if __name__ == "__main__":
    main()