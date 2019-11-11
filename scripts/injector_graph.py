from .graph import Graph
from .keys import Well_Keys

class Injector_Graph:
    def __init__(self, well_lst, table_obj):
        self.well_lst = well_lst
        self.table_obj = table_obj

    def gas(self, well_lst=[]):
        Graph.fluid(self._df_gas(well_lst), 'Cumulative Gas SC')

    def water(self, well_lst=[]):
        Graph.fluid(self._df_wat(well_lst), 'Cumulative Water SC')

    def gas_dot(self, well_lst=[]):
        Graph.fluid_dot(self._df_gas_dot(well_lst), 'Gas Rate SC')

    def water_dot(self, well_lst=[]):
        Graph.fluid_dot(self._df_wat_dot(well_lst), 'Water Rate SC')

    def bhp(self, well_lst=[]):
        Graph.pressure(self._df_bhp(well_lst), 'Bottom Hole Pressure')

    #def wag_dot(self, well_lst=[]):
    #    tab = self.table_obj
    #    if self._is_empty(well_lst):
    #        well_lst = self.well_lst
    #    for well in well_lst:
    #        gas_srs = tab.get(well+'_G').df[Well_Keys.gas_rate_sc()]
    #        wat_srs = tab.get(well+'_W').df[Well_Keys.wat_rate_sc()]
    #        import pdb; pdb.set_trace()
    #        return

    def _df_gas(self, well_lst=[]):
        tab = self.table_obj
        well_lst = self._G(well_lst)
        if not well_lst:
            well_lst = self._G(self.well_lst)
        df = tab.grp_col(Well_Keys.cum_gas_sc()).dropna()[well_lst]
        dic = {}
        for col in df:
            dic[col] = col[:-2]
        df.rename(dic, axis='columns', inplace=True)
        return df

    def _df_wat(self, well_lst=[]):
        tab = self.table_obj
        well_lst = self._W(well_lst)
        if not well_lst:
            well_lst = self._W(self.well_lst)
        df = tab.grp_col(Well_Keys.cum_wat_sc()).dropna()[well_lst]
        dic = {}
        for col in df:
            dic[col] = col[:-2]
        df.rename(dic, axis='columns', inplace=True)
        return df

    def _df_gas_dot(self, well_lst=[]):
        tab = self.table_obj
        well_lst = self._G(well_lst)
        if not well_lst:
            well_lst = self._G(self.well_lst)
        df = tab.grp_col(Well_Keys.gas_rate_sc()).dropna()[well_lst]
        dic = {}
        for col in df:
            dic[col] = col[:-2]
        df.rename(dic, axis='columns', inplace=True)
        return df

    def _df_wat_dot(self, well_lst=[]):
        tab = self.table_obj
        well_lst = self._W(well_lst)
        if not well_lst:
            well_lst = self._W(self.well_lst)
        df = tab.grp_col(Well_Keys.wat_rate_sc()).dropna()[well_lst]
        dic = {}
        for col in df:
            dic[col] = col[:-2]
        df.rename(dic, axis='columns', inplace=True)
        return df

    def _df_bhp(self, well_lst=[]):
        tab = self.table_obj
        well_lst_ = self._G(well_lst)
        if not well_lst:
            well_lst_ = self._G(self.well_lst)
        df_G = tab.grp_col(Well_Keys.well_bhp()).dropna()[well_lst_]

        dic = {}
        for col in df_G:
            dic[col] = col[:-2]
        df_G.rename(dic, axis='columns', inplace=True)

        well_lst_ = self._W(well_lst)
        if not well_lst:
            well_lst_ = self._W(self.well_lst)
        df_W = tab.grp_col(Well_Keys.well_bhp()).dropna()[well_lst_]

        dic = {}
        for col in df_W:
            dic[col] = col[:-2]
        df_W.rename(dic, axis='columns', inplace=True)

        return (df_W+df_G)/2.0

    def show(self):
        Graph.show()

    def _is_empty(self, lst):
        return not lst

    def _G(self, well_lst):
        return ['{}_G'.format(well) for well in well_lst]

    def _W(self, well_lst):
        return ['{}_W'.format(well) for well in well_lst]
