#scatter plot ile görselleştirme
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('C:/Users/90531/Desktop/Detail_Change1.csv',delimiter=";")
df.head()

plt.figure(figsize = (20,4), dpi = 200)
sns.scatterplot (x='CI Name (aff)', y='Change Type' , data = df)
plt.show()
