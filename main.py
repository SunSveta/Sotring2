import csv
import pandas as pd

def select_sorted(sort_columns = ['high'] , limit = 5 , group_by_name = False , order = 'desc' , filename = 'dump.csv'):
    df = pd.read_csv('all_stocks_5yr.csv')
    if order == 'desc':
        df_sorted = df.sort_values(by=sort_columns, ignore_index=True, ascending=False)
        df_sorted.head(limit).to_csv(r'C:\Users\Светлана\PycharmProjects\pythonProject5\dump.csv', index=False, sep='|')
    else:
        df_sorted = df.sort_values(by=sort_columns, ignore_index=True)
        df_sorted.head(limit).to_csv(r'C:\Users\Светлана\PycharmProjects\pythonProject5\dump.csv', index=False, sep='|')

select_sorted(sort_columns = ['high'] , limit = 8 , order = 'asc' , filename = 'dump.csv')