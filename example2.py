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

if __name__ == '__main__':
    import pandas as pd
    Tables = []
    nr_sims = 50
    for idx in range(nr_sims+1):
        sim_folder = 'sim_{:03d}'.format(idx)
        #path_to_rep_file = sett.LOCAL_ROOT  / sett.RES_FOLD / sim_folder / sett.REP_NAME
        path_to_rep_file = '/home/pamonha/Downloads/sims_icvs_increment/{}/main.rep'.format(sim_folder)
        Tables.append((sim_folder,utils.get_tables(path_to_rep_file),))

    for sim_folder, tables in Tables:
        tables.to_csv('csvs/{}'.format(sim_folder))

    rfs = []
    sim_folders = []
    for sim_folder, tables in Tables:
        rfs.append(tables.rec_fac().max()[0])
        sim_folders.append(sim_folder)
    df = pd.DataFrame.from_dict({'sim':sim_folders,'Entire Field':rfs})
    df.index.name = 'idxxx'
    #df.index += 1
    df.to_csv('csvs/rfs.csv')

    #import matplotlib.pyplot as plt
    #fig, ax = plt.subplots()
    #fig.suptitle('Recovery Factor')
    #ax = df.plot(ax=ax)
    #ax.set_title('ICV with multi-position choke opening state')
    #ax.set_ylabel('%')
    #ax.legend(fontsize='xx-small',loc='center left', bbox_to_anchor=(1, 0.5))
