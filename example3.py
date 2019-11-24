import os
import pathlib

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from scripts import utils
    import pathlib
    from scripts import utils

    from config.scripts import settings as sett

    path_to_sim_group = sett.REP_ROOT / 'SIM_ICV_2_STGS'
    tables = []
    for folder in os.listdir(str(path_to_sim_group)):
        path_to_sim_folder = path_to_sim_group / folder
        if os.path.isdir(path_to_sim_folder):
            path_to_rep_file = path_to_sim_folder / sett.REP_NAME
            tables.append(utils.get_tables(str(path_to_rep_file)))
