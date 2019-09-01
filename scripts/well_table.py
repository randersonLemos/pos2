import pandas as pd

class Well_Table:
    dic = {}
    dic['Cumulative Oil SC'] = 'Cum. Oil SC'
    dic['Cumulative Gas SC'] = 'Cum. Gas SC'
    dic['Cumulative Water SC'] = 'Cum. Water SC'
    dic['Oil Rate SC - Instantaneous On-time'] = 'Oil Rate SC - Inst.'
    dic['Gas Rate SC - Instantaneous On-time'] = 'Gas Rate SC - Inst.'
    dic['Water Rate SC - Instantaneous On-time'] = 'Water Rate SC - Inst.'
    dic['Oil Cut SC - %'] = 'Oil Cut SC'
    dic['Water Cut SC - %'] = 'Water Cut SC'
    dic['Well Bottom-hole Pressure'] = 'Well BHP'
    dic['Well BHP Derivative'] = 'Well BHPD'

    def __init__(self,  lst):
        self.file = lst[0]
        self.what = lst[1][6:]
        cols = lst[2].split('\t')
        units =  lst[3].split('\t')
        header = []
        for col ,uni in zip(cols, units):
            if col in self.dic:
                col = self.dic[col]
            if uni == '':
                if col == 'Well state':
                    uni = '_'
                else:
                    uni = '%'
            header.append('{} ({})'.format(col, uni.lower().replace('(','').replace(')','')))
        data = [raw.split('\t') for raw in lst[4:]]
        self.df = pd.DataFrame(data, columns=header)

        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['DATE (yyyy/mm/dd)'] = self.df['DATE (yyyy/mm/dd)'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('DATE (yyyy/mm/dd)', drop=True)
