# ACKNOWLEDGEMENT: Code based on accelerations code written by Elena Mitra.

# Necessary modules 
import pandas as pd
import csv
import astropy.units as u
import numpy as np

# Pulling the sample to search.
my_sample = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')
pmdec_hip = pd.read_csv('/Users/Jess/HGCA_survey_paper/pmdec_hip.csv')

# Pulling necessary values from the data table.
parallax = my_sample['gaia_parallax']
hip_id = my_sample['hip_id']
rad_vel = my_sample['rad_vel']
pmra_hip = my_sample['pmra_hip']
pmdec_hip = pmdec_hip
pmra_gaia = my_sample['pmra_gaia']
pmdec_gaia = my_sample['pmdec_gaia']
pmra_hg = my_sample['pmra_hg']
pmdec_hg = my_sample['pmdec_hg']
epoch_ra_gaia = my_sample['epoch_ra_gaia']
epoch_dec_gaia = my_sample['epoch_dec_gaia']
epoch_ra_hip = my_sample['epoch_ra_hip']
epoch_dec_hip = my_sample['epoch_dec_hip']

pmrahipl, pmragaial, pmrahgl, pmdechipl, pmdecgaial, pmdechgl, rahipepochl, ragaiaepochl, dechipepochl, decgaiaepochl, plxl = ([] for i in range(11))

# Cycle through each star and create lists of the values needed in the right units. 
for i in range(len(hip_id)):

    pmrahipl.append(pmra_hip.iloc[i]*u.mas/u.yr) #mas/yr
    pmragaial.append(pmra_gaia.iloc[i]*u.mas/u.yr) #mas/yr
    pmrahgl.append(pmra_hg.iloc[i]*u.mas/u.yr) #mas/yr
    pmdechipl.append(pmdec_hip.iloc[i]*u.mas/u.yr) #mas/yr
    pmdecgaial.append(pmdec_gaia.iloc[i]*u.mas/u.yr) #mas/yr
    pmdechgl.append(pmdec_hg.iloc[i]*u.mas/u.yr) #mas/yr
    rahipepochl.append(epoch_ra_hip.iloc[i]*u.yr) #yr
    ragaiaepochl.append(epoch_ra_gaia.iloc[i]*u.yr) #yr
    dechipepochl.append(epoch_dec_hip.iloc[i]*u.yr) #yr
    decgaiaepochl.append(epoch_ra_gaia.iloc[i]*u.yr) #yr
    plxl.append((parallax.iloc[i])*u.mas) #parallax in mas

# Determine the distance to each of the stars.
d_list = []
for i in plxl:
    d = i.to(u.parsec, equivalencies=u.parallax())
    d_list.append(d)

# Set up lists for acceperations that will be calculated. 
acc_ra_numl, acc_ra_denl, acc_dec_numl, acc_dec_denl, acc_ra_num2, acc_dec_num2 = ([] for i in range(6))

# Cycle through all stars and determine the numerator and denominator of later equations. 
# del mu (in mas/yr) * parallax (in parsec) converted to (mas pc/yr)
for i in range(len(d_list)):
    acc_ra_numl.append((pmragaial[i] - pmrahgl[i])* d_list[i]) 
    acc_ra_denl.append((ragaiaepochl[i] - rahipepochl[i]) / 2)
    
    acc_dec_numl.append((pmdecgaial[i] - pmdechgl[i]) * d_list[i])
    acc_dec_denl.append((decgaiaepochl[i] - dechipepochl[i]) / 2)
    
    # Change the units in both of the numerators
    acc_ra_num2.append(acc_ra_numl[i].to(u.m / u.second, equivalencies=u.dimensionless_angles()))
    acc_dec_num2.append(acc_dec_numl[i].to(u.m / u.second, equivalencies=u.dimensionless_angles()))

# Use these numerators and denominators to determine the acceleration in RA and Dec
acc_ral, acc_decl = [], []

for i in range(len(acc_ra_numl)):
    acc_ral.append(acc_ra_num2[i] / acc_ra_denl[i])
    acc_decl.append(acc_dec_num2[i] / acc_dec_denl[i])

# Combine the acceleration in RA and Dec in quadrature to determine the astrometric acceleration, and save to a list.
astrometric_accel_quantity = []
for i in range(len(acc_ral)):
    astrometric_acc = np.sqrt(acc_ral[i] ** 2 + acc_decl[i] ** 2)
    astrometric_accel_quantity.append(astrometric_acc)

astrometric_accel = []
for i in astrometric_accel_quantity:
    str_i = str(i)
    str_i_cut = str_i[0:-10]
    astrometric_accel.append(str_i_cut)

# Create a csv file with the acceleration column
header = ['acceleration']
row = zip(astrometric_accel)
accel_file = pd.DataFrame(row, columns=header)
accel_file.to_csv('/Users/Jess/HGCA_survey_paper/accelerations.csv', index=False)
