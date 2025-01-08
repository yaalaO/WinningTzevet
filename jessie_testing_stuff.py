###################################
#     finding averege framerate   #
#############################3##3##
import pandas as pd
from main import *






df = load_file(
        "input/with_id/With ID/Target bank data/Kiryat_Gat_with_ID.csv", KIRYAT_GAT)
sum1 = 0
for i in range(len(df)-1):
    sum1 += -df['time'][i] + df['time'][i+1]
print(sum1/len(df))

