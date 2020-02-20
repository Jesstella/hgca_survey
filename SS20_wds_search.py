from astroquery.vizier import Vizier
import pandas as pd
import time
import numpy as np
import astropy.units as u

hip_id = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')['hip_id']
print('There are ' + str(len(hip_id)) + ' stars in the file.')

full_hip_name = []
for i in range(len(hip_id)):
    new_name = 'HIP ' + str(hip_id[i])
    full_hip_name.append(new_name)

# Set columns wanted from vizier and the row limit 
v = Vizier(columns=['WDS'])
Vizier.ROW_LIMIT = 210000
Vizier.TIMEOUT = 500

# Defining function to query region around each HIP ID, using the WDS catalog.
def query(x):
    result = v.query_region(x, radius=0.1*u.arcsec, catalog=['B/wds/wds'])
    return result

# Searching each HIP ID in Vizier and returning either 0 (none) or a corresponding WDS ID.
t0 = time.time()

wds_names = [] 
wds_companions = []

i_list = np.arange(0, len(full_hip_name), 1)
for i in i_list:
    print(full_hip_name[i])
    result = query(full_hip_name[i])
    res = str(result)
    
    if res == 'Empty TableList':
        wds_names.append(0)
        wds_companions.append(0)
        
    else: 
        wds_names.append(result['B/wds/wds']['WDS'][0]) 
        wds_companions.append(res[61:-7])
        
t1 = time.time()
total = t1-t0
print('Time for this segment to run: ' + str(total/60) + ' minutes.')

# Check to make sure all of the stars are accounted for.
print(str(len(wds_names)) + ' HIP IDs were checked in this process, out of ' + str(len(hip_id)) + '.')

# Downloading the complete WDS catalog and pull other values using the WDS IDs.
wds_table = Vizier.get_catalogs(['B/wds/wds'])

obs1, obs2, pa1, pa2, sep1, sep2, mag1, mag2 = [],[],[],[],[],[],[],[]
 
for i in range(len(wds_names)): 
    if wds_names[i] == 0:
        obs1.append(0)
        obs2.append(0)
        pa1.append(0)
        pa2.append(0)
        sep1.append(0)
        sep2.append(0)
        mag1.append(0)
        mag2.append(0)
    else: 
        obs1.append(wds_table['B/wds/wds']['Obs1'][0])
        obs2.append(wds_table['B/wds/wds']['Obs2'][0])
        pa1.append(wds_table['B/wds/wds']['pa1'][0])
        pa2.append(wds_table['B/wds/wds']['pa2'][0])
        sep1.append(wds_table['B/wds/wds']['sep1'][0])
        sep2.append(wds_table['B/wds/wds']['sep2'][0])
        mag1.append(wds_table['B/wds/wds']['mag1'][0])
        mag2.append(wds_table['B/wds/wds']['mag2'][0])   

# Calculating the magnitude difference between the primary and secondary star.
mag_diff = np.array(mag2) - np.array(mag1)

# Saving to CSV. 
rows = list(zip(wds_names, wds_companions, obs1, obs2, pa1, pa2, sep1, sep2, mag1, mag2, mag_diff))
header = ['wds_names', 'wds_companions', 'obs1', 'obs2', 'pa1', 'pa2', 'sep1', 'sep2', 'mag1', 'mag2', 'mag_diff']
rows = pd.DataFrame(rows, columns=header)
rows.to_csv('/Users/Jess/HGCA_survey_paper/wds_values.csv', index=False)
