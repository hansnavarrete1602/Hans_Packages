from typing import *
from Hans_Packages import Foldpy as fold, Snum as nx, FileSelect as fc
from pathlib import Path
import pandas as pd
from os import system
import time as t


def select_file(direccion, ext):
    while True:
        try:
            system('cls')
            a = fold.all_search_file(direccion, ext)
            if len(a) > 0:
                for i in range(len(a)):
                    print(f'[{i + 1}]. {Path(a[i]).name}')
                c = fold.elegir_(a)
                system('cls')
                d = input(f'¿Este archivo tiene mas de una Hoja de calculo?\nPorfavor seleccione [S/N]: ')
                if d.lower() in ['s', 'n']:
                    if d.lower() == 's':
                        e = input(f'Ingrese el nombre de la hoja que desea abrir: ')
                        system('cls')
                        df = pd.read_excel(c, sheet_name=e)
                        return df
                    else:
                        system('cls')
                        df = pd.read_excel(c)
                        return df
                else:
                    system('cls')
                    print('Seleccione una opcion valida...')
                    t.sleep(2)
                    continue
            system('cls')
            print('No file founds')
            break
        except ImportError:
            system('cls')
            print('Falta instalar el modulo "openpyxl"')
            break
        except:
            pass


def open_dataframe(type, *args):
    if type == 'excel':
        return pd.read_excel(fc.select_file(), *args)
    elif type == 'csv':
        return pd.read_csv(fc.select_file())
    elif type == 'html':
        return pd.read_html(fc.select_file(), *args)


def view_columns(df: Any) -> List:
    """

    :param df: dataframe
    :rtype: List

    """
    return df.columns.tolist()


def df_size(df: Any) -> str:
    """

    :param: dataframe
    :rtype: str

    """
    return f'''
    {'*' * 20}
    \tColumns: {df.shape[1]}
    \tRows: {df.shape[0]}
    Total data: {df.size}
    {'*' * 20}
    '''


def basic_function_dataframe(df: Any, **kwargs: [Text]) -> Any:
    """

    :param df: dataframe

    :type kwargs: Dict{
    'mode':
    ['max','min','count','mean','median','sum','unique','describe','sort','diff','vcount']}
    if mode = 'describe' -> additional optionals kwargs: 'types' or 'info' or 'shape'
    if mode = 'sort' -> additional optionals kwargs: 'by' and 'colName'
    if mode = 'diff' ->  additional optionals kwargs: 'colName'
    if mode = 'vcount' -> additional optionals kwargs: 'colName'

    :return Dataframe or str or int

    """
    if kwargs.get('mode') == 'max':
        return df[kwargs.get('colName')].max()
    if kwargs.get('mode') == 'min':
        return df[kwargs.get('colName')].min()
    elif kwargs.get('mode') == 'count':
        return df[kwargs.get('colName')].count()
    elif kwargs.get('mode') == 'mean':
        return df[kwargs.get('colName')].mean()
    elif kwargs.get('mode') == 'median':
        return df[kwargs.get('colName')].median()
    elif kwargs.get('mode') == 'sum':
        return df[kwargs.get('colName')].sum()
    elif kwargs.get('mode') == 'unique':
        return df[kwargs.get('colName')].nunique()
    elif kwargs.get('mode') == 'sort':
        return df.sort_values(by=kwargs.get('by'), ascending=kwargs.get('ascending'))
    elif kwargs.get('mode') == 'describe':
        return df.describe()
    elif kwargs.get('mode') == 'head':
        return df.head()
    elif kwargs.get('mode') == 'types':
        return df.dtypes
    elif kwargs.get('mode') == 'info':
        return df.info()
    elif kwargs.get('mode') == 'shape':
        return df.shape
    elif kwargs.get('mode') == 'diff':
        return df[kwargs.get('colName')].diff()
    elif kwargs.get('mode') == 'vcount':
        return df[kwargs.get('colName')].value_counts()
    else:
        return df


def df_walk(df: Any, **kwargs: [Text]) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    mode -> 'FromTo' -> need: start, stop, colName
    mode -> 'From' -> need: start, colName
    mode -> 'To' -> need: stop, colName
    only 'colName' -> all column data
    :return: dataframe if exist, else return None

    """
    try:
        if kwargs.get('mode') == 'FromTo':
            return df[kwargs.get('colName')][kwargs.get('start'):kwargs.get('stop')]
        elif kwargs.get('mode') == 'From':
            return df[kwargs.get('colName')][kwargs.get('start'):]
        elif kwargs.get('mode') == 'To':
            return df[kwargs.get('colName')][:kwargs.get('stop')]
        else:
            return df[kwargs.get('colName')]
    except KeyError:
        return None


def basic_search(df: Any, *args: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param args: Any
    :param kwargs: colName -> str or List[str]
    :return: dataframe

    """
    return df[df[kwargs.get('colName')].isin(list(args))]


def basic_condition_search(df: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    mode:
    if mode = condition -> need condition, value, colName
    if mode = mask -> need mask
    :return: dataframe or None

    """
    if kwargs.get('mode') == 'condition':
        if kwargs.get('condition') == '>':
            return df[df[kwargs.get('colName')] > kwargs.get('value')]
        elif kwargs.get('condition') == '>=':
            return df[df[kwargs.get('colName')] >= kwargs.get('value')]
        elif kwargs.get('condition') == '<':
            return df[df[kwargs.get('colName')] < kwargs.get('value')]
        elif kwargs.get('condition') == '<=':
            return df[df[kwargs.get('colName')] <= kwargs.get('value')]
        elif kwargs.get('condition') == '=':
            return df[df[kwargs.get('colName')] == kwargs.get('value')]
        elif kwargs.get('condition') == '!':
            return df[df[kwargs.get('colName')] != kwargs.get('value')]
        else:
            return 'invalid condition'
    elif kwargs.get('mode') == 'mask':
        return df[kwargs.get('mask')]
    else:
        return None


def loc_functions(df: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    if mode = Rloc -> need condition like >,<,>=,<=,=,!; value for compare and Rcol(column for return)
    if mode = loc -> need condition like >,<,>=,<=,=,!; value for compare
    if mode = index -> need idxN -> list with index for search
    :return: dataframe

    """
    if kwargs.get('mode') == 'Rloc':
        if kwargs.get('condition') == '>':
            return df.loc[df[kwargs.get('colName')] > kwargs.get('value'), kwargs.get('Rcol')]
        elif kwargs.get('condition') == '>=':
            return df.loc[df[kwargs.get('colName')] >= kwargs.get('value'), kwargs.get('Rcol')]
        elif kwargs.get('condition') == '<':
            return df.loc[df[kwargs.get('colName')] < kwargs.get('value'), kwargs.get('Rcol')]
        elif kwargs.get('condition') == '<=':
            return df.loc[df[kwargs.get('colName')] <= kwargs.get('value'), kwargs.get('Rcol')]
        elif kwargs.get('condition') == '=':
            return df.loc[df[kwargs.get('colName')] == kwargs.get('value'), kwargs.get('Rcol')]
        elif kwargs.get('condition') == '!':
            return df.loc[df[kwargs.get('colName')] != kwargs.get('value'), kwargs.get('Rcol')]
        else:
            return 'invalid condition'
    elif kwargs.get('mode') == 'loc':
        if kwargs.get('condition') == '>':
            return df.loc[df[kwargs.get('colName')] > kwargs.get('value')]
        elif kwargs.get('condition')== '>=':
            return df.loc[df[kwargs.get('colName')] >= kwargs.get('value')]
        elif kwargs.get('condition') == '<':
            return df.loc[df[kwargs.get('colName')] < kwargs.get('value')]
        elif kwargs.get('condition') == '<=':
            return df.loc[df[kwargs.get('colName')] <= kwargs.get('value')]
        elif kwargs.get('condition') == '=':
            return df.loc[df[kwargs.get('colName')] == kwargs.get('value')]
        elif kwargs.get('condition') == '!':
            return df.loc[df[kwargs.get('colName')] != kwargs.get('value')]
        else:
            return 'invalid condition'
    elif kwargs.get('mode') == 'index':
        return df.loc[df.index[kwargs.get('idxN')]]
    else:
        return 'wich mode [loc, Rloc, index]?'


def search_in_all(df: Any, lst: List[Any], v: Any) -> List[Any]:
    """

    :param df: dataframe
    :param lst: List with columns
    :param v: Value for search
    :return: List[columns with value and index]

    """
    lst_2 = []
    for i in range(len(lst)):
        a = loc_functions(df, condition='=', value=v, colName=lst[i], Rcol=lst[i], mode='Rloc')
        if(len(a)) > 0:
            lst_2.append(a)
    return lst_2


def check_position_list(lst: List, v: List[Any]) -> List[Any]:
    """

    :param lst: list of data (single column)
    :param v: List of keys for search
    :return: List with the result index of searh for any key

    """
    lst_2 = []
    for i in range(len(v)):
        lst_2.append(nx.check_position(lst, v[i]))
    return lst_2


def iloc_functions(df: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    if mode = extract: -> need colName
        if low and top -> return dataframe with columns in colName in the range of low and top
        if low -> return dataframe with columns in colName in the range of low to end datframe
        if top -> return dataframe with columns in colName in the range of 0 to top
        if row -> return dataframe with columns in colName in the row
    if mode = update: -> need colName and value
        if low and top -> update dataframe with columns in colName in the range of low and top with the value
        if low -> update dataframe with columns in colName in the range of low to end dataframe with the value
        if top -> update dataframe with columns in colName in the range of 0 to top with the value
        if row -> update dataframe with columns in colName in the row with the value
    if mode = mask -> need mask and colName
        if value -> set the value to the columns in colName
        if not value -> return dataframe with conditions set
    :return: dataframe

    """
    if kwargs.get('mode') == 'extract':
        res = list(map(lambda sub: int(''.join(
            [ele for ele in sub if ele.isnumeric()])), check_position_list(df.columns.tolist(), kwargs.get('colName'))))
        if 'low' and 'top' in kwargs:
            return df_walk(df, colName=[df.columns.tolist()[i] for i in res]).iloc[kwargs.get('low'):kwargs.get('top')]
        elif 'low' in kwargs:
            return df_walk(df, colName=[df.columns.tolist()[i] for i in res]).iloc[
                   kwargs.get('low'):]
        elif 'top' in kwargs:
            return df_walk(df, colName=[df.columns.tolist()[i] for i in res]).iloc[
                   :kwargs.get('top')]
        elif 'row' in kwargs:
            return df_walk(df, colName=[df.columns.tolist()[i] for i in res]).iloc[kwargs.get('row')]
        else:
            return df_walk(df, colName=[df.columns.tolist()[i] for i in res]).iloc[:]
    elif kwargs.get('mode') == 'update':
        if 'low' and 'top' in kwargs:
            df.loc[kwargs.get('low'):kwargs.get('top'), kwargs.get('colName')] = kwargs.get('value')
            return df
        elif 'low' in kwargs:
            df.loc[kwargs.get('low'):, kwargs.get('colName')] = kwargs.get('value')
            return df
        elif 'top' in kwargs:
            df.loc[:kwargs.get('top'), kwargs.get('colName')] = kwargs.get('value')
            return df
        elif 'row' in kwargs:
            df.loc[kwargs.get('row'), kwargs.get('colName')] = kwargs.get('value')
            return df
        else:
            return df_walk(df, colName=[kwargs.get('colName')]).iloc[:]
    elif kwargs.get('mode') == 'mask':
        if 'value' in kwargs:
            mask = kwargs.get('mask')
            df.loc[mask, kwargs.get('colName')] = kwargs.get('value')
            return df
        else:
            mask = kwargs.get('mask')
            return df.loc[mask, kwargs.get('colName')]


def group_function(df: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    if mode = mean -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return mean of colName
    if mode = median -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return median of colName
    if mode = max -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return max of colName
    if mode = min -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return min of colName
    if mode = count -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return count of colName
    if mode = first -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return first of colName
    if mode = describe -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return describe of colName
    if mode = unique -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return unique of colName
    if mode = diff -> need
        colName: column for compare with group
        return diff of colName
    if mode = all -> need
        colName: column for compare with group
        return all of colName
    if mode = lambda -> need
        colGroup: list with columns for group
        colName: column for compare with group
        return lambda x:x of colName
    if mode = agg -> need
        return dataframe with agg
    :return: dataframe

    """
    if kwargs.get('mode') == 'mean':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].mean()
    elif kwargs.get('mode') == 'median':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].median()
    elif kwargs.get('mode') == 'max':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].max()
    elif kwargs.get('mode') == 'min':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].min()
    elif kwargs.get('mode') == 'min':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].sum()
    elif kwargs.get('mode') == 'count':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].count()
    elif kwargs.get('mode') == 'first':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].first()
    elif kwargs.get('mode') == 'describe':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].describe()
    elif kwargs.get('mode') == 'unique':
        return df.groupby(kwargs.get('colGroup'))[kwargs.get('colName')].nunique()
    elif kwargs.get('mode') == 'diff':
        return df.groupby(kwargs.get('colName'))[kwargs.get('colName')].diff()
    elif kwargs.get('mode') == 'all':
        return df.groupby(kwargs.get('colName'))[kwargs.get('colName')].head(n=len(df))
    elif kwargs.get('mode') == 'lambda':
        return df.groupby(kwargs.get('colGroup')).apply(lambda x:x)
    elif kwargs.get('mode') == 'agg':
        return df.agg(kwargs.get('agg'))
    else:
        return 'invalid condition'


def str_operations(df: Any, **kwargs: Any) -> Any:
    """

    :param df: dataframe
    :param kwargs:
    if mode = lower -> need colName:
        return column with str lower
    if mode = upper -> need colName
        return column with str upper
    if mode = len -> need colName
        return columns with count of character per row
    if mode = lenMax -> need colName
        return the size of the bigger string in the column
    if mode = lenMin -> need colName
        return the size of the smallest string in the column
    if mode = Maxstr -> need colName
        return the bigger string in the column
    if mode = Minstr -> need colNmae
        return the smallest string in the column
    if mode = replace -> need colName and mask
        return the column with the character replace
    if mode = split -> need colName and mask
        return the column with the string split
    if mode = contains -> need colName and mask
        return a column with the search
    :return: str or int or dataframe or list

    """
    if kwargs.get('mode') == 'lower':
        return df[kwargs.get('colName')].str.lower()
    elif kwargs.get('mode') == 'upper':
        return df[kwargs.get('colName')].str.upper()
    elif kwargs.get('mode') == 'len':
        return df[kwargs.get('colName')].str.len()
    elif kwargs.get('mode') == 'lenMax':
        return df[kwargs.get('colName')].str.len().idxmax()
    elif kwargs.get('mode') == 'lenMin':
        return df[kwargs.get('colName')].str.len().idxmin()
    elif kwargs.get('mode') == 'replace':
        return df[kwargs.get('colName')].replace(kwargs.get('mask'))
    elif kwargs.get('mode') == 'split':
        return df[kwargs.get('colName')].str.split(kwargs.get('mask'))
    elif kwargs.get('mode') == 'contains':
        return df[kwargs.get('colName')].str.contains(kwargs.get('mask'))
    elif kwargs.get('mode') == 'Maxstr':
        return df.loc[df[kwargs.get('colName')].str.len().idxmax(), kwargs.get('colName')]
    elif kwargs.get('mode') == 'Minstr':
        return df.loc[df[kwargs.get('colName')].str.len().idxmin(), kwargs.get('colName')]


class PdSaver:

    def __init__(self, df):
        self.df = df

    def CSV(self, route, name, **kwargs):
        name = name + '.csv'
        file = Path(route, name)
        self.df.to_csv(file, **kwargs)
        return True