import pandas as pd
import numpy as np
from main import *
import os







loc_in_dir = "input/with_id/With ID/Target bank data/"
list_of_csv_dir = [loc_in_dir + i for i in os.listdir(loc_in_dir)]
print(list_of_csv_dir)