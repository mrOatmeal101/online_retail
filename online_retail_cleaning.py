import numpy as np
import pandas as pd

df = pd.read_csv("unclean/test_online_retail.csv")

# print(df.head(21)) # this prints out the first 21 rows in the dataset.
# print(df.head()) # if you leave it blank it will print out the first 5 rows. 
# print(df.tail(10)) # this will print out the last ten rows of the dataset. 
# print(df.shape) # for the test it will give you (21,8) which is (total_rows, total_columns).
# shape is not a method so do not use (), it is an attribute
# print(df.info()) # gives columns and data types of each column and it is a method which requires ().

# pd.set_option('display.max_colums', 8) # this is changing a setting to show all of the columns if it cuts off some of them.
# useful if there is like 85 columns so instead of 8 you could put 85.
# pd.set_option('display.max_rows', 8) # this also works for rows. 

# schema_df = pd.read_csv('data/survey_results_schema.csv') can use pandas to also load the schema for the dataset. 
# so if you were doing a survey and you wanted to see what questions match the column titles for your dataset. 
# like if a column title was Hobbyist, the schema could show you the question: Do you code as a hobby?

# think of pandas dataframe (df) like python dictionaries with list:
# people = {
#     "first": ['cody', 'jane', 'john'],
#     "last": ['johnson', 'doe', 'doe'],
#     "email": ["cjohnson@email.com", 'janedoe@email.com', 'johndoe@email.com']
# }

# df = pd.DataFrame(people) # this will make a dataframe out of people, and it will add an index for each row. 
#   first    last       email
# 0 cody   johnson cjohnson@email.com
# 1 jane   doe      janedoe@email.com
# 2 john   doe      janedoe@email.com

# can then do quries like df['email'] to output the email column. 
# can also check type with type(def['email']) 
# this will output a series => pandas.core.series.Series

# a Series is basically a list of data i.e. it is the rows of a column.
# a Series is one dimensional
# so all of the first names are a Series, all of the last names are a Series, along with the emails.
# all come with their own indexes also.
# can also use the dot notation => df.email but usually use bracket as df.count would preform the method count which if there is a column
# named count it could cause some problemns. 
# a df is multidimensional

# to get multipule columns:
# print(df[['last', 'email']]) # need to pass in a list and that is why you have double brackets [[]]
# can also slice these.

# print(df.columns) # this will print out the column titles.
# Index(['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'Price', 'Customer ID', 'Country'], dtype='object')

# to get rows use loc and iloc
# iloc allows you to access the interger location. 
# think of loc and iloc as functions. 
# print(df.iloc[0]) # so this will access the first row in the dataset.
# Invoice                                     489434
# StockCode                                    85048
# Description    15CM CHRISTMAS GLASS BALL 20 LIGHTS
# Quantity                                        12
# InvoiceDate                    2009-12-01 07:45:00
# Price                                         6.95
# Customer ID                                13085.0
# Country                             United Kingdom
# Name: 0, dtype: object

# if you want multiply rows you need to make it a list of indexes, so double brackets.
# print(df.iloc[[0,1]])
#    Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0   489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1   489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom

# can also select columns
# so this will select the first 2 rows and the 2nd column. 
# print(df.iloc[[0,1], 2])
# 0    15CM CHRISTMAS GLASS BALL 20 LIGHTS
# 1                     PINK CHERRY LIGHTS
# Name: Description, dtype: object

# loc is search by label i.e. the indexes for the rows. 
# print(df.loc[0])
# Invoice                                     489434
# StockCode                                    85048
# Description    15CM CHRISTMAS GLASS BALL 20 LIGHTS
# Quantity                                        12
# InvoiceDate                    2009-12-01 07:45:00
# Price                                         6.95
# Customer ID                                13085.0
# Country                             United Kingdom
# Name: 0, dtype: object

# can also input a list to get multipule rows. 
# print(df.loc[[0,1]])
#    Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0   489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1   489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom

# can use labels to get the column you want with loc instead of using an interger
# print(df.loc[[0,1], 'Quantity'])
# 0    12
# 1    12
# Name: Quantity, dtype: int64

# can also put multi column names in as a list to get multiple columns.
# can change up the order of the column titles as it will print out in the order that is inputted. 
# print(df.loc[[0,1], ['Description', 'Quantity']])
#                            Description  Quantity
# 0  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12
# 1                   PINK CHERRY LIGHTS        12

# pandas has a lot of built in methods like .value_counts()
# print(df['Invoice'].value_counts())
# Invoice
# 489436    9
# 489434    8
# 489435    4
# Name: count, dtype: int64
# this shows that Invoice Number 489436 showed up 9 times, 489434 showed up 8 times, and 489435 showed up 4 times. 

# Can also slice with loc and it is almost the same as the python slice but the last index is inclusive. 
# print(df.loc[0:2, 'Customer ID'])
# 0    13085.0
# 1    13085.0
# 2    13085.0
# Name: Customer ID, dtype: float64

# can also slice the columns to:
# print(df.loc[3:6, 'Description':'Country'])
#                       Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 3    RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4  STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5      PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6             SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom

