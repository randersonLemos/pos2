# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:04:55 2019

@author: randerson
"""

import re
import pathlib
import pandas as pd
from .well_table import Well_Table
from .sector_table import Sector_Table
from .special_table import Special_Table
from .keys import Keys
from .keys import Sector_Keys

class Tables():
    def __init__(self):
        self._dic = {}

    def add(self, obj_tab):
        self._dic[obj_tab.what] = obj_tab

    def get(self, key):
        return self._dic[key]

    def keys(self):
        return self._dic.keys()

    def columns(self):
        return set([col for key in self._dic for col in self._dic[key].df.columns])

    def rec_fac(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.recovery_factor()].copy()

    def avg_pre(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.avg_pressure()].copy()

    def grp_col(self, column):
        dic = {}
        for key in self._dic:
            if column in self._dic[key].df.columns:
                dic[key] = self._dic[key].df[column]
        return pd.DataFrame.from_dict(dic)

    def grp_col_spe_well(self, well):
        dic = {}
        for key in self._dic:
            if isinstance(self._dic[key], Special_Table):
                for col in self._dic[key].df.columns:
                    if well in col:
                        dic[re.sub(r'\w\w\w\d\d\d',key,col)] = self._dic[key].df[col]
        return pd.DataFrame.from_dict(dic)

    def to_csv(self, dir):
        dir = pathlib.Path(dir)
        dir.mkdir(parents=True, exist_ok=True)

        self.rec_fac().to_csv(dir / 'recovery_factor.csv', header=[Sector_Keys.recovery_factor()])
        self.avg_pre().to_csv(dir / 'avg_pressure.csv', header=[Sector_Keys.avg_pressure()])

        for key in self._dic:
            if isinstance(self._dic[key], Well_Table):
                    self._dic[key].df.to_csv(dir / '{}.csv'.format(key))

                    df = self.grp_col_spe_well(key)
                    df.to_csv(dir / '{}_Layers.csv'.format(key))