from bs4 import BeautifulSoup
import numpy as np
import requests, os, sqlite3
from datetime import datetime
import pandas as pd

# CONSTANTS

LOGFILE = rf"{os.getcwd()}/docs/code_log.txt"



# FUNCTIONS

def log_progress(LOGFILE, message):
    time_date = datetime.datetime()
    with open(LOGFILE, 'a') as file_in:
        file_in.write(f'{time_date} : {message}')


response_archive = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')
soup = BeautifulSoup(response_archive.text, 'html.parser')
headings_tags = ['h1','h2','h3']
heading = soup.find('h2', string='By market capitalization')
table = heading.find_next('table')
data = []
columns = [header.text for header in table.find_next('th')]
for row in table.find_all('tr'):
    row_data = []
    columns.append(row.find_all('th'))
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    data.append(row_data)
df = pd.DataFrame(data)
print(df)
#print(soup.prettify)

# response_wiki = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')
# print(response_wiki.status_code)
# soup_wiki = BeautifulSoup(response_archive.text, 'html.parser')
# print(soup_wiki.prettify)









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


