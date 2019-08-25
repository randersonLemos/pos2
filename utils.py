# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:06:08 2019

@author: randerson
"""

import pathlib
import pandas as pd
from table import Table, Tables

def to_well_table(lst):
    file = lst[0]
    what = lst[1][6:]
    cols = lst[2].split('\t')
    units =  lst[3].split('\t')
    header = ['{} ({})'.format(col,uni) for col,uni in zip(cols, units)]
    data = [raw.split('\t') for raw in lst[4:]]
    df = pd.DataFrame(data, columns=header)    
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
    df = pd.DataFrame(data, columns=header)    
    return Table(what, file, df)        


def is_sector_table(lst):
    for line in lst:
        if 'SECTOR' in line:
            return True
    return False  

def get_tables(path_to_rep_file):    
    import infos
    Tables.set_prods(infos.PRODS)
    tables = Tables()
    lst = []
    with pathlib.Path(path_to_rep_file).open() as fh:        
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