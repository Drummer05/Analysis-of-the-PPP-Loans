#!/usr/bin/env python
# coding: utf-8

# ### Data Transformation
# 
# 1. Remove Duplicates.
# 2. Change the data type of some columns
# 3. Check and treat null values.
# 4. Estandarized column names.
# 5. Estandarized string data values for some columns
# 6. Create a year, month, day from date columns. 

# In[ ]:


# Packages 
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO  
import re


# In[3]:


# Get the data from my azure storage account, merged all the csv files and create a dataframe to transform the data

def load_and_combine_csv_from_azure(account_name, account_key, container_name):
    # Create a BlobServiceClient using account credentials
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

    # Access the container
    container_client = blob_service_client.get_container_client(container_name)

    # List all blobs (files) in the container, filtering for CSV files
    blob_list = container_client.list_blobs()
    csv_files = [blob.name for blob in blob_list if blob.name.endswith('.csv')]

    # Initialize an empty list to store DataFrames
    dataframes = []

    # Loop through CSV files, read each into a DataFrame and append to the list
    for file in csv_files:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
        stream = blob_client.download_blob().readall()
        df = pd.read_csv(StringIO(stream.decode('utf-8')))
        dataframes.append(df)

    # Combine all DataFrames into one
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

# Usage
account_name = 'stcis4400projects'
account_key = 'y6gnspi1EMeRxEE4Jin3BfaIu6fOd7NMW9RfU1n04fHfcZARGLzlEM4aWeoribo7U2YMTG58nNzh+ASt+LLOGw=='
container_name = 'pppdata'
combined_df = load_and_combine_csv_from_azure(account_name, account_key, container_name)

# Now 'combined_df' contains all the data from the CSV files


# In[4]:


combined_df.head()


# In[5]:


# Let's see the shape of the ppp loans dataframe
combined_df.shape


# In[6]:


# check the data types of all the columns
data_types = combined_df.dtypes
print(data_types)


# In[8]:


# Selecting only columns that are of int or float data type
numeric_columns_df = combined_df.select_dtypes(include=['int', 'float'])

# Printing the first few rows of the numeric columns
print(numeric_columns_df.head())


# In[10]:


# Convert specified columns to 'Int32' data type
combined_df['LoanNumber'] = combined_df['LoanNumber'].astype('int32')
combined_df['SBAOfficeCode'] = combined_df['SBAOfficeCode'].astype('Int32')
combined_df['OriginatingLenderLocation_ID'] = combined_df['OriginatingLenderLocationID'].astype('Int32')
combined_df['NAICSCode'] = combined_df['NAICSCode'].astype('Int64')
combined_df['ServicingLenderLocationID'] = combined_df['ServicingLenderLocationID'].astype('Int32')
combined_df['JobsReported'] = combined_df['JobsReported'].astype('Int32')

# List of columns to change to float32
columns_to_convert = [
    'UTILITIES_PROCEED', 'PAYROLL_PROCEED', 'MORTGAGE_INTEREST_PROCEED', 
    'RENT_PROCEED', 'REFINANCE_EIDL_PROCEED', 'HEALTH_CARE_PROCEED', 
    'DEBT_INTEREST_PROCEED'
]

# Convert each specified column to 'float32'
for column in columns_to_convert:
    combined_df[column] = combined_df[column].astype('float32')

# Verify the change
print(combined_df.dtypes)


# In[ ]:


"""Counting the number of duplicate rows"""

# No duplicate rows found
duplicate_count = duplicates.sum()
print(f"Number of duplicate rows: {duplicate_count}")


# In[13]:


"""Checking for null values"""

# A lot of null Values found
null_counts = combined_df.isnull().sum()
print(null_counts)


# In[14]:


"""Remove columns from the dataset where over half of the entries are missing. In other words, 
if more than 50% of the rows in any column do not have data (are null), that entire column will
be eliminated from the dataset.""""

# Calculate the percentage of null values in each column
null_percentage = (combined_df.isnull().sum() / len(combined_df)) * 100

# Identify columns where the percentage of null values is greater than 50%
columns_to_drop = null_percentage[null_percentage > 50].index

# Drop these columns from the DataFrame
combined_df = combined_df.drop(columns=columns_to_drop)

# Print remaining columns to verify
print(combined_df.columns)


# #### Columns Deleted:
# 
# 1. UTILITIES_PROCEED                               
# 2. MORTGAGE_INTEREST_PROCEED      
# 3. RENT_PROCEED                   
# 4. REFINANCE_EIDL_PROCEED         
# 5. HEALTH_CARE_PROCEED            
# 6. DEBT_INTEREST_PROCEED
# 7. FranchiseName
# 8. NonProfit

# In[17]:


"""Replace null values of the numeric columns with the mean of these columns."""

# Calculating the mean of 'ForgivenessAmount'
forgiveness_amount_mean = combined_df['ForgivenessAmount'].mean()

# Replacing null values in 'ForgivenessAmount' with its mean
combined_df['ForgivenessAmount'] = combined_df['ForgivenessAmount'].fillna(forgiveness_amount_mean)


# Calculating the mean of 'PAYROLL_PROCEED'
PAYROLL_PROCEED_mean = combined_df['PAYROLL_PROCEED'].mean()

# Replacing null values in 'PAYROLL_PROCEED' with its mean
combined_df['PAYROLL_PROCEED'] = combined_df['PAYROLL_PROCEED'].fillna(PAYROLL_PROCEED_mean)


# Calculating the mean of 'ForgivenessAmount'
Undisbursed_Amount_mean = combined_df['UndisbursedAmount'].mean()

# Replacing null values in 'ForgivenessAmount' with its mean
combined_df['UndisbursedAmount'] = combined_df['UndisbursedAmount'].fillna(Undisbursed_Amount_mean)


# In[18]:


# doble check if the code worked
null_counts = combined_df.isnull().sum()
print(null_counts)


# In[19]:


"""Standarization of column names and string data"""

def add_underscores_to_column_names(df):
    # Define a function to insert underscores
    def insert_underscores(name):
        # Replace occurrences where a lowercase letter is followed by an uppercase letter
        # with the same characters separated by an underscore
        modified_name = re.sub('([a-z])([A-Z])', r'\1_\2', name)
        return modified_name

    # Apply the function to each column name
    new_column_names = {col: insert_underscores(col) for col in df.columns}
    
    # Rename the columns of the DataFrame
    df.rename(columns=new_column_names, inplace=True)
    
# Rename the 'PAYROLL_PROCEED' column to 'Payroll_Proceed'
combined_df.rename(columns={'PAYROLL_PROCEED': 'Payroll_Proceed'}, inplace=True)

# Example usage
# combined_df is your existing DataFrame
add_underscores_to_column_names(combined_df)
print(combined_df.columns)


# In[23]:


def standardize_string_columns_to_proper_case(df):
    # Custom function to handle strings with special characters
    def proper_case_with_special_handling(s):
        if '-' in s:
            return '-'.join([part.title() for part in s.split('-')])
        else:
            return s.title()

    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column's data type is 'object'
        if df[column].dtype == 'object':
            # Apply the proper case conversion only to string values
            df[column] = df[column].apply(lambda x: proper_case_with_special_handling(x) if isinstance(x, str) else x)

standardize_string_columns_to_proper_case(combined_df)


# In[25]:


def uppercase_state_columns(df, column_names):
    # Iterate over the list of column names
    for column_name in column_names:
        # Check if the specified column exists in the DataFrame
        if column_name in df.columns:
            # Convert the values in the column to uppercase
            df[column_name] = df[column_name].str.upper()
        else:
            print(f"Column '{column_name}' not found in the DataFrame.")

state_columns = ['Originating_Lender_State', 'Originating_Lender_Location_State', 'Borrower_State',]
uppercase_state_columns(combined_df, state_columns)


# In[27]:


def uppercase_processing_method(df, column_name='Processing_Method'):
    # Check if the specified column exists in the DataFrame
    if column_name in df.columns:
        # Convert the values in the column to uppercase
        df[column_name] = df[column_name].str.upper()
    else:
        print(f"Column '{column_name}' not found in the DataFrame.")

uppercase_processing_method(combined_df)


# In[28]:


# check if the code worked
combined_df.head()


# In[29]:


# Selecting only string (object) columns
string_columns_df = combined_df.select_dtypes(include=['object'])

# Displaying the first few rows of the DataFrame with only string columns
print(string_columns_df.head())


# In[30]:


"""Create a year, month, and day column from the following columns:"""

# Ensure the date columns are in datetime format
combined_df['Date_Approved'] = pd.to_datetime(combined_df['Date_Approved'], errors='coerce')
combined_df['Forgiveness_Date'] = pd.to_datetime(combined_df['Forgiveness_Date'], errors='coerce')
combined_df['Loan_Status_Date'] = pd.to_datetime(combined_df['Loan_Status_Date'], errors='coerce')

# Extract year, month, and day for 'Date_Approved'
combined_df['Date_Approved_Year'] = combined_df['Date_Approved'].dt.year
combined_df['Date_Approved_Month'] = combined_df['Date_Approved'].dt.month
combined_df['Date_Approved_Day'] = combined_df['Date_Approved'].dt.day

# Extract year, month, and day for 'Forgiveness_Date'
combined_df['Forgiveness_Date_Year'] = combined_df['Forgiveness_Date'].dt.year
combined_df['Forgiveness_Date_Month'] = combined_df['Forgiveness_Date'].dt.month
combined_df['Forgiveness_Date_Day'] = combined_df['Forgiveness_Date'].dt.day

# Extract year, month, and day for 'Loan_Status_Date'
combined_df['Loan_Status_Date_Year'] = combined_df['Loan_Status_Date'].dt.year
combined_df['Loan_Status_Date_Month'] = combined_df['Loan_Status_Date'].dt.month
combined_df['Loan_Status_Date_Day'] = combined_df['Loan_Status_Date'].dt.day



# change data type to integer
combined_df['Forgiveness_Date_Month'] = combined_df['Forgiveness_Date_Month'].astype('Int64')
combined_df['Forgiveness_Date_Day'] = combined_df['Forgiveness_Date_Day'].astype('Int64')
combined_df['Forgiveness_Date_Year'] = combined_df['Forgiveness_Date_Year'].astype('Int64')


combined_df['Date_Approved_Month'] = combined_df['Date_Approved_Month'].astype('Int64')
combined_df['Date_Approved_Year'] = combined_df['Date_Approved_Year'].astype('Int64')
combined_df['Date_Approved_Day'] = combined_df['Date_Approved_Day'].astype('Int64')


combined_df['Loan_Status_Date_Year'] = combined_df['Loan_Status_Date_Year'].astype('Int64')
combined_df['Loan_Status_Date_Month'] = combined_df['Loan_Status_Date_Month'].astype('Int64')
combined_df['Loan_Status_Date_Day'] = combined_df['Loan_Status_Date_Day'].astype('Int64')

# Display the first few rows to verify
print(combined_df.head())


# In[42]:


# take a look at the clean data
combined_df.head()


# In[54]:


# Export the clean data 

combined_df.to_csv('C:\\Users\\c.silverio\\Desktop\\ppp_loans_clean_data\\PPP_Loans_Data_Clean.csv', index=False)


# In[ ]:




