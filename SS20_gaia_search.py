# Necessary modules 
import astropy.units as u
from astroquery.gaia import Gaia
import pandas as pd
import time
import numpy as np
from astropy.coordinates import SkyCoord

# Pulling the sample to search.
my_sample = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')

# Making lists for the Gaia RA and Dec.
gaia_ra = my_sample['ra']
gaia_dec = my_sample['dec']

# Setting the radius around which to search.
radius = u.Quantity(5.0, u.arcsec)

# Querying Gaia database for all stars in list.
t0 = time.time()
 
gaia_companions = []
i_list = np.arange(0, len(gaia_ra), 1)

# Cycling through all HIP stars.
for i in i_list:
    
    # Setting up an object to search around and searching around it
    coord = SkyCoord(ra=gaia_ra[i], dec=gaia_dec[i], unit=(u.degree, u.degree), frame='icrs')
    j = Gaia.cone_search_async(coord, radius)
    r = j.get_results()
    
    # Determining how many companions (will be -1 because primary appears)
    comps = str(len(r)-1)
    print(comps)
    gaia_companions.append(comps)

t1 = time.time()
total = t1-t0
print('Time to run this segment: ' + str(total/60) + ' minutes.')

print('There should be ' + str(len(my_sample)) + ' stars in this file.\nThere are ' + str(len(gaia_companions)))

rows = list(zip(gaia_companions))
header = ['gaia_comps']
rows = pd.DataFrame(rows, columns=header)
rows.to_csv('/Users/Jess/HGCA_survey_paper/gaia_companions.csv')
