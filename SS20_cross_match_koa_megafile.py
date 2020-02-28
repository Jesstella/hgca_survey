# Necessary Modules 
import pandas as pd
from astropy.coordinates import SkyCoord, Distance
from astropy import units as u
from astropy.time import Time
import numpy as np
import time
import glob

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

# Breaking down the KOA file into groups by date
a = 0
for i in myset:
    df = koafile[koafile["date"] == i]
    df.to_csv('/Users/Jess/HGCA_survey_paper/koa_date' + str(a) + '.csv')
    a = a + 1

# Setting timer for segment
t0 = time.time()

# list to save final indexes
total_indices = []

# Opening each of the files - there is one for each date, each containing all observations at that date. 
koa_dates = glob.glob('/Users/Jess/HGCA_survey_paper/koa_date*.csv')

# Loop through each date 
for i in koa_dates:
    koad = pd.read_csv(i) # Date file generally 
    print('There are ' + str(len(koad)) + ' KOA observations with this date.')
    
    koadd = pd.read_csv(i)['date'][0] # The specific date in this file
    print('Shifting HGCA stars to date No#: ' + str(koadd)) 
    
    # Set up catalog of all the stars in the megafile
    c = SkyCoord(ra = list(megafile['ra'])*u.deg, dec = list(megafile['dec'])*u.deg, 
    distance = Distance(parallax = list(megafile['gaia_parallax']) * u.mas), 
    pm_ra_cosdec = list(megafile['pmra_gaia']) * u.mas/u.yr, 
    pm_dec = list(megafile['pmdec_gaia']) * u.mas/u.yr, 
    obstime = Time(ave_time, format='decimalyear'))
   
    # Shift the megafile to the new observation date
    sc = c.apply_space_motion(new_obstime=Time(koadd))
        
    # Create a catalog for the KOA observations at this date, removing the 'NaN' values
    catalog = SkyCoord(ra=koad['ra']*u.degree, dec=koad['dec']*u.degree)
    clean = (~np.isnan(catalog.ra) & ~np.isnan(catalog.dec))
    catalog_clean = catalog[clean]
        
    # Search around the sky 
    idxcatalog, idxsc, d2d, d3d = sc.search_around_sky(catalog_clean, 20*u.arcsecond)
    print('There are ' + str(len(set(idxsc))) + ' stars in HGCA that are also present in KOA observations. \n')
    
    # Save indices for matches found
    for x in idxsc:
        total_indices.append(x)

# Complete timer
t1 = time.time()
total = t1-t0
print('The time to run this code segment is ' + str(total/60) + 'minutes.')

# Matching the indices to rows in the megafile and saving as a new csv.
print('There are ' + str(len(set(total_indices))) + ' unique stars in this list.')
idx_set = list(set(total_indexes))
cross_matched_stars = megafile.iloc[idx_set]
cross_matched_stars.to_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')

