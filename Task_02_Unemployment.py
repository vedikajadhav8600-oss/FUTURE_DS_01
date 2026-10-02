# Task 02 Unemployment Analysis - Vedika
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url="https://raw.githubusercontent.com/jainvidit/Covid-19-India/master/Data/Unemployment_in_India.csv"
# For demo we use sample data
data={'Region':['North','South','East','West','Central'],'Unemployment_Rate':[6.5,5.2,7.8,4.9,8.1]}
df=pd.DataFrame(data)
print(df.head())
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Unemployment_Rate', data=df, palette='viridis')
plt.title('Unemployment Rate by Region - India')
plt.savefig('unemployment.png')
print("Plot saved - Task 2 Completed")
