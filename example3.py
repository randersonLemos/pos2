# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""


import os
import shutil

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from post_process.scripts import utils
    from config.scripts import settings as sett

    sim_group_folder = 'REFERENCE_OTM'
    sim_folder  = 'sim_001'
    path_to_rep_file = sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder / sett.REP_NAME
    ref = utils.get_tables(path_to_rep_file)

    sim_group_folders = os.listdir(sett.REP_ROOT / sett.SIMS_FOLDER)
    for sim_group_folder in sim_group_folders:
        sim_folders = []
        for content in os.listdir(sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder):
            if os.path.isdir(sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / content):
                sim_folders.append(content)
            #elif '.eofcs.csv' in content:
            #    os.makedirs(sett.CSV_ROOT / sett.SIMS_FOLDER / sim_group_folder, exist_ok=True)
            #    shutil.copyfile(sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / content,
                                   sett.CSV_ROOT / sett.SIMS_FOLDER / sim_group_folder / content)
        for sim_folder in sim_folders:
            try:
                path_to_rep_file = sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder / sett.REP_NAME
                tables = utils.get_tables(path_to_rep_file)
                print(path_to_rep_file)
                from inputt import loader
                for well in loader.inje_lst: ref.add(ref.join(well.name, *well.alias_lst))
                #output_dir = sett.CSV_ROOT / sett.SIMS_FOLDER/ sim_group_folder / sim_folder
                #output_dir = sett.CSV_ROOT / sett.SIMS_FOLDER/ sim_group_folder / sim_folder / sett.CSV_FOLD
                tables.to_csv(output_dir, tables_obj=ref)
            except KeyError:
                print("Error with rep file from:")
                print("  ", path_to_rep_file)
                print(str(path_to_rep_file), file=open("errors.txt", "a"))
