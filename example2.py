import os
import pathlib
from scripts import utils

if __name__ == '__main__':
    path_to_sim_group = pathlib.Path('/media/pamonha/DATA/sim_group_002')
    tables = []
    for sim_folder in os.listdir(str(path_to_sim_group)):
        path_to_rep_file = path_to_sim_group / sim_folder / 'main.rep'
        tables.append(utils.get_tables(str(path_to_rep_file)))
        break

