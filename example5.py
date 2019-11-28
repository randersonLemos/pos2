import pandas
import pathlib

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from scripts import utils

    from config.scripts import settings as sett

    sim_group_folders = []
    sim_group_folders.append('SIM_ICV_2_STGS')
    sim_group_folders.append('SIM_ICV_3_STGS')
    sim_group_folders.append('SIM_ICV_4_STGS')
    sim_group_folders.append('SIM_ICV_5_STGS')
    sim_group_folders.append('SIM_ICV_6_STGS')
    sim_group_folders.append('SIM_ICV_7_STGS')
    sim_group_folders.append('SIM_ICV_8_STGS')

    for sim_group_folder in sim_group_folders:
        path_to_eco_file = sett.ECO_ROOT / sim_group_folder / sett.ECO_NAME

        df = []
        df = pandas.read_csv(path_to_eco_file, sep=';')[['MODEL', 'NPVF']]

        df.index.name = 'index'
        df.index += 1

        df['SIM_GROUP'] = sim_group_folder

        df['MODEL'] = df['MODEL'].str[:-5]

        for idi, i in enumerate(range(250, 5250, 250)):
                df.loc[idi+1, 'CATEGORY'] = '{}'.format(i)

        output_dir = pathlib.Path('csv') / sim_group_folder
        output_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_dir / 'npvfs.csv', index=True)
