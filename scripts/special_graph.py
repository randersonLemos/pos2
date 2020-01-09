from .graph import Graph
#from .keys import Special_Keys

class Special_Graph:
    def __init__(self, well_lst, table_obj):
        self.well_lst = well_lst
        self.table_obj = table_obj

    def opc(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='OPC', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def opr(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='OPR', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def gpc(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GPC', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def wpr(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WPR', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def wpc(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WPC', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def gpr(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GPR', axis=1)
            if not df.empty:
                Graph.fluid_dot(df, well)

    def wcut(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WCUT', axis=1)
            if not df.empty:
                Graph.percent(df, well)

    def gor(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GOR', axis=1)
            if not df.empty:
                Graph.fluid_ratio(df, well)

    def show(self):
        Graph.show()

