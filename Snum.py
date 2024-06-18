import numpy as np


def generate_array(*args):
    return np.array(list(args))


def generate_range_array(start, stop, step):
    return np.arange(start=start, stop=stop, step=step)


def ones_array(cantidad):
    return np.ones(shape=cantidad)


def zeros_array(cantidad):
    return np.zeros(shape=cantidad)


def rand_choice(lst):
    return np.random.choice(lst)


def rand_shuffle(lst):
    np.random.shuffle(lst)
    return lst


def float_random_array_one(cantidad):
    return np.random.random(size=cantidad)


def int_random_array(start, stop, size):
    return np.random.randint(low=start, high=stop, size=size)


def generate_order_interval_array(low, high, size):
    return np.linspace(start=low, stop=high, num=size)


def order_array(lst):
    lst.sort()
    return lst


def number_array_info(lst, *args):
    if 'basic' in args:
        return f'''
        Size: {len(lst)}
        Unique len: {len(np.unique(lst))}
        Unique: {np.transpose(np.unique(lst))}
        '''
    elif 'operations' in args:
        return f'''
        Sum: {sum(lst)}
        Min: {np.min(lst)}
        Max: {np.max(lst)}
        '''
    elif 'statics' in args:
        return f'''
        Mean: {np.mean(lst)}
        Standard deviation: {np.std(lst)}
        Round data: {np.transpose(np.round(lst, decimals=1))}
        '''
    elif 'describe' in args:
        import pandas as pd
        x = pd.Series(lst.tolist(), name='resultado')
        return x.describe()
    else:
        return f'''
        Size: {lst.size}
        '''


def number_array_count_zeros(lst: callable) -> int:
    s = len(lst)
    z = lst.count_nonzero(s)
    if len(z) != s:
        return s - z
    else:
        return 0


def search_index_value(lst, value):
    return np.where(lst == value)


def recorrer_lista(lst, **kwargs):
    if 'start' in kwargs and 'stop' in kwargs:
        return lst[kwargs.get('start'):kwargs.get('stop')]
    elif 'start' in kwargs:
        return lst[kwargs.get('start'):]
    elif 'stop' in kwargs:
        return lst[:kwargs.get('stop')]
    else:
        return lst


def transpose_list(lst):
    return np.transpose(lst)


def check_position(a, b):
    return [str(i) for i, ltr in enumerate(a) if ltr == b]