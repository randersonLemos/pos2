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

    sims_folder = 'SIM_ICV_2_STGS'
    sim_folder  = 'sim_000'
    path_to_rep_file = sett.REP_ROOT / sims_folder / sim_folder / sett.REP_NAME
    ref = utils.get_tables(path_to_rep_file)

    from inputt.scripts import resume
    for well in resume.inje_lst:
       ref.add(ref.join(well.name, *well.nickname_lst))
