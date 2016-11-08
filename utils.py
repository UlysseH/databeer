# Utils file with functions used in notebooks
import pandas as pd
import numpy as np



def load_from_csv(start, end):
    data = {}
    data['recipes'] = pd.read_csv('brewtoad/csv/recipes_page_{0}_to_{1}.csv'.format(start, end))
    data['styles'] = pd.read_csv('brewtoad/csv/styles_page_{0}_to_{1}.csv'.format(start, end))
    data['fermentables'] = pd.read_csv('brewtoad/csv/fermentables_page_{0}_to_{1}.csv'.format(start, end))
    data['hops'] = pd.read_csv('brewtoad/csv/hops_page_{0}_to_{1}.csv'.format(start, end))
    data['yeasts'] = pd.read_csv('brewtoad/csv/yeasts_page_{0}_to_{1}.csv'.format(start, end))
    data['miscs'] = pd.read_csv('brewtoad/csv/miscs_page_{0}_to_{1}.csv'.format(start, end))
    return data


def format_data(data):
    def f(x):
        if x[0] == '[':
            x = x[3: len(x) - 2]
            try:
                x = np.float(x)
            except:
                pass
        return x

    for key in data.keys():
        data[key] = data[key].applymap(f)

    # Ugly but solves hop's g/oz issue
    def f_hops(x):
        if not x:
            return x
        if x[len(x) - 1] == 'z':
            x = np.float(x[: len(x) - 3])
            return x * 28
        else:
            return np.float(x[: len(x) - 2])
        return x
    data['hops']['amount'] = data['hops']['display_amount'].map(f_hops)
    params = [
        'beer_id',
        'beer_name',
        'name',
        'origin',
        'alpha',
        'beta',
        'amount',
        'use',
        'form',
        'time',
        'notes'
    ]
    data['hops'] = data['hops'][params]
    return data
