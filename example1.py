# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import utils
import pathlib
import settings as sett


if __name__ == '__main__':    
    sim_folder = 'sim_001'
    path_to_rep_file = pathlib.Path(sett.ROOT_LOCAL / sett.MAIN_FOLDER /
                      sim_folder / sett.REP_FILE)
    tables = utils.get_tables(path_to_rep_file)    
    lst = tables.oil_rate_sc()
    



        
#        fig, ax1 = plt.subplots(1, 1)   
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax1, kind='line',x='DATE (YYYY/MM/DD)',y='Cumulative Oil SC (m3)')
#            except: pass
#        fig, ax2 = plt.subplots(1, 1)
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax2, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Rate SC - Monthly (m3/day)')
#            except: pass
#        fig, ax3 = plt.subplots(1, 1)
#        for key in tables:
#            try:    tables[key].df.plot(ax=ax3, kind='line',x='DATE (YYYY/MM/DD)',y='Oil Recovery Factor SCTR (percent)')
#            except: pass
        