import pandas as pd
import numpy as np
from main import *
import os

city_dict = {"Ashdod": ASHDOD, "Carmel": CARMEL, "Gosh": GOSH_DAN, "Kiryat": KIRYAT_GAT, "Meron": MERON,
             "Modiin": MODIIN, "Ofakim": OFAKIM, "Tseelim": TSEELIM, "YABA": YABA}


def get_first_name(file_path):
    base = os.path.basename(file_path)
    return base.split("_")[0]


# biggest_id = 0
# all_tables = []

def combine_all_tables(loc_in_dir):
    """param should look like this: input/with_id/With ID/Target bank data/"""
    all_tables_by_id = {}
    list_of_csv_dir = [loc_in_dir + i for i in os.listdir(loc_in_dir)]
    for csv_dir in list_of_csv_dir:
        file = load_file(csv_dir, city_dict[get_first_name(csv_dir)])
        tables = separate_by_ids(file)
        for table in tables:
            table.sort_values(by='time', inplace=True)
            table.reset_index(inplace=True)
            id = table['ID'][0]
            if id in all_tables_by_id.keys():
                all_tables_by_id[id] = pd.concat([all_tables_by_id[id], table], axis=0)
            else:
                all_tables_by_id[id] = table

    return all_tables_by_id


        # all_tables.append(table)
        # if table['ID'][0] > biggest_id:
        #     biggest_id = table['ID'][0]

# all_tables_by_id = {key:0 for key in range(1, int(biggest_id)+1)}
# for table_index in range(len(all_tables)):
#     current_id = all_tables[table_index]['ID'][0]
#     if all_tables_by_id[current_id] == 0:
#         all_tables_by_id[current_id] = table_index
#     else:
#         all_tables_by_id[current_id] = pd.concat([all_tables_by_id[current_id], table_index], axis=0)

