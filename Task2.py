import csv
import pandas as pd

def like_a_cache(func): #декоратор для сохранения кеша
    cache = {}
    def wrapper(**kwargs):
        if tuple(kwargs) in cache:
            return cache[tuple(kwargs)]
        else:
            cache[tuple(kwargs)] = func(**kwargs)
            return cache[tuple(kwargs)]
    return wrapper

@like_a_cache
def select_sorted(sort_columns=['high'], limit=5, group_by_name=False, order='desc', filename='dump2.csv'):
    df = pd.read_csv('all_stocks_5yr.csv') #преобразовывает данные из файли csv в dataframe
    if order == 'desc':  #сортировка по убыванию
        df_sorted = df.sort_values(by=sort_columns, ignore_index=True, ascending=False)
    else: #по убыванию
        df_sorted = df.sort_values(by=sort_columns, ignore_index=True)

    df_sorted.head(limit).to_csv(r'C:\Users\Светлана\PycharmProjects\pythonProject5\dump2.csv', mode = 'a', index=False, sep='|')


select_sorted(sort_columns = ['high'] , limit = 4 , order = 'asc' , filename = 'dump2.csv')
select_sorted(sort_columns = ['open'] , limit = 6 , order = 'asc' , filename = 'dump2.csv')
select_sorted(sort_columns = ['high'] , limit = 4 , order = 'asc' , filename = 'dump2.csv')
# функции, на которых я проверяла работу. В файл все равно записалось три раза, но я не знаю, как проверить, откуда записалась информация 3-й раз.