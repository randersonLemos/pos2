import pandas
import pathlib

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from scripts import utils
    from config.scripts import settings as sett

    sim_group_folders = []
    sim_group_folders.append('SIM_ICV_01_STG')
    sim_group_folders.append('SIM_ICV_02_STG')
    sim_group_folders.append('SIM_ICV_02_STG_HRD')
    sim_group_folders.append('SIM_ICV_02_STG_SMT')
    sim_group_folders.append('SIM_ICV_03_STG')
    sim_group_folders.append('SIM_ICV_03_STG_HRD')
    sim_group_folders.append('SIM_ICV_03_STG_SMT')
    sim_group_folders.append('SIM_ICV_04_STG')
    sim_group_folders.append('SIM_ICV_04_STG_HRD')
    sim_group_folders.append('SIM_ICV_04_STG_SMT')
    sim_group_folders.append('SIM_ICV_05_STG')
    sim_group_folders.append('SIM_ICV_05_STG_HRD')
    sim_group_folders.append('SIM_ICV_05_STG_SMT')

    for sim_group_folder in sim_group_folders:
        path_to_npv_file = sett.NPV_ROOT / sett.SIMS_FOLDER / sim_group_folder / sett.NPV_NAME

        df = []
        df = pandas.read_csv(path_to_npv_file, sep=';')[['MODEL', 'NPVF']]

        df.index.name = 'index'
        df.index += 1
        df['SIM_GROUP'] = sim_group_folder
        df['MODEL'] = df['MODEL'].str[:-5]

        for idi, i in enumerate(range(250, 5250, 250)):
                df.loc[idi+1, 'CATEGORY'] = '{}'.format(i)

        output_dir = sett.CSV_ROOT / sett.SIMS_FOLDER/ sim_group_folder / sett.NPV_NAME
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_dir, index=True)
