# Necessary Modules
from astroquery.vizier import Vizier
import pandas as pd
import time
import numpy as np
import astropy.units as u
import csv

# Data for the names of WDS stars and how many components are in the system. 
wds_values = pd.read_csv('/Users/Jess/HGCA_survey_paper/wds_values.csv')['wds_companions']
wds_names = pd.read_csv('/Users/Jess/HGCA_survey_paper/wds_values.csv')['wds_names']

# Cutting out the stars that have no companions as we do not want to waste time.
wds_names = list(wds_names)
wds_names_cut = []

for i in wds_names:
    if i == '0':
        continue
    else:
        wds_names_cut.append(i)

print('There are ' + str(len(wds_names_cut)) + ' systems with multiple components.')

# Calling Vizier and setting limits
Vizier.ROW_LIMIT = 210000
Vizier.TIMEOUT = 500

# Defining the search query for Vizier (the same as when the initial companion search took place.)
def query(x):
    result = Vizier.query_region('WDS' + str(x), radius=0.1*u.arcsec, catalog=['B/wds/wds'])
    return result 

# Gathering the data from each of the system components and saving it into an individual csv file for each system.
path = '/Users/Jess/HGCA_survey_paper/wds_companions/'
t0 = time.time()

for i in wds_names_cut:
    print('WDS' + str(i))
    result = query(i)
    df = result['B/wds/wds']
    df.write(path + 'wds_companion_WDS_' + str(i) + '.csv')
        
t1 = time.time()
total = t1-t0
print('Time for this segment to run: ' + str(total/60) + ' minutes.')

