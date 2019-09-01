# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import pathlib
from scripts import utils
from scripts.graph import Graph
from scripts.table_keys import Well_Keys
from scripts.table_keys import Sector_Keys

WELLS = ['PRK014','PRK028','PRK045','PRK052','PRK060','PRK061'
         ,'PRK083','PRK084','PRK085','PWILDC']

def graphs(wells):
    Graph.rate(tables.well_column(Well_Keys.oil_rate_sc())[wells], 'Rate Oil SC')
    #Graph.cumu(tables.well_column(Well_Keys.cum_oil_sc())[wells], 'Cum. Oil SC')
    #Graph.ratio(tables.well_column(Well_Keys.gor_sc())[wells], 'Gas Oil Ratio SC')
    #Graph.percent(tables.well_column(Well_Keys.wat_cut_sc())[wells], 'Water Cut')
    #Graph.percent(tables.recovery_factor(), 'Recovery Factor')
    #Graph.pressure(tables.avg_pressure(), 'Pressure')
    #Graph.pressure(tables.well_column(Well_Keys.well_bhp())[wells], 'BHP')
    #Graph.dot_pressure(tables.well_column(Well_Keys.well_bhpd())[wells], 'BHPD')

def graphs_specials(wells):
    for well in wells:
        if well == 'PWILDC':
            pass
        else:
            df = tables.special_well(well)
            wcols = []
            gcols = []
            ocols = []
            for col in df:
                if 'WCUT' in col:
                    wcols.append(col)
                elif 'GOR' in col:
                    gcols.append(col)
                elif 'OPR' in col:
                    ocols.append(col)

            Graph.percent(df[wcols], well)
            Graph.ratio(df[gcols], well)
            Graph.rate(df[ocols], well)

if __name__ == '__main__':
    #import settings as sett
    #sim_folder = 'sim_001'
    #path_to_rep_file = pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /
    #                  sim_folder / sett.REP_FILE)
    path_to_rep_file = '/home/pamonha/simulation/ref2/main.rep'
    tables = utils.get_tables(path_to_rep_file)
    graphs(['PRK014'])
    graphs_specials(['PRK014'])
    Graph.show()
