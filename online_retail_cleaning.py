import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv("unclean/test_online_retail.csv")

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
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
# Then rename specific ones afterwards. 
df.rename(columns={    
    "invoice":"invoice_number",
    "stockcode":"stock_code",
    "invoicedate":"invoice_date"
    }, inplace=True)

# print(df.columns)

# The next step is to review the column invoice_number. 
    # first step is to see if there are duplicated values
    # using the built in pandas method duplicated()
    # also using the subset argument of duplicated() to refine search as there could be duplicated Invoices with different dates. 
# print(df[df.duplicated(subset=['invoice_number', 'stock_code', 'quantity', 'price'])])

# If you would like to log the duplicates you can 
# if df.duplicated(subset=['invoice_number', 'stock_code']).any():
#     print(df[df.duplicated()])
# else:
#     # print("no duplicates")

# After identifying that there are duplicates you want to drop the duplicates using 
df_clean = df.drop_duplicates(subset=['invoice_number', 'stock_code'], keep='first')
print(df_clean)