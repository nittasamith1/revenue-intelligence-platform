from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def churn_prediction(rfm):
    rfm['Churn'] = rfm['Recency'].apply(lambda x: 1 if x > 90 else 0)

    X = rfm[['Recency','Frequency','Monetary']]
    y = rfm['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    model.fit(X_train,y_train)

    preds = model.predict(X_test)

    print(classification_report(y_test,preds))
    return model