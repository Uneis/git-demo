import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:/Users/HP/Documents/ass 1 unzip/jobs_in_data.csv')
print(df)
print(df.head(10))
print(df.tail(10))
print("total enties: ", df.shape[0])
print("total attributes: ", df.shape[1])
print("Dataset Information")
print(df.info())
print("/n statistical summary:")
print(df.describe())


counts = df['job_title'].value_counts()
plt.figure(size = (16, 10))
plt.pie(counts, autopct="%1.1f%%")


 


