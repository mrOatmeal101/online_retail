USE online_retail;
GO

DROP TABLE IF EXISTS stage_online_retail;
GO

CREATE TABLE stage_online_retail(
invoice_number VARCHAR (50),
stock_code VARCHAR (50),
description_text NVARCHAR (1000),
quantity INT,
invoice_date DATETIME,
price MONEY,
customer_id BIGINT,
country VARCHAR(255)
);
GO

PRINT 'Starting Bulk Insert';
BULK INSERT stage_online_retail -- which table to insert the data into
FROM 'C:\sql_datasets\online_retail_II\cleaned_online_retail_II.csv'
WITH (
	FORMAT='CSV',
	FIELDTERMINATOR = ',', -- stating that the columns in the csv are separated by commas (,)
	ROWTERMINATOR = '0x0a', -- stating that the rows in the csv end with a new line i.e., \n
	FIELDQUOTE = '"',
	FIRSTROW = 2 -- seting to 2 to skip the title column in the csv file
);
PRINT 'Bulk Insert Finished';
PRINT @@ROWCOUNT;
GO