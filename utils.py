# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:06:08 2019

@author: randerson
"""
import re
import pathlib
import warnings
import pandas as pd
from collections import OrderedDict
from itertools import zip_longest
from table import Table, Tables

def to_well_table(lst):
    file = lst[0]
    what = lst[1][6:]
    cols = lst[2].split('\t')
    units =  lst[3].split('\t')
    header = []
    for col,uni in zip_longest(cols, units):
        col = col if col else ''
        col = col.replace('- Instantaneous On-time','Inst')
        col = col.replace(' - %','')
        uni = uni if uni else '%'
        if 'Well state' in col: uni = '_'
        uni = uni.replace('(','').replace(')','')
        header.append('{} ({})'.format(col, uni))
    data = [raw.split('\t') for raw in lst[4:]]
    df = pd.DataFrame(data, columns=header)
    return Table(what, file, df)

def is_well_table(lst):
    return 'WELL' in ''.join(lst)

def to_special_table(lst):
    MAPP = {}
    MAPP['CRLGOR']   = 'GOR'
    MAPP['CRLLRATE'] = 'OPR'
    MAPP['CRLWCUT']  = 'WCUT'

    def get_cols(line):
        cols = ['TIME','DATE']
        for phrase in line.split('\t'):
            fix = [MAPP[key] for key in MAPP if key in phrase].pop()
            suffix = phrase[phrase.index('"')+1:-1]
            cols.append('{}_{}'.format(fix, suffix))
        return cols

    file = lst[0]
    if 'Average Reservoir Pressure' in lst[1]:
        what = 'Avg. RP'
        cols = lst[2].split('\t')
        units =  lst[3].split('\t')
        data = [raw.split('\t') for raw in lst[4:]]
    elif 'CTRL WCUT' in lst[1]:
        what = 'CTRL WCUT'
        cols = get_cols(lst[3])
        units =  lst[4].split('\t')
        data = [raw.split('\t') for raw in lst[5:]]
    elif 'CTRL LR' in lst[1]:
        what = 'CTRL LR'
        cols = get_cols(lst[3])
        units =  lst[4].split('\t')
        data = [raw.split('\t') for raw in lst[5:]]
    elif 'CTRL GOR' in lst[1]:
        what = 'CTRL GOR'
        cols = get_cols(lst[3])
        units =  lst[4].split('\t')
        data = [raw.split('\t') for raw in lst[5:]]

    header = []
    for col,uni in zip_longest(cols, units):
        col = col if col else ''
        uni = uni if uni else '%'
        uni = uni.replace('(','').replace(')','')
        header.append('{} ({})'.format(col, uni))

    df = pd.DataFrame(data, columns=header)
    return Table(what, file, df)

def is_special_table(lst):
    return 'SPECIAL' in ''.join(lst)

def to_sector_table(lst):
    file = lst[0]
    cols = lst[1].split('\t')
    what = '{}'.format(lst[3])
    units =  lst[4].split('\t')
    units.append('%')
    header = ['{} ({})'.format(col,uni) for col,uni in zip(cols, units)]
    data = [raw.split('\t') for raw in lst[5:]]
    df = pd.DataFrame(data, columns=header)
    return Table(what, file, df)

def is_sector_table(lst):
    return 'SECTOR' in ''.join(lst)

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
                if   is_well_table(lst)   : tables.add(to_well_table(lst))
                elif is_sector_table(lst) : tables.add(to_sector_table(lst))
                elif is_special_table(lst): tables.add(to_special_table(lst))
                else:
                    warnings.warn('{} pattern not mapped. Just ignoring it...'.format(line))
                lst = []
            else:
                lst.append(line)
    return tables