import pandas as pd
import pyodbc

# Define database connection parametersNEWNEW
server = 'DESKTOP-1J63TNT\\MSSQLSERVER2022'
database = 'AdventureWorks'
table = 'Sales.SalesPerson'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Read the CSV file into a DataFrame
csv_file_path = r'C:\Users\admin\Downloads\SalesPerson.csv'
csv_data = pd.read_csv(csv_file_path)

# Connect to SQL Server and query the table
with pyodbc.connect(connection_string) as conn:
    query = f"SELECT * FROM {table}"
    sql_data = pd.read_sql(query, conn)

# Drop the ModifiedDate column from both DataFrames
if 'ModifiedDate' in csv_data.columns:
    csv_data = csv_data.drop(columns=['ModifiedDate'])

if 'ModifiedDate' in sql_data.columns:
    sql_data = sql_data.drop(columns=['ModifiedDate'])

# Compare the two DataFrames
comparison_result = csv_data.compare(sql_data)

# Output the results
if comparison_result.empty:
    print("The records in the SQL table and the CSV file are identical (excluding ModifiedDate).")
else:
    print("Differences found between the SQL table and the CSV file:")
    print(comparison_result)
