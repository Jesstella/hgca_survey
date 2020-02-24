# Necessary Modules 
import pandas as pd
from astropy.coordinates import SkyCoord, Distance
from astropy import units as u
from astropy.time import Time
import numpy as np
import time

# Reading in the HGCA megafile
megafile = pd.read_csv('/Users/Jess/HGCA_survey_paper/megafile.csv')
print('There are ' + str(len(megafile)) + ' HCGA stars.')

# Reading in KOA file
koafile = pd.read_csv('/Users/Jess/Downloads/new_keck_stars_edited.csv')
print('There are ' + str(len(koafile)) + ' files in the KOA database.')

# Create a list of unique observation dates
myset = set(koafile['date'])
myset = list(myset)
print('The KOA list of files has ' + str(len(koafile['date'])) + ' files, which have ' + str(len(myset)) + ' unique observation dates.')

# Determine the average epoch time
ave_time = (megafile['epoch_ra_gaia'] + megafile['epoch_dec_gaia']) / 2

# Set up catalog of all the stars in the megafile
c = SkyCoord(ra = list(megafile['ra'])*u.deg, dec = list(megafile['dec'])*u.deg, 
distance = Distance(parallax = list(megafile['gaia_parallax']) * u.mas), 
pm_ra_cosdec = list(megafile['pmra_gaia']) * u.mas/u.yr, 
pm_dec = list(megafile['pmdec_gaia']) * u.mas/u.yr, 
obstime = Time(ave_time, format='decimalyear'))
print(len(c))

# Set up a catalog of...
catalog = SkyCoord(ra=koafile['ra']*u.degree, dec=koafile['dec']*u.degree)
clean = (~np.isnan(catalog.ra) & ~np.isnan(catalog.dec))
print('The initial file has ' + str(len(catalog)) + ' lines,') 
print('After being cleaned it has ' + str(clean.sum()) + ' lines,')
print('Meaning that ' + str(len(catalog)-clean.sum()) + ' files have been removed.')
catalog_clean = catalog[clean]

t0 = time.time()

for j in range(len(myset)):
    print('Running for KOA date No# ' + str(j) + ': ' + str(myset[j])) 
    sc = c.apply_space_motion(new_obstime=Time(myset[j]))
    idxsc, idxcatalog, d2d, d3d = catalog_clean.search_around_sky(sc, 20*u.arcsecond)
    
t1 = time.time()
total = t1-t0
print('The time to run this code segment is ' + str(total/60) + 'minutes.')

idx_set = set(idxsc)
print('There are ' + str(len(idx_set)) + ' unique stars in this list.')

idx_set = list(idx_set)
matches = c[idx]
cross_matched_stars = megafile.iloc[idx_set]
cross_matched_stars.to_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')

print("There are " + str(len(cross_matched_stars)) + ' matches.')
