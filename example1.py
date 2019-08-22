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

def is_well_table(lst):
    for line in lst:
        if 'WELL' in line:
            return True
    return False
    
class Table:
    def __init__(self, what, file, df):
        self.what = what
        self.file = file
        self.df = df

with pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /  sim_folder / sett.REP_FILE).open() as fh:
    tab = {}
    lst = []
    for raw_line in reversed(list(fh)):
        line = raw_line.strip('\n').strip()
        if 'TABLE' in line:
            lst = list(reversed(lst))
            if is_well_table(lst):     
                file = lst[0]
                well = lst[1]
                cols = lst[2].split('\t')
                units =  lst[3].split('\t')
                header = ['{} ({})'.format(col,uni) for col,uni in zip(cols, units)]
                data = [raw.split('\t') for raw in lst[4:]]
                df = pd.DataFrame(data, columns=header).apply(pd.to_numeric, errors='ignore')
                
                tab[line] = Table(well, file, df)
            lst = []
        else:
            lst.append(line)    
            
    for key in tab:
        tab[key].df.plot(kind='line',x='DATE (YYYY/MM/DD)',y='Cumulative Oil SC (m3)', title=tab[key].what)
        tab[key].df.plot(kind='line',x='DATE (YYYY/MM/DD)',y='Oil Rate SC - Monthly (m3/day)', title=tab[key].what)