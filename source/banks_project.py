from bs4 import BeautifulSoup
import numpy as np
import requests, os, sqlite3
from datetime import datetime


# CONSTANTS

LOGFILE = rf"{os.getcwd()}/docs/code_log.txt"



# FUNCTIONS

def log_progress(LOGFILE, message):
    time_date = datetime.datetime()
    with open(LOGFILE, 'a') as file_in:
        file_in.write(f'{time_date} : {message}')


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
soup = url.prettify
print(soup)










# def extract(url, table_attribs):
#     ''' This function aims to extract the required
#     information from the website and save it to a data frame. The
#     function returns the data frame for further processing. '''
#     return df
# def transform(df, csv_path):
#     ''' This function accesses the CSV file for exchange rate
#     information, and adds three columns to the data frame, each
#     containing the transformed version of Market Cap column to
#     respective currencies'''
#     return df
# def load_to_csv(df, output_path):
#     ''' This function saves the final data frame as a CSV file in
#     the provided path. Function returns nothing.'''
# def load_to_db(df, sql_connection, table_name):
#     ''' This function saves the final data frame to a database
#     table with the provided name. Function returns nothing.'''
# def run_query(query_statement, sql_connection):
#     ''' This function runs the query on the database table and
#     prints the output on the terminal. Function returns nothing. '''
# ''' Here, you define the required entities and call the relevant
# functions in the correct order to complete the project. Note that this
# portion is not inside any function.'''




# if __name__ == "__main__":
#     main()


