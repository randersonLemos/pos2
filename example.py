# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""

import pathlib
from scripts import utils

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from config.scripts import settings as sett

    sim_folder = 'sim_000'
    path_to_rep_file = sett.LOCAL_ROOT  / sett.SIMS_FOLDER / sim_folder / sett.REP_NAME
    ref = utils.get_tables(path_to_rep_file)
    ref.to_csv('csvs/{}'.format(sim_folder))

    from post_process.scripts import sector_graph
    sGraph = sector_graph.Sector_Graph(ref)

    from inputt.scripts.infos import prods_lst
    from post_process.scripts import well_graph
    pGraph = well_graph.Producer_Graph(prods_lst, ref)

    from post_process.scripts import special_graph
    spGraph = special_graph.Special_Graph(prods_lst, ref)
