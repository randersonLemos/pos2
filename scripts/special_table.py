import pandas as pd
from itertools import zip_longest
from .keys import Keys

class Special_Table:

    def __init__(self, lst):
        if 'CTRL WCUT' in lst[1]:
            what = 'WCUT'
        elif 'CTRL LR' in lst[1]:
            what = 'OPR'
        elif 'CTRL GOR' in lst[1]:
            what = 'GOR'

        self.file = lst[0]
        self.what = what

        cols = self._get_cols(lst[3])

        self.units = list(zip_longest(cols, map(str.lower,lst[4].split('\t'))))
        if 'CTRL WCUT' in lst[1]:
            for idx, tup in enumerate(self.units):
                if tup[1] is None:
                    self.units[idx] = (tup[0],'percent',)

        data = [raw.split('\t') for raw in lst[5:]]
        self.df = pd.DataFrame(data, columns=cols)
        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['Date'] = self.df['Date'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('Date', drop=True)

    def _get_cols(self, line):
        cols = [Keys.time(),Keys.date()]
        for phrase in line.split('\t'):
            cols.append('{}'.format(phrase[phrase.index('"')+1:-1]))
        return cols
