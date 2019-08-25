# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import utils
import pathlib
import settings as sett
from graph import Graph

if __name__ == '__main__':    
    sim_folder = 'sim_001'
    path_to_rep_file = pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /
                      sim_folder / sett.REP_FILE)
    tables = utils.get_tables(path_to_rep_file)    
    
    Graph.oil_rate_sc(tables.oil_rate_sc())
    Graph.oil_cumu_sc(tables.oil_cumu_sc())    