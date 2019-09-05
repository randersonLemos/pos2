import pandas as pd
from itertools import zip_longest

class Special_Table:
    dic = {}
    dic['CRLGOR']   = 'GOR'
    dic['CRLLRATE'] = 'OPR'
    dic['CRLWCUT']  = 'WCUT'

    def __init__(self, lst):
        if 'Average Reservoir Pressure' in lst[1]:
            what = 'Avg. Pressure'
            cols = lst[2].split('\t')
            units =  lst[3].split('\t')
            data = [raw.split('\t') for raw in lst[4:]]
        elif 'CTRL WCUT' in lst[1]:
            what = 'WCUT'
            cols = self._get_cols(lst[3])
            units =  lst[4].split('\t')
            data = [raw.split('\t') for raw in lst[5:]]
        elif 'CTRL LR' in lst[1]:
            what = 'OPR'
            cols = self._get_cols(lst[3])
            units =  lst[4].split('\t')
            data = [raw.split('\t') for raw in lst[5:]]
        elif 'CTRL GOR' in lst[1]:
            what = 'GOR'
            cols = self._get_cols(lst[3])
            units =  lst[4].split('\t')
            data = [raw.split('\t') for raw in lst[5:]]

        self.file = lst[0]
        self.what = what

        header = []
        for col,uni in zip_longest(cols, units):
            if uni is None:
                uni = '%'
            uni = uni.replace('(','').replace(')','')
            header.append('{} ({})'.format(col, uni.lower()))
        self.df = pd.DataFrame(data, columns=header)

        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['DATE'] = self.df['DATE (yyyy/mm/dd)'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df.drop(columns=['DATE (yyyy/mm/dd)'], inplace=True)
        self.df = self.df.set_index('DATE', drop=True)

    def _get_cols(self, line):
        cols = ['TIME','DATE']
        for phrase in line.split('\t'):
            #for key in self.dic:
            #    if key in phrase:
            #        fix = self.dic[key]
            #suffix = phrase[phrase.index('"')+1:-1]
            #cols.append('{}_{}'.format(fix, suffix))
            cols.append('{}'.format(phrase[phrase.index('"')+1:-1]))
        return cols


