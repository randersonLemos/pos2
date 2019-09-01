import pandas as pd
from itertools import zip_longest

class Sector_Table:
    dic = {'Oil Recovery Factor SCTR': 'Factor'}

    def __init__(self,  lst):
        self.file = lst[0]
        self.what = 'Recovery Factor'
        cols = lst[1].split('\t')
        units =  lst[4].split('\t')
        header = []
        for col, uni in zip_longest(cols, units):
            if col in self.dic:
                col = self.dic[col]
            if uni is None:
                uni = '%'
            header.append('{} ({})'.format(col, uni.lower()))
        data = [raw.split('\t') for raw in lst[5:]]
        self.df = pd.DataFrame(data, columns=header)

        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['DATE (yyyy/mm/dd)'] = self.df['DATE (yyyy/mm/dd)'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('DATE (yyyy/mm/dd)', drop=True)
