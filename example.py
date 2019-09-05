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
    import settings as sett
    #sim_folder = 'ref2'
    #path_to_rep_file = sett.LOCAL_ROOT  / sett.RES_FOLD / sim_folder / sett.REP_NAME
    #reference = utils.get_tables(path_to_rep_file)
    
    sim_folder = 'sim_001'
    path_to_rep_file = sett.LOCAL_ROOT  / sett.RES_FOLD / sim_folder / sett.REP_NAME
    #path_to_rep_file = '/home/pamonha/simulation/ref2/main.rep'
    tables = utils.get_tables(path_to_rep_file)
    graphs(WELLS)
    graphs_specials(WELLS)
    Graph.show()
    
    #import pandas as pd
    #df = pd.DataFrame()
    #for idx in range(1,51):
    #    sim_folder = 'sim_{:03d}'.format(idx)
    #    path_to_rep_file = sett.LOCAL_ROOT  / sett.RES_FOLD / sim_folder / sett.REP_NAME
    #    tables = utils.get_tables(path_to_rep_file)
    #    df['sim_{:03d}'.format(idx)] = tables.recovery_factor()['Entire Field']    
    #df['ref'] = reference.recovery_factor()['Entire Field'] 
    #import matplotlib.pyplot as plt
    #fig, ax = plt.subplots()
    #fig.suptitle('Recovery Factor')
    #ax = df.plot(ax=ax)
    #ax.set_title('ICV with multi-position choke opening state')
    #ax.set_ylabel('%')
    #ax.legend(fontsize='xx-small',loc='center left', bbox_to_anchor=(1, 0.5))
