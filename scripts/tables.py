# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:04:55 2019

@author: randerson
"""

import re
import pandas as pd
from .well_table import Well_Table
from .sector_table import Sector_Table
from .special_table import Special_Table
from .table_keys import Sector_Keys
from .table_keys import Special_Keys

class Tables():
    def __init__(self):
        self.dic = {}

    def add(self, obj_tab):
        self.dic[obj_tab.what] = obj_tab

    def keys(self):
        return self.dic.keys()

    def columns(self):
        return set([col for key in self.dic for col in self.dic[key].df.columns])

    def well_column(self, column):
        dic = {}
        for key in self.dic:
            if isinstance(self.dic[key], Well_Table):
                if key == 'Wildcat':
                    pass
                else:
                    dic[key] = self.dic[key].df[column]
        return pd.DataFrame.from_dict(dic)

    def recovery_factor(self):
        dic = {}
        dic[Sector_Keys.entire_field()] = self.dic['Recovery Factor'].df[Sector_Keys.recovery_factor()]
        return pd.DataFrame.from_dict(dic)

    def avg_pressure(self):
        dic = {}
        dic[Sector_Keys.entire_field()]= self.dic['Avg. Pressure'].df[Special_Keys.avg_pressure()]
        return pd.DataFrame.from_dict(dic)

    def special_well(self, well):
        dic = {}
        for key in self.dic:
            if isinstance(self.dic[key], Special_Table):
                for col in self.dic[key].df.columns:
                    #import pdb; pdb.set_trace()
                    if well in col:
                        dic[re.sub(r'\w\w\w\d\d\d',key,col)] = self.dic[key].df[col]
        return pd.DataFrame.from_dict(dic)

    def __getitem__(self, key):
        return self.dic[key]