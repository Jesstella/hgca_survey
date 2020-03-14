# Necessary Modules 
import numpy as np 
import pandas as pd
from astropy.io import fits
from astropy.table import Table
from collections import defaultdict

# Downloading new HGCA file
hdul = fits.open('/Users/Jess/HGCA_survey_paper/HGCA_vDR2_withchisq.fits')
data = hdul[1].data
evt_data = Table(data)

hip_id = list(evt_data.field(0)) # HIP ID column
chi_2 = list(evt_data.field(37)) # Chi2 column

# HIP IDs for wich Chi2 values are needed
hip_needed = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')['hip_id']

# Indexes from the hip_full list
# These will be in the right order because they were mapped originally to the hip_needed values. 

d = defaultdict(list)
for index, item in enumerate(hip_id):
     d[item].append(index)

matches = [index for item in hip_needed for index in d[item] if item in d]
print('There are matches to ' + str(len(matches)) + ' stars.')

# Use the index for the HIP IDs to find the corresponding chi2 values

final_chi2 = []

for i in matches: 
    final_chi2.append(chi_2[i])

print('There are ' + str(len(final_chi2)) + ' chi2 values.')

# Save to file that can be added, as a column, to the spreadsheet

rows = final_chi2
header = ['chi2']
chi2 = pd.DataFrame(rows, columns=header)
chi2.to_csv('/Users/Jess/HGCA_survey_paper/chi2.csv')

# Testing for chi2 we expect (143 = 84.4 and 159 = 0.23)
print(evt_data.field(0)[141])
print(evt_data.field(37)[141])
print(evt_data.field(0)[157])
print(evt_data.field(37)[157])

