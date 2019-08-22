# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import settings as sett
sim_folder = 'sim_001'

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
    def __init__(self, what, file, df):
        self.what = what
        self.file = file
        self.df = df
        self.columns = df.columns.to_list()


with pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /  sim_folder / sett.REP_FILE).open() as fh:
    tables = {}
    lst = []
    for raw_line in reversed(list(fh)):
        line = raw_line.strip('\n').strip()
        if 'TABLE' in line:
            lst = list(reversed(lst))
            if is_well_table(lst):
                t = to_well_table(lst)                     
                tables[t.what] = t                 
            elif is_sector_table(lst):
                t = to_sector_table(lst)                     
                tables[t.what] = t
            else:
                raise Warning('Table pattern not mapped. Just ignoring it...')
            lst = []
        else:
            lst.append(line)    
        
    fig, ax1 = plt.subplots(1, 1)   
    for key in tables:
        try:    tables[key].df.plot(ax=ax1, kind='line',x='DATE (YYYY/MM/DD)',y='Cumulative Oil SC (m3)')
        except: pass
    fig, ax2 = plt.subplots(1, 1)
    for key in tables:
        try:    tables[key].df.plot(ax=ax2, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Rate SC - Monthly (m3/day)')
        except: pass
    fig, ax3 = plt.subplots(1, 1)
    for key in tables:
        try:    tables[key].df.plot(ax=ax3, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Recovery Factor SCTR (percent)')
        except: pass
        