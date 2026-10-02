# Task 04 Sales Prediction - Vedika Jadhav
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {'TV':[230,44,17,151,180], 'Sales':[22,10,9,18,12]}
df = pd.DataFrame(data)
X = df[['TV']]
y = df['Sales']
model = LinearRegression()
model.fit(X,y)
pred = model.predict([[100]])
print(f"Predicted Sales: {pred[0]:.2f}")
