#Verileri CSV dosyasından çekme

import pm4py
import pandas as pd

df=pd.read_csv('C:/Users/90531/Desktop/Detail_Change1.csv',delimiter=";")

print(df['CI Name (aff)'] +"     "+ df['CI Type (aff)'] +"     "+ df['Actual Start'] +"     "+  df['Actual End'])