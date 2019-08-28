# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import utils
import pathlib
import settings as sett
from graph import Graph

def graphs():
    #Graph.cumu_sc(tables.oil_cumu_sc(), 'Cumulative Oil SC',   y_factor=1e3)
    #Graph.cumu_sc(tables.wat_cumu_sc(), 'Cumulative Water SC', y_factor=1e3)
    #Graph.cumu_sc(tables.gas_cumu_sc(), 'Cumulative Gas SC',   y_factor=1e6)
    Graph.rate_sc(tables.oil_rate_sc(), 'Oil Rate SC',         y_factor=1)
    #Graph.rate_sc(tables.gas_rate_sc(), 'Gas Rate SC',         y_factor=1000)
    #Graph.rate_sc(tables.wat_rate_sc(), 'Water Rate SC',       y_factor=1)
    #Graph.cut_sc(tables.oil_cutt_sc(),  'Oil Cut SC')
    Graph.cut_sc(tables.wat_cutt_sc(),  'Water Cut SC')
    Graph.gas_oil_ratio(tables.gas_oil_ratio_sc(), 'Gas Oil Ratio SC')
    Graph.show()

if __name__ == '__main__':
    #sim_folder = 'sim_001'
    #path_to_rep_file = pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /
    #                  sim_folder / sett.REP_FILE)
    path_to_rep_file = '/home/pamonha/simulation/ref2/main.rep'
    tables = utils.get_tables(path_to_rep_file)

    df = tables._column_agregator_ctrl('PRK014')


