import pandas
import pathlib

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from scripts import utils

    from config.scripts import settings as sett

    #############
    # REFERENCE #
    #############

    sim_group_folder = 'REFERENCE'
    path_to_eco_file = sett.ECO_ROOT / sim_group_folder / sett.ECO_NAME

    df = []
    df = pandas.read_csv(path_to_eco_file, sep=';')[['MODEL', 'NPVF']]

    df.index.name = 'index'
    df.index += 1

    df['SIM_GROUP'] = sim_group_folder

    df['MODEL'] = df['MODEL'].str[:-5]

    df['CATEGORY'] = '(none;none)'

    output_dir = pathlib.Path('csv') / sim_group_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_dir / 'npvfs.csv', index=True)

    ##################
    # SIM_ICV_2_STGS #
    ##################

    sim_group_folder = 'SIM_ICV_2_STGS_EXTENDED'
    path_to_eco_file = sett.ECO_ROOT / sim_group_folder / sett.ECO_NAME

    df = []
    df = pandas.read_csv(path_to_eco_file, sep=';')[['MODEL', 'NPVF']]

    df.index.name = 'index'
    df.index += 1

    df['SIM_GROUP'] = sim_group_folder

    df['MODEL'] = df['MODEL'].str[:-5]

    for idi, i in enumerate(range(250, 5250, 250)):
        for idj, j in enumerate(range(75, 100, 5)):
            df.loc[idi*5+idj+1, 'CATEGORY'] = '({:d};{:4.2f})'.format(i,j/100)

    output_dir = pathlib.Path('csv') / sim_group_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_dir / 'npvfs.csv', index=True)
