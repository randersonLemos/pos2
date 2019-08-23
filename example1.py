# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import settings as sett
tables = {}

def to_well_table(lst):
    file = lst[0]
    what = lst[1][6:]
    cols = lst[2].split('\t')
    units =  lst[3].split('\t')
    header = ['{} ({})'.format(col,uni) for col,uni in zip(cols, units)]
    data = [raw.split('\t') for raw in lst[4:]]
    df = pd.DataFrame(data, columns=header).apply(pd.to_numeric, errors='ignore')
    return Table(what, file, df)        

def is_well_table(lst):
    for line in lst:
        if 'WELL' in line:
            return True
    return False

def to_sector_table(lst):
    file = lst[0]
    cols = lst[1].split('\t')
    what = '{}'.format(lst[3])
    units =  lst[4].split('\t')
    units.append('percent')
    header = ['{} ({})'.format(col,uni) for col,uni in zip(cols, units)]
    data = [raw.split('\t') for raw in lst[5:]]
    df = pd.DataFrame(data, columns=header).apply(pd.to_numeric, errors='ignore')
    return Table(what, file, df)        

def is_sector_table(lst):
    for line in lst:
        if 'SECTOR' in line:
            return True
    return False    
    
class Table:
    dic = {}
    dic['Oil Rate SC - Monthly (m3/day)'] = 'Oil Rate SC (m3/day)'    
    
    def __init__(self, what, file, df):
        self.what = what
        self.file = file
        self.df = df.rename(self.dic, axis='columns')
        self.columns = self.df.columns
        
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
    
    def __init__(self, prods='', injes=''):
        self.dic = {}        
        
    def add(self, obj_tab):
        self.dic[obj_tab.what] = obj_tab

    def oil_rate_sc(self):   
        self._check_prods()
        intersection = [key for key in self.dic if key in self.prods]
        dic = {}
        for key in intersection:
            dic[key] = self.dic[key].df['Cumulative Oil SC (m3)']
        return pd.DataFrame.from_dict(dic)        
    
    def _check_prods(self):
        if not self.prods:
            raise NameError('Producers names must be passed as list to class via cls.set_prods...')

def get_tables(sim_folder):    
    import infos
    Tables.set_prods(infos.PRODS)
    tables = Tables()
    lst = []
    with pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /
                      sim_folder / sett.REP_FILE).open() as fh:        
        for raw_line in reversed(list(fh)):
            line = raw_line.strip('\n').strip()
            if 'TABLE' in line:
                lst = list(reversed(lst))
                if    is_well_table(lst)  : tables.add(to_well_table(lst))                 
                elif  is_sector_table(lst): tables.add(to_sector_table(lst))
                else: raise Warning('Table pattern not mapped. Just ignoring it...')
                lst = []
            else:
                lst.append(line) 
    return tables

if __name__ == '__main__':    
    sim_folder = 'sim_001'
    tables = get_tables(sim_folder)    
    lst = tables.oil_rate_sc()
    



        
#        fig, ax1 = plt.subplots(1, 1)   
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax1, kind='line',x='DATE (YYYY/MM/DD)',y='Cumulative Oil SC (m3)')
#            except: pass
#        fig, ax2 = plt.subplots(1, 1)
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax2, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Rate SC - Monthly (m3/day)')
#            except: pass
#        fig, ax3 = plt.subplots(1, 1)
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax3, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Recovery Factor SCTR (percent)')
#            except: pass
        