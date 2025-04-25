import numpy as np
import pandas as pd
import csv
from datetime import datetime

df = pd.read_csv("unclean/online_retail_II.csv")

# Making a copy of df to make sure the raw data is not modified. 
df_clean = df.copy()

# The beginning process of cleaning this dataset is to have a consistent column title
# this includes removing spaces, capitilization, and non-descriptive titles. 

# Here is how i manually renamed of all the column titles for readability. 
# df.rename(columns={
#     "Invoice":"invoice_number",
#     "StockCode":"stock_code",
#     "Description":"description",
#     "Quantity":"quantity",
#     "InvoiceDate":"invoice_date",
#     "Price":"price",
#     "Customer ID":"customer_id",
#     "Country":"country"}, inplace=True)

# You can also automate the column titles if they are dynamic or if there are a lot of columns in the data set. 
df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(' ','_')
# Then rename specific ones afterwards. 
df_clean.rename(columns={    
    "invoice":"invoice_number",
    "stockcode":"stock_code",
    "description":"description_text",
    "invoicedate":"invoice_date"
    }, inplace=True)

# print(df_clean.columns)

# The next step is to review the column invoice_number. 
    # first step is to see if there are duplicated values
    # using the built in pandas method duplicated()
    # also using the subset argument of duplicated() to refine search as there could be duplicated Invoices with different dates. 
# print(df_clean[df_clean.duplicated(subset=['invoice_number', 'stock_code', 'quantity', 'price'])])

# If you would like to log the duplicates you can also use an if statement with the built in .any() method
    # .any() method checks if any of the values in the Bollean Series are True.  
# if df_clean.duplicated(subset=['invoice_number', 'stock_code']).any():
#     print(df_clean[df_clean.duplicated()])
# else:
#     print("no duplicates")

# After identifying that there are duplicates you want to drop the duplicates using drop_duplicates()
    # using subset arguments invoice number and stock code,
df_clean = df_clean.drop_duplicates(subset=['invoice_number', 'stock_code'], keep='first')
# print(df_clean)

# Then after identifying/removing duplicates you want to check for missing or null values. 
    # Can check for missing values using .isna() combined with aggregate function .sum()
    # this will sum all of the Boolean values of True. 
# print(df.isna().sum())
# After seeing that there are missing values you can inspect the missing values again with .isna() and .any()
# print(df[df.isna().any(axis=1)])
# After inspection the next step is to replace the missing values with np.nan
df_clean.replace(['NA','N/A','null','',' '], np.nan, inplace=True)
# print(df_clean)
# print(df[df.isna().any(axis=1)])
# print(df_clean.info())

# The next step is to correct the data types for each column for smooth importing into pandas.
df_clean['invoice_number'] = df_clean['invoice_number'].astype(str)
df_clean['stock_code'] = df_clean['stock_code'].astype(str)
df_clean['description_text'] = df_clean['description_text'].astype(str)
df_clean['quantity'] = pd.to_numeric(df_clean['quantity'], errors='coerce').astype('Int64')
df_clean['invoice_date'] = pd.to_datetime(df_clean['invoice_date'], format='%Y-%m-%d %H:%M:%S')
df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')
df_clean['customer_id'] = pd.to_numeric(df_clean['customer_id'], errors='coerce').astype('Int64')
df_clean['country'] = df_clean['country'].astype(str)

# Validating data with SSMS data to ensure complete ingestion. 
# print(df_clean['quantity'])
# Double checking data before exporting
# print(df_clean.info())
# print(df_clean.count())
# print(df_clean['customer_id'].isna().sum())

# print(df_clean.head(-10))

# print(df[df.isna().any(axis=1)])

# print(df.isna().sum())

# if df_clean.duplicated(subset=['invoice_number', 'stock_code']).any():
#     print(df_clean[df_clean.duplicated()])
# else:
#     print("no duplicates")

# print(df[df['Invoice'] == '541971'])
# Last step is to export the cleaned data and wrap all the fields in double qutoes.
    # this is to close off open quotes and extra commas in the data. 
# df_clean.to_csv('clean/cleaned_online_retail_II.csv', index=False, quoting=csv.QUOTE_MINIMAL, quotechar='"')