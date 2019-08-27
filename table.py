# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:04:55 2019

@author: randerson
"""

import pandas as pd

class Table:
    dic = {}
    dic['Oil Rate SC - Monthly (m3/day)'] = 'Oil Rate SC (m3/day)'

    def __init__(self, what, file, df):
        self.what = what
        self.file = file
        self.df = df.rename(self.dic, axis='columns')
        self._settings()

    def _settings(self):
        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['DATE (YYYY/MM/DD)'] = self.df['DATE (YYYY/MM/DD)'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('DATE (YYYY/MM/DD)', drop=True)

    def columns(self):
        return self.df.columns.tolist()

    def oil_rate_sc(self):
        return self.df['Oil Rate SC (m3/day)']

    def oil_cumu_sc(self):
        return self.df['Cumulative Oil SC (m3)']

    def __repr__(self):
        with pd.option_context('display.max_rows', 6):
            return self.df.__repr__()

class Tables():
    prods = set()
    @classmethod
    def set_prods(cls, lst_names):
        cls.prods = set(lst_names)

    def __init__(self):
        self.dic = {}

    def add(self, obj_tab):
        self.dic[obj_tab.what] = obj_tab

    def columns(self):
        cols = set()
        for key in self.dic:
            for col in self.dic[key].columns():
                cols.add(col)
        return list(cols)

    def keys(self):
        return self.dic.keys()

    def oil_rate_sc(self):
        return self._column_agragator('Oil Rate SC (m3/day)')

    def oil_cumu_sc(self):
        return self._column_agragator('Cumulative Oil SC (m3)')

    def _column_agragator(self, column):
        self._check_prods()
        intersection = [key for key in self.dic if key in self.prods]
        dic = {}
        for key in intersection:
            dic[key] = self.dic[key].df[column]
        return pd.DataFrame.from_dict(dic)

    def _check_prods(self):
        if not self.prods:
            raise NameError('Producers names must be passed as list to class via cls.set_prods...')

    def __getitem__(self, key):
        return self.dic[key]

    def __repr__(self):
        return self.dic.__repr__()