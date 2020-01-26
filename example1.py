# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""


if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from post_process.scripts import utils
    from config.scripts import settings as sett

    sim_group_folder = 'REFERENCE'
    sim_folder  = 'sim_001'
    path_to_rep_file = sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder / sett.REP_NAME
    tables = utils.get_tables(path_to_rep_file)

    from inputt import loader
    for well in loader.inje_lst:
        als1, als2 = well.alias_lst
        tables.add(tables.join(well.name, als1, als2, dell=True))

    path_to_csv_folder = sett.CSV_ROOT / sett.SIMS_FOLDER/ sim_group_folder / sim_folder
    tables.to_csv(path_to_csv_folder)
