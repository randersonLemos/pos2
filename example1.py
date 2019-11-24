# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""


if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from scripts import utils

    from config.scripts import settings as sett

    sim_folder = 'sim_016'
    path_to_rep_file = sett.REP_ROOT / sim_folder / sett.REP_NAME
    ref = utils.get_tables(path_to_rep_file)
