# This is data cleaning application

"""
**Requirements**
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

# importing dependencies

import pandas as pd
import numpy as np
import time
import random
import openpyxl
import xlrd
import os

# data_path = 'day19_sales.xlsx'
# data_name = 'jan_sales'

def data_cleaning_master(data_path, data_name):
    print('Thank you for giving the details')

    sec = random.randint(1, 4) # generating random number

    # print delay message
    print(f"Please wait for {sec} seconds! Checking file path")
    time.sleep(sec)

    # checking if the path exists
    if not os.path.exists(data_path):
        print('Incorrect path. Please try again with correct path')
        return
    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv')
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Dataset is an excel file')
            data = pd.read_excel(data_path)
        else:
            print('Unknown file type')
            return
        
        # print delay message
    sec = random.randint(1, 4)   
    print(f"Please wait for {sec} seconds! Checking for total number of columns and rows")
    time.sleep(sec)

    # showing number of records
    print(f"Dataset contains total rows: {data.shape[0]} \nTotal columns: {data.shape[1]}")

    # start cleaning


    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec} seconds! Checking for total duplicates")
    time.sleep(sec)

    # # checking duplicates
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()
    print(f"Datasets has total duplicates records: {total_duplicate}")

    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec} seconds! Saving total duplicate rows")
    time.sleep(sec)

    # saving the duplicates
    if total_duplicate > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', header=None)

    # deleting duplicates
    df = data.drop_duplicates()

    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec} seconds! Checking for missing values")
    time.sleep(sec)


    # find missing values
    total_missing_value = df.isnull().sum().sum()
    missing_value_by_columns = df.isnull().sum()

    print(f'Dataset has total missing value: {total_missing_value}')
    print(f'Dataset contain missing value by column: \n {missing_value_by_columns}')

    # dealing with missing values
    # fillna -- int and float
    # dropna -- any other object type

    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec} seconds! Cleaning datasets")
    time.sleep(sec)

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in (int, float):
            df[col] = df[col].fillna(df[col].mean())
        else:
            # dropping all rows with missing records for non number columns
            df.dropna(subset=col, inplace=True)


    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec} seconds! Exporting datasets")
    time.sleep(sec)

    # data is cleaned

    print(f'Congrats! Data set is cleaned! \nNumber of rows: {df.shape[0]} Number of columns: {df.shape[1]}')

    # saving the clean dataset
    df.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("Dataset is saved!")


if __name__ == "__main__":


    print("Welcome to Data Cleaning Master!")
    # asking name and file path
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")

    # calling the function
    data_cleaning_master(data_path, data_name)