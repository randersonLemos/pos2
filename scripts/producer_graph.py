from .graph import Graph
from .keys import Well_Keys

class Producer_Graph:
    def __init__(self, well_lst, table_obj):
        self.well_lst = well_lst
        self.table_obj = table_obj

    def fluids(self, well_lst=[]):
        self.oil(well_lst)
        self.gas(well_lst)
        self.water(well_lst)

    def fluids_dot(self, well_lst=[]):
        self.oil_dot(well_lst)
        self.gas_dot(well_lst)
        self.water_dot(well_lst)

    def oil(self, well_lst=[]):
        Graph.fluid(self._df_oil(well_lst), 'Cumulative Oil SC')

    def gas(self, well_lst=[]):
        Graph.fluid(self._df_gas(well_lst), 'Cumulative Gas SC')

    def water(self, well_lst=[]):
        Graph.fluid(self._df_wat(well_lst), 'Cumulative Water SC')

    def oil_dot(self, well_lst=[]):
        Graph.fluid_dot(self._df_oil_dot(well_lst), 'Oil Rate SC')

    def gas_dot(self, well_lst=[]):
        Graph.fluid_dot(self._df_gas_dot(well_lst), 'Gas Rate SC')

    def water_dot(self, well_lst=[]):
        Graph.fluid_dot(self._df_wat_dot(well_lst), 'Water Rate SC')

    def gor(self, well_lst=[]):
        Graph.fluid_ratio(self._df_gor(well_lst), 'Gas Oil Ratio SC')

    def wcut(self, well_lst=[]):
        Graph.percent(self._df_wcut(well_lst)*100, 'Water Cut SC')

    def bhp(self, well_lst=[]):
        Graph.pressure(self._df_bhp(well_lst), 'Bottom Hole Pressure')

    def _df_oil(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_oil_sc()).dropna()[well_lst]

    def _df_gas(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_gas_sc()).dropna()[well_lst]

    def _df_wat(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_wat_sc()).dropna()[well_lst]

    def _df_oil_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.oil_rate_sc()).dropna()[well_lst]

    def _df_gas_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.gas_rate_sc()).dropna()[well_lst]

    def _df_wat_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.wat_rate_sc()).dropna()[well_lst]

    def _df_gor(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.gor_sc()).dropna()[well_lst]

    def _df_wcut(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.wat_cut_sc()).dropna()[well_lst]

    def _df_bhp(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.well_bhp()).dropna()[well_lst]

    def show(self):
        Graph.show()
