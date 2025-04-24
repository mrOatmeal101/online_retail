import numpy as np
import pandas as pd
from datetime import datetime

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

#  ****** Indexes - How to set, reset, and Use Indexes ********

# can set the index of a dataset with 
# df.set_index('email') email is the name of the column you want to set as your index.
# print(df.index) # this will show you the index
# RangeIndex(start=0, stop=21, step=1)
# Will need to add inplace=True to make the changes take affect
# so final will look like
# df.set_index('email', inplace=True)

# to reset the index 
# df.reset_index(inplace=True)

# to set index at the beginning when you are importing the data from a csv
# you add another argument to the read command
# df.pd.read_csvdf = pd.read_csv("unclean/test_online_retail.csv", index_col='whatever_name_you_want')

# can also do this to your schema so that you can overwrite the auto generated index to be the column names 
# so that it is easier to search the schema using loc
# schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')
# so now you can search for what the column is directly 
# schema_df.loc['Hobbyist'] which will now give you the description of what the Hobbyist column contains.

# ********* Filtering - Using Conditionals to Filter Rows and Columns **********

# print(df['Invoice'] == 489436) # this outputs a Series with boolean values. ie True/False
# this is a filter mask 
# 0     False
# 1     False
# 2     False
# 3     False
# 4     False
# 5     False
# 6     False
# 7     False
# 8     False
# 9     False
# 10    False
# 11    False
# 12     True
# 13     True
# 14     True
# 15     True
# 16     True
# 17     True
# 18     True
# 19     True
# 20     True
# Name: Invoice, dtype: bool

# can also assign to a variable but dont use the word 'filter' for a var name as it is a python keyword.
# filt = (df['Invoice'] == 489436) # if this is a string make sure to add "" around the string.

# print(df[filt]) # then calling on the var with df will give you a data set back
#     Invoice StockCode                    Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 12   489436    48173C          DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755       LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 14   489436     21754       HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 15   489436     84879  ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 16   489436     22119     PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 17   489436     22142   CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 18   489436     22296      HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 19   489436     22295      HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 20   489436     22109   FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom

# Another way to write is:
# print(df[df['Invoice'] == 489436])

# And another way to write:
# print(df.loc[filt])

# can add other parameters using .loc:
# print(df.loc[filt, 'StockCode'])
# 12    48173C
# 13     21755
# 14     21754
# 15     84879
# 16     22119
# 17     22142
# 18     22296
# 19     22295
# 20     22109
# Name: StockCode, dtype: object

# AND/OR operators using pandas
# AND is & and OR is |

# You can use operators to further refine your search results
# so in this example we are filtering for Customer ID is equal to 13078.0 AND where Price is equal to 1.65
# filt = (df['Customer ID'] == 13078.0) & (df["Price"] == 1.65)
# then we print out the filter with only the Invoice column.
# print(df.loc[filt, 'Invoice'])
# 18    489436
# 19    489436
# Name: Invoice, dtype: int64

# Using the OR operator
# filt = (df['Customer ID'] == 13078.0) & (df["Price"] == 1.65) | (df["Price"] == 3.39)
# print(df.loc[filt, 'Invoice'])
# 18    489436
# 19    489436
# 20    489436
# Name: Invoice, dtype: int64

# To get the oppisite of your filter you can use the ~:
# filt = (df['Customer ID'] == 13078.0) & (df["Price"] == 1.65)
# so this will exclude rows 18 and 19
# print(df.loc[~filt, 'Invoice'])
# 0     489434
# 1     489434
# 2     489434
# 3     489434
# 4     489434
# 5     489434
# 6     489434
# 7     489434
# 8     489435
# 9     489435
# 10    489435
# 11    489435
# 12    489436
# 13    489436
# 14    489436
# 15    489436
# 16    489436
# 17    489436
# 20    489436
# Name: Invoice, dtype: int64

# Another example of filtering where you try and find item prices are over 2.00
# expensive = (df['Price'] > 2.00)
# print(df.loc[expensive])
#     Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0    489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1    489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3    489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 7    489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8    489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9    489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 11   489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 12   489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 14   489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 16   489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 20   489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom

# to narrow down the columns you can just pass into .loc using a list.
# print(df.loc[expensive, ['Invoice', 'Description']])
#     Invoice                          Description
# 0    489434  15CM CHRISTMAS GLASS BALL 20 LIGHTS
# 1    489434                   PINK CHERRY LIGHTS
# 2    489434                  WHITE CHERRY LIGHTS
# 3    489434         RECORD FRAME 7" SINGLE SIZE
# 7    489434   FANCY FONT HOME SWEET HOME DOORMAT
# 8    489435                            CAT BOWL
# 9    489435       DOG BOWL , CHASING BALL DESIGN
# 11   489435   LUNCHBOX WITH CUTLERY FAIRY CAKES
# 12   489436                DOOR MAT BLACK FLOCK
# 13   489436             LOVE BUILDING BLOCK WORD
# 14   489436             HOME BUILDING BLOCK WORD
# 16   489436           PEACE WOODEN BLOCK LETTERS
# 20   489436         FULL ENGLISH BREAKFAST PLATE

# a shortcut if you have a lot of items you want to filter by
# you can make a list with the items you want to look for
# prices = [6.75, 5.95, 2.55,]
# then call on the data set with the column title you want and use isin to call on the list you made.
# filt = df['Price'].isin(prices)
# print(df.loc[filt])
#     Invoice StockCode                         Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 1    489434    79323P                  PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                 WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 7    489434     21523  FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8    489435     22350                           CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 11   489435     22353  LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 12   489436    48173C               DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 14   489436     21754            HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom

# can also use string methods to find items where their might be multi values and they are seperated by ; or : or something else
# so using str to see if the string of text in Description contains the string "DOG"
# filt = df['Description'].str.contains('DOG')
# then applying the filter to the dataframe
# print(df.loc[filt])
#    Invoice StockCode                     Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 9   489435     22349  DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom

# Again, you can add additional parameters so that not all of the columns print out. 
# print(df.loc[filt, 'Description'])
# 9    DOG BOWL , CHASING BALL DESIGN
# Name: Description, dtype: object

# can also use string methods to replace text, split values, and all kinds of stuff.
# Again as a reminder if you just did print(filt) you will get a Series which contains boolean values 
# then after applying to the dataframe: print(df.loc[filt])
# it will then only show the True values for the Series. 

# ****** Updating Rows and Columns - Modifying Data Within DataFrames *******
# Recap to show Column names
# print(df.columns)
# Index(['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'Price', 'Customer ID', 'Country'], dtype='object')

# So if you wanted to update the columns to be more specific
# you can do an assignment using the columns attribute and then pass in a list of what you want all of the column names to be
# df.columns = ['new_column_name', 'new_column_name']
# this way is inefficent though as you have to input all of the column names in and you cannot just update one column name

# Side note: if you want to update something specific in your column names like change everything to uppercase or remove spaces and put _
# you can use a list comprehension.
# df.columns = [x.upper() for x in df.columns]
# print(df)
#     INVOICE STOCKCODE                          DESCRIPTION  QUANTITY          INVOICEDATE  PRICE  CUSTOMER ID         COUNTRY
# 0    489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1    489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3    489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4    489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5    489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6    489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 7    489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8    489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9    489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 10   489435     22195         HEART MEASURING SPOONS LARGE        24  2009-12-01 07:46:00   1.65      13085.0  United Kingdom
# 11   489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 12   489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 14   489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 15   489436     84879        ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 16   489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 17   489436     22142         CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 18   489436     22296            HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 19   489436     22295            HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 20   489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom

# if you wanted to replace spaces with _ you can use the string replace method. See Customer ID column
# df.columns = df.columns.str.replace(' ', '_')
# print(df)
#     Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer_ID         Country
# 0    489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1    489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3    489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4    489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5    489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6    489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 7    489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8    489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9    489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 10   489435     22195         HEART MEASURING SPOONS LARGE        24  2009-12-01 07:46:00   1.65      13085.0  United Kingdom
# 11   489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 12   489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 14   489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 15   489436     84879        ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 16   489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 17   489436     22142         CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 18   489436     22296            HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 19   489436     22295            HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 20   489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom

# can also use rename method and pass in a dictionary of the column names you want to change
# df.rename(columns={'Invoice': 'Invoice_Number', 'Customer ID': 'Customer_ID'}, inplace=True)
# this is a method where inplace=True for the changes to take affect.
# print(df)
#     Invoice_Number StockCode                          Description  Quantity          InvoiceDate  Price  Customer_ID         Country
# 0           489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1           489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2           489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3           489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4           489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5           489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6           489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 7           489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8           489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9           489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 10          489435     22195         HEART MEASURING SPOONS LARGE        24  2009-12-01 07:46:00   1.65      13085.0  United Kingdom
# 11          489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 12          489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13          489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 14          489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 15          489436     84879        ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 16          489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 17          489436     22142         CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 18          489436     22296            HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 19          489436     22295            HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 20          489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom

# to update rows
# First call on the row we want to change to see what is in it. 
# print(df.loc[2])
# Invoice                      489434
# StockCode                    79323W
# Description     WHITE CHERRY LIGHTS
# Quantity                         12
# InvoiceDate     2009-12-01 07:45:00
# Price                          6.75
# Customer ID                 13085.0
# Country              United Kingdom
# Name: 2, dtype: object

# Then to update you can update by inputing a list like we did with columns names.
# df.loc[2] = [489435, 79324, "RED CHERRY LIGHTS", 14]
# though this has the same problem as before in that you have to update every row.

# so if you just want to update a couple of values you can use loc
# first input the row you want to change then pass in a list of the columns that you want
# df.loc[2, ['Quantity', 'Price']] = [21, 7.00]
# print(df.loc[2])
# Invoice                      489434
# StockCode                    79323W
# Description     WHITE CHERRY LIGHTS
# Quantity                         21
# InvoiceDate     2009-12-01 07:45:00
# Price                           7.0
# Customer ID                 13085.0
# Country              United Kingdom
# Name: 2, dtype: object

# to change just a single value you just don't pass in a list
# df.loc[2, 'Price'] = 7.00
# print(df.loc[2])
# Invoice                      489434
# StockCode                    79323W
# Description     WHITE CHERRY LIGHTS
# Quantity                         12
# InvoiceDate     2009-12-01 07:45:00
# Price                           7.0
# Customer ID                 13085.0
# Country              United Kingdom
# Name: 2, dtype: object

# pandas also as a built in method called at which works the sames as loc from above
# df.at[2, 'Price'] = 7.00

# if you want to use a filter, it has to be formatted correctly ie you need to use loc and not just set it directly
# filt = (df['email'] == 'JohnDoe@email.com')
# df.loc[filt, 'last'] = "Smith"

# to update multiple rows of data.
# assign a column to the lowercase value of itself. 
# df['email'].str.lower() # this just returns the values but did not change anything

# to actually change the data you would assign the column to that value
# df['email'] = df['email'].str.lower()

# for more complex data manipulation there are 4 common methods
# apply, map, applymap, replace: these are the 4 methods

# apply: is used for calling a function on our values
# works on either a dataframe or Series object.
# first example is using apply on a Series
# So you are applying a function to every value in the Series. 
# for instance, if you are trying to find the length you can apply the len function to every value in the Series.
# this will give you the length of every row in Description column
# print(df['Description'].apply(len))
# 0     35
# 1     18
# 2     20
# 3     28
# 4     30
# 5     26
# 6     19
# 7     34
# 8      9
# 9     30
# 10    28
# 11    34
# 12    21
# 13    24
# 14    24
# 15    29
# 16    27
# 17    28
# 18    25
# 19    25
# 20    28
# Name: Description, dtype: int64

# can use whatever function you want to use
# def update_description(args):
#     return args.lower()

# print(df['Description'].apply(update_description))
# or 
# old_descript = df["Description"]
# print(old_descript.apply(update_description))
# 0     15cm christmas glass ball 20 lights
# 1                      pink cherry lights
# 2                     white cherry lights
# 3            record frame 7" single size
# 4          strawberry ceramic trinket box
# 5              pink doughnut trinket pot
# 6                     save the planet mug
# 7      fancy font home sweet home doormat
# 8                               cat bowl
# 9          dog bowl , chasing ball design
# 10           heart measuring spoons large
# 11     lunchbox with cutlery fairy cakes
# 12                  door mat black flock
# 13               love building block word
# 14               home building block word
# 15          assorted colour bird ornament
# 16             peace wooden block letters
# 17           christmas craft white fairy
# 18              heart ivory trellis large
# 19              heart filigree dove large
# 20           full english breakfast plate
# Name: Description, dtype: object

# using an anonymous/lambda functions is also acceptable 
# df['Description'] = df['Description'].apply(lambda x: x.lower())
# print(df)

# print(df.apply(len))
# print(df.apply(pd.Series.min))

# print(df['Description'].map({'PINK CHERRY LIGHTS': 'RED CHERRY LIGHTS', 'FULL ENGLISH BREAKFAST PLATE': "FULL BRITISH BREAKFAST PLATE"}))
# 0                              NaN
# 1                RED CHERRY LIGHTS
# 2                              NaN
# 3                              NaN
# 4                              NaN
# 5                              NaN
# 6                              NaN
# 7                              NaN
# 8                              NaN
# 9                              NaN
# 10                             NaN
# 11                             NaN
# 12                             NaN
# 13                             NaN
# 14                             NaN
# 15                             NaN
# 16                             NaN
# 17                             NaN
# 18                             NaN
# 19                             NaN
# 20    FULL BRITISH BREAKFAST PLATE
# Name: Description, dtype: object

# print(df['Description'].replace({'PINK CHERRY LIGHTS': 'RED CHERRY LIGHTS', 'FULL ENGLISH BREAKFAST PLATE': "FULL BRITISH BREAKFAST PLATE"}))
# 0     15CM CHRISTMAS GLASS BALL 20 LIGHTS
# 1                       RED CHERRY LIGHTS
# 2                     WHITE CHERRY LIGHTS
# 3            RECORD FRAME 7" SINGLE SIZE
# 4          STRAWBERRY CERAMIC TRINKET BOX
# 5              PINK DOUGHNUT TRINKET POT
# 6                     SAVE THE PLANET MUG
# 7      FANCY FONT HOME SWEET HOME DOORMAT
# 8                               CAT BOWL
# 9          DOG BOWL , CHASING BALL DESIGN
# 10           HEART MEASURING SPOONS LARGE
# 11     LUNCHBOX WITH CUTLERY FAIRY CAKES
# 12                  DOOR MAT BLACK FLOCK
# 13               LOVE BUILDING BLOCK WORD
# 14               HOME BUILDING BLOCK WORD
# 15          ASSORTED COLOUR BIRD ORNAMENT
# 16             PEACE WOODEN BLOCK LETTERS
# 17           CHRISTMAS CRAFT WHITE FAIRY
# 18              HEART IVORY TRELLIS LARGE
# 19              HEART FILIGREE DOVE LARGE
# 20           FULL BRITISH BREAKFAST PLATE
# Name: Description, dtype: object

# def customer_id(args):
#     if type(args) == float:
#         return int(args)

# print(df["Customer ID"].apply(customer_id))

# ******** ADD/REMOVE ROWS AND COLUMNS FROM DATAFRAMES ****************
# to combine columns and make a new column you can use bracket notation
# df['full_name'] = df['first'] + ' ' + df['last']

# to remove a column you can use drop 
# df.drop(columns=['first', 'last']) # this just gives a preview of what it would look like
# in the inplace=True if you want changes to take effect.abs

# If you wanted to create columns out of an existing column you can use the split method and the expand method
# df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)

# To add row to dataframe, you can use the concat method.
# new_row = pd.DataFrame([{'first': 'Tony'}])
# df = pd.concat([df, new_row], ignore_index=True)
# print(df)
# need the ignore_index=True or will throw error of not having an index.
# every row that does not have a value will be auto filled with NaN

# To combine rows of the dataframe you can also you concat
# though you need to be aware that the indexes will not match up so you need ignore_index=True
# it will still throw a warning telling you that the sort will not be controlled.
# if you dont want pandas to sort the data you will also need to set sort=False

# people = {
#     "first": ['cody', 'jane', 'john'],
#     "last": ['johnson', 'doe', 'doe'],
#     "email": ["cjohnson@email.com", 'janedoe@email.com', 'johndoe@email.com']
# }

# people2 = {
#     "first": ['Tony', 'Steve'],
#     "last": ['Stark', 'Rogers'],
#     "email": ["ironman@email.com", 'cap@email.com']
# }

# df2 = pd.DataFrame(people)
# df3 = pd.DataFrame(people2)

# df_combined = pd.concat([df2, df3], ignore_index=True, sort=False)
# print(df_combined)
#    first     last               email
# 0   cody  johnson  cjohnson@email.com
# 1   jane      doe   janedoe@email.com
# 2   john      doe   johndoe@email.com
# 3   Tony    Stark   ironman@email.com
# 4  Steve   Rogers       cap@email.com

# To remove rows you can pass in the indexes.
# df_combined.drop(index=4, inplace=True)
# print(df_combined)
#   first     last               email
# 0  cody  johnson  cjohnson@email.com
# 1  jane      doe   janedoe@email.com
# 2  john      doe   johndoe@email.com
# 3  Tony    Stark   ironman@email.com

# can also drop by using a conditional inside of the brackets. This is similar to how we built the filter in the previous section.
# df_combind.drop(index=df[df['last'] == 'Doe'].index)
# print(df_combined)

# a prettier way to write the above by putting you filter into a variable. 
# filt = df['last'] == 'Doe'
# df_combind.drop(index=df[filt].index)
# print(df_combined)

# ******** SORTING DATA **************
# people = {
#     "first": ['cody', 'jane', 'john'],
#     "last": ['johnson', 'doe', 'doe'],
#     "email": ["cjohnson@email.com", 'janedoe@email.com', 'johndoe@email.com']
# }

# people2 = {
#     "first": ['Tony', 'Steve'],
#     "last": ['Stark', 'Rogers'],
#     "email": ["ironman@email.com", 'cap@email.com']
# }

# df2 = pd.DataFrame(people)
# df3 = pd.DataFrame(people2)

# df_combined = pd.concat([df2, df3], ignore_index=True, sort=False)

# print(df2.sort_values(by='last'))
#   first     last               email
# 1  jane      doe   janedoe@email.com
# 2  john      doe   johndoe@email.com
# 0  cody  johnson  cjohnson@email.com

# you can sort by column, which has a default, at least for numbers, low to high
# if you want high to low you need to add ascending=False, which will sort the values high to low
# print(df.sort_values(by='Price', ascending=False))
#     Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0    489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 16   489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 1    489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 7    489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 14   489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 12   489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 9    489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 20   489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom
# 8    489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 11   489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 3    489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 15   489436     84879        ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 19   489436     22295            HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 5    489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 10   489435     22195         HEART MEASURING SPOONS LARGE        24  2009-12-01 07:46:00   1.65      13085.0  United Kingdom
# 18   489436     22296            HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 17   489436     22142         CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 4    489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 6    489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom

# print(df.sort_values(by='Description'))

# Can also pass in a list of columns to sort by so if there is duplicates it will refer to the second or third provided column name. 
# print(df2.sort_values(by=['last', 'first'], ascending=False))
#   first     last               email
# 0  cody  johnson  cjohnson@email.com
# 2  john      doe   johndoe@email.com
# 1  jane      doe   janedoe@email.com

# Can also sort different columns by passing in a list of boolean values. 
# this is order dependent, ie the first index of the list of columns will be attached to the first index of the boolean list. 
# Again if you want the changes to take effect you will need to set inplace to True
# print(df_combined.sort_values(by=['last', 'first'], ascending=[False, True]))
#    first     last               email
# 0   cody  johnson  cjohnson@email.com
# 1   jane      doe   janedoe@email.com
# 2   john      doe   johndoe@email.com
# 3   Tony    Stark   ironman@email.com
# 4  Steve   Rogers       cap@email.com

# can also sort by index
# print(df_combined.sort_index())

# can also sort just a single Series/column, as Series objs have the sort_values() method.
# this has all arguments set to default
# print(df_combined['last'].sort_values())
# 4     Rogers
# 3      Stark
# 1        doe
# 2        doe
# 0    johnson
# Name: last, dtype: object

# Another example wehre i added more data to the test file
# Now the data is sorted by price and by country
# df.sort_values(by=['Country', 'Price'], ascending=[True, False], inplace=True)
# So this has the countries in alpha order and the prices in decending order. 
# print(df)
#     Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 23  C489449     21895        POTTING SHED SOW 'N' GROW SET        -4  2009-12-01 10:33:00   4.25      16321.0       Australia
# 21  C489449     22087             PAPER BUNTING WHITE LACE       -12  2009-12-01 10:33:00   2.95      16321.0       Australia
# 25  C489449     22083           PAPER CHAIN KIT RETRO SPOT       -12  2009-12-01 10:33:00   2.95      16321.0       Australia
# 24  C489449     21896                   POTTING SHED TWINE        -6  2009-12-01 10:33:00   2.10      16321.0       Australia
# 22  C489449    85206A         CREAM FELT EASTER EGG BASKET        -6  2009-12-01 10:33:00   1.65      16321.0       Australia
# 26  C489449     21871                  SAVE THE PLANET MUG       -12  2009-12-01 10:33:00   1.25      16321.0       Australia
# 27  C489449     84946      ANTIQUE SILVER TEA GLASS ETCHED       -12  2009-12-01 10:33:00   1.25      16321.0       Australia
# 28  C489449    84970S    HANGING HEART ZINC T-LIGHT HOLDER       -24  2009-12-01 10:33:00   0.85      16321.0       Australia
# 33   489520     21523   FANCY FONT HOME SWEET HOME DOORMAT         2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 34   489520     48187                 DOOR MAT NEW ENGLAND         2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 35   489520     48195              DOOR MAT GREEN PAISLEY          2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 37   489520    85232D        SET/3 DECOUPAGE STACKING TINS         3  2009-12-01 11:41:00   4.95      14911.0            EIRE
# 31   489520     22114    HOT WATER BOTTLE TEA AND SYMPATHY         8  2009-12-01 11:41:00   3.95      14911.0            EIRE
# 32   489520     22212           FOUR HOOK  WHITE LOVEBIRDS         6  2009-12-01 11:41:00   2.10      14911.0            EIRE
# 36   489520     72741                GRAND CHOCOLATECANDLE        36  2009-12-01 11:41:00   1.45      14911.0            EIRE
# 30   489520    72739B         WHITE CHOCOLATE SCENT CANDLE        12  2009-12-01 11:41:00   1.25      14911.0            EIRE
# 29   489520    35751C           PURPLE CURRENT CANDLE RING        12  2009-12-01 11:41:00   0.75      14911.0            EIRE
# 44   489526     21537             RETRO SPOTS PUDDING BOWL         4  2009-12-01 11:50:00   4.25      12533.0         Germany
# 45   489526     21733     RED HANGING HEART T-LIGHT HOLDER         6  2009-12-01 11:50:00   2.95      12533.0         Germany
# 41   489526     22077               6 RIBBONS RUSTIC CHARM        12  2009-12-01 11:50:00   1.65      12533.0         Germany
# 43   489526     84948   SILVER HANGING T-LIGHT HOLDER DOME        24  2009-12-01 11:50:00   1.65      12533.0         Germany
# 38   489526    85049E            SCANDINAVIAN REDS RIBBONS        12  2009-12-01 11:50:00   1.25      12533.0         Germany
# 42   489526     84946      ANTIQUE SILVER TEA GLASS ETCHED        12  2009-12-01 11:50:00   1.25      12533.0         Germany
# 39   489526     21976       PACK OF 60 MUSHROOM CAKE CASES        24  2009-12-01 11:50:00   0.55      12533.0         Germany
# 40   489526     21498                     RED SPOTS  WRAP         25  2009-12-01 11:50:00   0.42      12533.0         Germany
# 0    489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 16   489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 1    489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2    489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 7    489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 12   489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 14   489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 13   489436     21755             LOVE BUILDING BLOCK WORD        18  2009-12-01 09:06:00   5.45      13078.0  United Kingdom
# 9    489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# 20   489436     22109         FULL ENGLISH BREAKFAST PLATE        16  2009-12-01 09:06:00   3.39      13078.0  United Kingdom
# 8    489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 11   489435     22353   LUNCHBOX WITH CUTLERY FAIRY CAKES         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 3    489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 15   489436     84879        ASSORTED COLOUR BIRD ORNAMENT        16  2009-12-01 09:06:00   1.69      13078.0  United Kingdom
# 5    489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 10   489435     22195         HEART MEASURING SPOONS LARGE        24  2009-12-01 07:46:00   1.65      13085.0  United Kingdom
# 18   489436     22296            HEART IVORY TRELLIS LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 19   489436     22295            HEART FILIGREE DOVE LARGE        12  2009-12-01 09:06:00   1.65      13078.0  United Kingdom
# 17   489436     22142         CHRISTMAS CRAFT WHITE FAIRY         12  2009-12-01 09:06:00   1.45      13078.0  United Kingdom
# 4    489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 6    489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom

# If you want to sort by looking at the largest or smallest values.
# there is the nlargest method that will show you the largest values
# print(df['Price'].nlargest(10))
# 0     6.95
# 16    6.95
# 1     6.75
# 2     6.75
# 33    6.75
# 34    6.75
# 35    6.75
# 7     5.95
# 12    5.95
# 14    5.95
# Name: Price, dtype: float64

# if you want to see all of the data assoiated with the largest values
# print(df.nlargest(10,"Price"))
#    Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0   489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 16  489436     22119           PEACE WOODEN BLOCK LETTERS         3  2009-12-01 09:06:00   6.95      13078.0  United Kingdom
# 1   489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2   489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 33  489520     21523   FANCY FONT HOME SWEET HOME DOORMAT         2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 34  489520     48187                 DOOR MAT NEW ENGLAND         2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 35  489520     48195              DOOR MAT GREEN PAISLEY          2  2009-12-01 11:41:00   6.75      14911.0            EIRE
# 7   489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 12  489436    48173C                DOOR MAT BLACK FLOCK         10  2009-12-01 09:06:00   5.95      13078.0  United Kingdom
# 14  489436     21754             HOME BUILDING BLOCK WORD         3  2009-12-01 09:06:00   5.95      13078.0  United Kingdom

# To find the smallest, use nsmallest() method
# print(df.nsmallest(10,"Price"))
#     Invoice StockCode                        Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 40   489526     21498                   RED SPOTS  WRAP         25  2009-12-01 11:50:00   0.42      12533.0         Germany
# 39   489526     21976     PACK OF 60 MUSHROOM CAKE CASES        24  2009-12-01 11:50:00   0.55      12533.0         Germany
# 29   489520    35751C         PURPLE CURRENT CANDLE RING        12  2009-12-01 11:41:00   0.75      14911.0            EIRE
# 28  C489449    84970S  HANGING HEART ZINC T-LIGHT HOLDER       -24  2009-12-01 10:33:00   0.85      16321.0       Australia
# 4    489434     21232     STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 6    489434     21871                SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 26  C489449     21871                SAVE THE PLANET MUG       -12  2009-12-01 10:33:00   1.25      16321.0       Australia
# 27  C489449     84946    ANTIQUE SILVER TEA GLASS ETCHED       -12  2009-12-01 10:33:00   1.25      16321.0       Australia
# 30   489520    72739B       WHITE CHOCOLATE SCENT CANDLE        12  2009-12-01 11:41:00   1.25      14911.0            EIRE
# 38   489526    85049E          SCANDINAVIAN REDS RIBBONS        12  2009-12-01 11:50:00   1.25      12533.0         Germany

# ******************* Grouping and Aggregating - Analyzing and Exploring Your Data **********************
# print(df['Price'].median())
# 2.1

# to get quick overview of data you can use describe
# print(df.describe())
#         Quantity      Price   Customer ID
# count  46.000000  46.000000     46.000000
# mean    9.608696   3.113043  13907.673913
# std    13.263950   2.147281   1375.077179
# min   -24.000000   0.420000  12533.000000
# 25%     3.000000   1.450000  13078.000000
# 50%    12.000000   2.100000  13085.000000
# 75%    15.000000   4.775000  14911.000000
# max    48.000000   6.950000  16321.000000

# count() - This method returns the number of non-null values in each column of a DataFrame or Series.
# It essentially tells you how many valid entries exist within each column, excluding any missing or NaN (Not a Number) values.
# When applied to a DataFrame, it returns a Series with the count for each column.
# When applied to a Series, it returns a scalar value representing the total count of non-null elements in that Series.

# print(df["Country"].count())
# 46

# value_counts() - This method returns a Series containing the counts of unique values within a Series or a column of a DataFrame.
# It shows how many times each distinct value appears in the data.
# The result is sorted in descending order by frequency, making it easy to see the most common values.
# By default, it excludes NaN values, but you can include them using the dropna=False parameter.

# print(df["Country"].value_counts())
# Country
# United Kingdom    21
# EIRE               9
# Australia          8
# Germany            8
# Name: count, dtype: int64

# Another example of value_counts() would be how many people on a survey answered yes or no. 
# can set value_counts(normalize=True) to show the percentages instead of the raw numbers

# print(df['Invoice'].value_counts(normalize=True))
# Invoice
# 489520     0.195652
# 489436     0.195652
# C489449    0.173913
# 489434     0.173913
# 489526     0.173913
# 489435     0.086957
# Name: proportion, dtype: float64

# Pandas groupby() - is a powerful method used to group rows in a DataFrame based on one or more columns. 
# It follows a "split-apply-combine" approach:
# Split:
    # The DataFrame is split into groups based on the unique values in the specified column(s).
# Apply:
    # A function is applied to each group independently. This can be an aggregation function (sum, mean, count), 
    # a transformation, or a filtering operation.
# Combine:
    # The results of the function application are combined into a new DataFrame or Series.

# country_grp = df.groupby(['Country']) # this will give you a DataFrameGroupBy object
# this object contains a bunch of groups and you can set it as a variable. 
# print(country_grp.get_group('Germany'))
#    Invoice StockCode                         Description  Quantity          InvoiceDate  Price  Customer ID  Country
# 38  489526    85049E           SCANDINAVIAN REDS RIBBONS        12  2009-12-01 11:50:00   1.25      12533.0  Germany
# 39  489526     21976      PACK OF 60 MUSHROOM CAKE CASES        24  2009-12-01 11:50:00   0.55      12533.0  Germany
# 40  489526     21498                    RED SPOTS  WRAP         25  2009-12-01 11:50:00   0.42      12533.0  Germany
# 41  489526     22077              6 RIBBONS RUSTIC CHARM        12  2009-12-01 11:50:00   1.65      12533.0  Germany
# 42  489526     84946     ANTIQUE SILVER TEA GLASS ETCHED        12  2009-12-01 11:50:00   1.25      12533.0  Germany
# 43  489526     84948  SILVER HANGING T-LIGHT HOLDER DOME        24  2009-12-01 11:50:00   1.65      12533.0  Germany
# 44  489526     21537            RETRO SPOTS PUDDING BOWL         4  2009-12-01 11:50:00   4.25      12533.0  Germany
# 45  489526     21733    RED HANGING HEART T-LIGHT HOLDER         6  2009-12-01 11:50:00   2.95      12533.0  Germany

# can also do this by using a filter.
# filt = df['Country'] == 'Germany'
# print(df.loc[filt])
#    Invoice StockCode                         Description  Quantity          InvoiceDate  Price  Customer ID  Country
# 38  489526    85049E           SCANDINAVIAN REDS RIBBONS        12  2009-12-01 11:50:00   1.25      12533.0  Germany
# 39  489526     21976      PACK OF 60 MUSHROOM CAKE CASES        24  2009-12-01 11:50:00   0.55      12533.0  Germany
# 40  489526     21498                    RED SPOTS  WRAP         25  2009-12-01 11:50:00   0.42      12533.0  Germany
# 41  489526     22077              6 RIBBONS RUSTIC CHARM        12  2009-12-01 11:50:00   1.65      12533.0  Germany
# 42  489526     84946     ANTIQUE SILVER TEA GLASS ETCHED        12  2009-12-01 11:50:00   1.25      12533.0  Germany
# 43  489526     84948  SILVER HANGING T-LIGHT HOLDER DOME        24  2009-12-01 11:50:00   1.65      12533.0  Germany
# 44  489526     21537            RETRO SPOTS PUDDING BOWL         4  2009-12-01 11:50:00   4.25      12533.0  Germany
# 45  489526     21733    RED HANGING HEART T-LIGHT HOLDER         6  2009-12-01 11:50:00   2.95      12533.0  Germany

# but groupby groups all of them so you can make more refined searches like how many customer ids are in each country. 
# print(country_grp['Customer ID'].value_counts())
# Country         Customer ID
# Australia       16321.0         8
# EIRE            14911.0         9
# Germany         12533.0         8
# United Kingdom  13085.0        12
#                 13078.0         9
# Name: count, dtype: int64

# can also use .loc to find out more specific information or narrow your search
# print(country_grp['Customer ID'].value_counts().loc['United Kingdom'])
# Customer ID
# 13085.0    12
# 13078.0     9
# Name: count, dtype: int64

# can use normalize to find the %. 
# print(country_grp['Customer ID'].value_counts(normalize=True).loc['United Kingdom'])
# Customer ID
# 13085.0    0.571429
# 13078.0    0.428571
# Name: proportion, dtype: float64

# print(country_grp['Price'].median())
# Country
# Australia         1.875
# EIRE              3.950
# Germany           1.450
# United Kingdom    2.550
# Name: Price, dtype: float64

# print(country_grp['Price'].median().loc['EIRE'])
# 3.95

# If you want to get mulit agg functions going you can use 
# print(country_grp['Price'].agg(['median', 'mean']))
# Country
# Australia        1.875  2.156250
# EIRE             3.950  3.855556
# Germany          1.450  1.746250
# United Kingdom   2.550  3.680000

# print(country_grp['Price'].agg(['median', 'mean']).loc['EIRE'])
# median    3.950000
# mean      3.855556
# Name: EIRE, dtype: float64

# filt = df['Country'] == 'Germany'
# print(df.loc[filt])

# ****************** Cleaning Data - Casting Datatypes and Handling Missing Values ***********************
# How to drop missing values
# people = {
#     "first": ['cody', 'jane', 'john', 'Chris', np.nan, None, 'NA'],
#     "last": ['johnson', 'doe', 'doe', "Schafter", np.nan, np.nan, "Missing" ],
#     "email": ["cjohnson@email.com", 'janedoe@email.com', 'johndoe@email.com', None, np.nan, "anonymous@email.com", "NA"],
#     "age": ['33', '55', '63', '36', None, None, "Missing"]
# }

# df2 = pd.DataFrame(people)

# print(df2.dropna())
#   first     last               email      age
# 0  cody  johnson  cjohnson@email.com       33
# 1  jane      doe   janedoe@email.com       55
# 2  john      doe   johndoe@email.com       63
# 6    NA  Missing                  NA  Missing

# behind the sences there is some default values being set which are the following
# this will get you the same results as above. 
# df2.dropna(axis='index', how='any')
# the axis argument can be set to index or columns 
    # if set to index they drop the rows if the rows are missing any values
    # if set to column it will drop the columns if they are missing values. 
# the other arg is how, which is the criteria for what will be dropped. 
    # if set to "all" it will only drop if all the values are missing 
    # any will drop the rows/columns with any missing values. 
# print(df2.dropna(axis='index', how='all'))
#    first      last                email      age
# 0   cody   johnson   cjohnson@email.com       33
# 1   jane       doe    janedoe@email.com       55
# 2   john       doe    johndoe@email.com       63
# 3  Chris  Schafter                 None       36
# 5   None       NaN  anonymous@email.com     None
# 6     NA   Missing                   NA  Missing

# if you change axis to column then it will drop the column that is missing the values. 
# so no columns have everything missing so it will not drop anything from the df. 
# print(df2.dropna(axis='columns', how='all'))
#    first      last                email      age
# 0   cody   johnson   cjohnson@email.com       33
# 1   jane       doe    janedoe@email.com       55
# 2   john       doe    johndoe@email.com       63
# 3  Chris  Schafter                 None       36
# 4    NaN       NaN                  NaN     None
# 5   None       NaN  anonymous@email.com     None
# 6     NA   Missing                   NA  Missing

# if you want to be more specific with your drops like only drop rows that have specific columns missing. 
# for example if they have first and last name but no email address.
# you can pass a subset argument.
# print(df2.dropna(axis='index', how='all', subset=['email']))
#   first     last                email      age
# 0  cody  johnson   cjohnson@email.com       33
# 1  jane      doe    janedoe@email.com       55
# 2  john      doe    johndoe@email.com       63
# 5  None      NaN  anonymous@email.com     None
# 6    NA  Missing                   NA  Missing
# the last row has custom values in it, which is why it isnt getting deleted 
# will handle that later. 

# Can pass in mulit subset args so that it needs the last or the email
    # this one has how set to all, which means both subsets would need to be missing for a row to be dropped.
    # again need to set inplace=True if you want these changes to take effect. 
# print(df2.dropna(axis='index', how='all', subset=['last', 'email']))
#    first      last                email      age
# 0   cody   johnson   cjohnson@email.com       33
# 1   jane       doe    janedoe@email.com       55
# 2   john       doe    johndoe@email.com       63
# 3  Chris  Schafter                 None       36
# 5   None       NaN  anonymous@email.com     None
# 6     NA   Missing                   NA  Missing

# to handle custom missing values with this dataset you can just replace the "NA" string with np.nan
    # np.nan is from the numpy library 
# df2.replace('NA', np.nan, inplace=True)
# df2.replace('Missing', np.nan, inplace=True)
# print(df2)
#    first      last                email   age
# 0   cody   johnson   cjohnson@email.com    33
# 1   jane       doe    janedoe@email.com    55
# 2   john       doe    johndoe@email.com    63
# 3  Chris  Schafter                 None    36
# 4    NaN       NaN                  NaN  None
# 5   None       NaN  anonymous@email.com  None
# 6    NaN       NaN                  NaN   NaN

# print(df2.dropna())
#   first     last               email age
# 0  cody  johnson  cjohnson@email.com  33
# 1  jane      doe   janedoe@email.com  55
# 2  john      doe   johndoe@email.com  63

# if you want a mask of values to see if there are NA values you can use isna()
    # see what values are classified as NA
# print(df2.isna())
#    first   last  email    age
# 0  False  False  False  False
# 1  False  False  False  False
# 2  False  False  False  False
# 3  False  False   True  False
# 4   True   True   True   True
# 5   True   True  False   True
# 6  False  False  False  False

# if you want to fill NA values with something else you can use the fillna('value')
    # great for numerical data so you can replace a NA with a zero or something else. 
    # make sure to set inplace=True
# print(df2.fillna("MISSING"))
#      first      last                email      age
# 0     cody   johnson   cjohnson@email.com       33
# 1     jane       doe    janedoe@email.com       55
# 2     john       doe    johndoe@email.com       63
# 3    Chris  Schafter              MISSING       36
# 4  MISSING   MISSING              MISSING  MISSING
# 5  MISSING   MISSING  anonymous@email.com  MISSING
# 6       NA   Missing                   NA  Missing

# to handle data that is the wrong data type like for instance all of our ages are strings.
    # obj ususally means it is a string or something else. 
# print(df2.dtypes)
# first    object
# last     object
# email    object
# age      object
# dtype: object

# if you have nan data types and you need to do math you must remember that nan is considered a float. 
    # so if you try to convert the age column into an int it will throw an error b/c it cant convert the nan
# print(type(np.nan)) # <class 'float'>
# df2['age'] = df2['age'].astype(int)
# print(df2) # you get an error: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

# so you might want to keep the other values as floats so you dont mess up the agg functions, which means
# you can keep the nan values. 
# df2.replace('NA', np.nan, inplace=True)
# df2.replace('Missing', np.nan, inplace=True)
# df2['age'] = df2['age'].astype(float)
# print(df2.dtypes)
# first     object
# last      object
# email     object
# age      float64
# dtype: object

# print(df2['age'].mean()) # 46.75

# WORKING WITH CSV
    # you can pass in a arg with a list of values on how you want them to be treated as missing. 
# na_vals =['NA', 'Missing']
# df = pd.read_csv("unclean/test_online_retail.csv", na_values=na_vals)

# Casting values
# can use the .unique() method to see all of the values in a column which can help you identify value
# print(df['StockCode'].unique())
# ['85048' '79323P' '79323W' '22041' '21232' '22064' '21871' '21523' '22350'
#  '22349' '22195' '22353' '48173C' '21755' '21754' '84879' '22119' '22142'
#  '22296' '22295' '22109' '22087' '85206A' '21895' '21896' '22083' '84946'
#  '84970S' '35751C' '72739B' '22114' '22212' '48187' '48195' '72741'
#  '85232D' '85049E' '21976' '21498' '22077' '84948' '21537' '21733']

# print(df['Description'].unique())

# ***************** Working with Dates and Time Series Data ***********************
# Usually your datetime is stored as a string or some mixed value so you need to convert to a datetime format. 
# print(df.loc[0, "InvoiceDate"]) # 2009-12-01 07:45:00
# print(df.dtypes) # dtype: object

# To actually convert you can use the pandas to_datetime along with pythons strftime() code methods. 
# for this example the datetime is stored in the format of year,month,day and hour,min,sec
# So you would use the following codes from the python strftime() method, which are Y,m,d and H,M,S
# df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format = '%Y-%m-%d %H:%M:%S')
# printing out the updated column showing that the column has been coverted to a datetime obj
# print(df['InvoiceDate'].head(10))
# 0   2009-12-01 07:45:00
# 1   2009-12-01 07:45:00
# 2   2009-12-01 07:45:00
# 3   2009-12-01 07:45:00
# 4   2009-12-01 07:45:00
# 5   2009-12-01 07:45:00
# 6   2009-12-01 07:45:00
# 7   2009-12-01 07:45:00
# 8   2009-12-01 07:46:00
# 9   2009-12-01 07:46:00
# Name: InvoiceDate, dtype: datetime64[ns]

# Now that we have converted the strings into a datetime we can use some datetime methods. 
# print(df.loc[0, 'InvoiceDate'].day_name()) # Tuesday
# so the first entry has a day of Tuesday

# Can also instert args into the read_csv line 
# need to pass it in as a function that converts to a datetime obj as you cant just pass in a format string
# d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
# df = pd.read_csv("unclean/test_online_retail.csv", parse_dates=["InvoiceDate"], date_parser=d_parser)
# print(df.head(10))
#   Invoice StockCode                          Description  Quantity         InvoiceDate  Price  Customer ID         Country
# 0  489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12 2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1  489434    79323P                   PINK CHERRY LIGHTS        12 2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2  489434    79323W                  WHITE CHERRY LIGHTS        12 2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3  489434     22041         RECORD FRAME 7" SINGLE SIZE         48 2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4  489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24 2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5  489434     22064           PINK DOUGHNUT TRINKET POT         24 2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6  489434     21871                  SAVE THE PLANET MUG        24 2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 7  489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10 2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8  489435     22350                            CAT BOWL         12 2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9  489435     22349       DOG BOWL , CHASING BALL DESIGN        12 2009-12-01 07:46:00   3.75      13085.0  United Kingdom
# print(df["InvoiceDate"].dtypes) # datetime64[ns]

# So we saw that you can find out the day of the week on a single row but what if you wanted the days for all items in a column.
# you can access the dt class on the Series obj. and access the datetime methods that way. 
# first you have to convert the strings into a datetime 
# df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format = '%Y-%m-%d %H:%M:%S')
# so now you access the dt class on the Series obj with the dot method and then the method you want
# print(df['InvoiceDate'].dt.day_name().head(10))
# 0    Tuesday
# 1    Tuesday
# 2    Tuesday
# 3    Tuesday
# 4    Tuesday
# 5    Tuesday
# 6    Tuesday
# 7    Tuesday
# 8    Tuesday
# 9    Tuesday
# Name: InvoiceDate, dtype: object

# to create a new column with this information you can:
# df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
# print(df.head(10))
#   Invoice StockCode                          Description  Quantity         InvoiceDate  Price  Customer ID         Country DayOfWeek
# 0  489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12 2009-12-01 07:45:00   6.95      13085.0  United Kingdom   Tuesday
# 1  489434    79323P                   PINK CHERRY LIGHTS        12 2009-12-01 07:45:00   6.75      13085.0  United Kingdom   Tuesday
# 2  489434    79323W                  WHITE CHERRY LIGHTS        12 2009-12-01 07:45:00   6.75      13085.0  United Kingdom   Tuesday
# 3  489434     22041         RECORD FRAME 7" SINGLE SIZE         48 2009-12-01 07:45:00   2.10      13085.0  United Kingdom   Tuesday
# 4  489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24 2009-12-01 07:45:00   1.25      13085.0  United Kingdom   Tuesday
# 5  489434     22064           PINK DOUGHNUT TRINKET POT         24 2009-12-01 07:45:00   1.65      13085.0  United Kingdom   Tuesday
# 6  489434     21871                  SAVE THE PLANET MUG        24 2009-12-01 07:45:00   1.25      13085.0  United Kingdom   Tuesday
# 7  489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10 2009-12-01 07:45:00   5.95      13085.0  United Kingdom   Tuesday
# 8  489435     22350                            CAT BOWL         12 2009-12-01 07:46:00   2.55      13085.0  United Kingdom   Tuesday
# 9  489435     22349       DOG BOWL , CHASING BALL DESIGN        12 2009-12-01 07:46:00   3.75      13085.0  United Kingdom   Tuesday

# Can also now you min, max methods to narrow search information 
# min() will give you the oldest date in your data set. 
# print(df['InvoiceDate'].min()) # 2009-12-01 07:45:00

# to view most recent date can run the max().
# print(df["InvoiceDate"].max()) # 2009-12-01 11:50:00

# Can also get the difference between dates which will give you a time delta
# print(df["InvoiceDate"].max() - df['InvoiceDate'].min()) # 0 days 04:05:00

# Can also make some filters to get ranges of dates. 
# filt = (df['InvoiceDate'] >= '2009')
# print(df.loc[filt]) # prints everything as there is no other year in this dataset. 
# can also have multi 
# filt = (df['InvoiceDate'] >= '2009') & (df['InvoiceDate'] < '2010')
# filt = (df['InvoiceDate'] >= datetime('2009-12-01')) & (df['InvoiceDate'] < datetime('2009-12-02'))

# Can also slice by setting the invoice to the index then slicing the date you want
# df.set_index('InvoiceDate', inplace=True)
# df.sort_index(inplace=True)
# df['2020-01':'2020-02']
# You can then get analytics fromt the data 
# df['2009-01':'2009-02']['Price'].mean() #this would get you the avg price for all of those rows. 

# Can find the highest value for a day
# print(df.loc['2009-12-01'].max())
# Invoice                             C489449
# StockCode                            85232D
# Description    WHITE CHOCOLATE SCENT CANDLE
# Quantity                                 48
# Price                                  6.95
# Customer ID                         16321.0
# Country                      United Kingdom
# DayOfWeek                           Tuesday
# dtype: object

# **************** Reading/Writing Data to Different Sources - Excel, JSON, SQL, Etc ***************
# If you want to export your data to a new csv file you can use the 'to_csv' method

# say you want just the data from the united kindom
# you could create a filter where you just take the data from the country column. 
# filt = (df["Country"] == 'United Kingdom')
# uk_df = df.loc[filt]
# print(uk_df.head(10))
#   Invoice StockCode                          Description  Quantity          InvoiceDate  Price  Customer ID         Country
# 0  489434     85048  15CM CHRISTMAS GLASS BALL 20 LIGHTS        12  2009-12-01 07:45:00   6.95      13085.0  United Kingdom
# 1  489434    79323P                   PINK CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 2  489434    79323W                  WHITE CHERRY LIGHTS        12  2009-12-01 07:45:00   6.75      13085.0  United Kingdom
# 3  489434     22041         RECORD FRAME 7" SINGLE SIZE         48  2009-12-01 07:45:00   2.10      13085.0  United Kingdom
# 4  489434     21232       STRAWBERRY CERAMIC TRINKET BOX        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 5  489434     22064           PINK DOUGHNUT TRINKET POT         24  2009-12-01 07:45:00   1.65      13085.0  United Kingdom
# 6  489434     21871                  SAVE THE PLANET MUG        24  2009-12-01 07:45:00   1.25      13085.0  United Kingdom
# 7  489434     21523   FANCY FONT HOME SWEET HOME DOORMAT        10  2009-12-01 07:45:00   5.95      13085.0  United Kingdom
# 8  489435     22350                            CAT BOWL         12  2009-12-01 07:46:00   2.55      13085.0  United Kingdom
# 9  489435     22349       DOG BOWL , CHASING BALL DESIGN        12  2009-12-01 07:46:00   3.75      13085.0  United Kingdom

# now to export this info to a new csv file you use the to_cvs method
# uk_df.to_csv('clean/test_uk_data.csv')

# if you want a tab seperated file:
# uk_df.to_csv('clean/test_uk_data.csv', sep='\t')

# to export to excel, you need to install the packages: xlwt, openpyxl, xlrd with pip install
# uk_df.to_csv('clean/test_uk_data.xlsx')
# can pass in arg to export to different sheets in excel

# to import excel and set index to customer ID
# test = pd.read_excel('clean/test_uk_data.xlsx', index_col="Customer ID")

# Can also do json
# uk_df.to_json('clean/test_uk_data.json')
# can set to list like instead of dictionary like
# uk_df.to_json('clean/test_uk_data.json', orient='records', lines=True)
# if you want other args to orient, look up pandas to json method

# to read/write to SQL database you need to install SQLAlchemy and psycopg2-binary with pip install
# To create a table in postgress: 
# from sqlalchemy import create_engine
# import psycopg2
# engine = create_engine('postgresql://dbuser:dbpass@localhost:port#/databasename')
# uk_df.to_sql('table_name', engine)

# can add args if the table exist so you can write over it.  
# uk_df.to_sql('table_name', engine, if_exists='replace')
# there are other options beside replace 

# can also set the index
# uk_df.to_sql('table_name', engine, if_exists='replace', index_column="name_of_column")

# Can also load in from a url
# posts_df = pd.read_csv('https://www.url.com')
