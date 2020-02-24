# Necessary Modules
import pandas as pd
from astropy.io import fits
import csv

# Pulling pmdec_hip
# Getting list of hip_id and opening the DR2 file to retrieve list of pmdec_hip values and long list of HIP IDs.
new_hip_list = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')['hip_id']

fits_table_filename = '/Users/Jess/HGCA_survey_paper/HGCA_vDR2.fits'
hdul = fits.open(fits_table_filename)
data = hdul[1].data

pmdec_hip = data['pmdec_hip']
old_hip_list = list(data['hip_id'])

# Creating a list to keep the indices in
index_list = []

# Cycle round the list of new HIP IDs and determine the index they fall at in the long list
for i in new_hip_list:
    idx = old_hip_list.index(i)
    index_list.append(idx)
    
# Choose just these values of pmdec_hip
pmdec_hip = (pmdec_hip[index_list])

# Save these to a csv file
with open('/Users/Jess/HGCA_survey_paper/pmdec_hip.csv', 'w') as f:
    writer = csv.writer(f)
    for val in pmdec_hip:
        writer.writerow([val])
