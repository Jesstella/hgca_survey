# Necessary Modules
import numpy as np 
import pandas as pd

# Open spreadsheet to pull wds and koa companion data
compiled_spreadsheet = pd.read_csv('/Users/Jess/HGCA_survey_paper/final_spreadsheet.csv')
wds_comps = compiled_spreadsheet['wds_comps']
koa_comps = compiled_spreadsheet['koa']

# Create a boolean list for WDS as it contains the number of stars in the system
wds_bool = []
for i in wds_comps:
    if i == 0:
        wds_bool.append(0)
    else:
        wds_bool.append(1)

# Find the stars that have both KOA and WDS companions
matches = []
for i in range(len(wds_bool)):
    if wds_bool[i] == 1 and koa_comps[i] == 1:
        matches.append(1)
    else:
        matches.append(0)

# Find the appropriate HIP IDs for these stars
hip_id = []
for i in range(len(wds_bool)):
    if matches[i] == 1:
        hip_id.append(compiled_spreadsheet['hip_id'][i])
    else:
        continue

print('There are ' + str(len(hip_id)) + ' systems with companions in both WDS and KOA.')

# Determine the indexes of these HIP IDs in the final spreadsheet
compiled_index = []

for i in hip_id:
    a = compiled_spreadsheet.loc[compiled_spreadsheet['hip_id'] == i].index[0]
    compiled_index.append(a)

# Pull these rows and save to a seperate spreadsheet
cut_spreadsheet = compiled_spreadsheet.iloc[compiled_index]
cut_spreadsheet.to_csv('/Users/Jess/HGCA_survey_paper/koa_wds_comps.csv', index=False)
