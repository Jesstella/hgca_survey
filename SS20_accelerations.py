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
err_parallax = my_sample['gaia_parallex_err']

hip_id = my_sample['hip_id']

rad_vel = my_sample['rad_vel']
err_rad_vel = my_sample['rad_vel_err']

pmra_hip = my_sample['pmra_hip']
err_pmra_hip = my_sample['pmra_hip_error']

pmdec_hip = pmdec_hip
err_pmdec_hip = my_sample['pmdec_hip_error']

pmra_gaia = my_sample['pmra_gaia']
err_pmra_gaia = my_sample['pmra_gaia_err']

pmdec_gaia = my_sample['pmdec_gaia']
err_pmdec_gaia = my_sample['pmdec_gaia_err']

pmra_hg = my_sample['pmra_hg']
err_pmra_hg = my_sample['pmra_hg_error']

pmdec_hg = my_sample['pmdec_hg']
err_pmdec_hg = my_sample['pmdec_hg_error']

epoch_ra_gaia = my_sample['epoch_ra_gaia']
epoch_dec_gaia = my_sample['epoch_dec_gaia']
epoch_ra_hip = my_sample['epoch_ra_hip']
epoch_dec_hip = my_sample['epoch_dec_hip']

pmrahipl, pmrahipel, pmragaial, pmragaiael, pmrahgl, pmrahgel, pmdechipl, pmdechipel, pmdecgaial, pmdecgaiael, pmdechgl, pmdechgel, rahipepochl, ragaiaepochl, dechipepochl, decgaiaepochl, plxl, plxel = ([] for i in range(18))

# Cycle through each star and create lists of the values needed in the right units. 
for i in range(len(hip_id)):

    pmrahipl.append(pmra_hip.iloc[i]*u.mas/u.yr) #mas/yr
    pmrahipel.append(err_pmra_hip.iloc[i]*u.mas/u.yr)
    
    pmragaial.append(pmra_gaia.iloc[i]*u.mas/u.yr) #mas/yr
    pmragaiael.append(err_pmra_gaia.iloc[i]*u.mas/u.yr)
    
    pmrahgl.append(pmra_hg.iloc[i]*u.mas/u.yr) #mas/yr
    pmrahgel.append(err_pmra_hg.iloc[i]*u.mas/u.yr)
    
    pmdechipl.append(pmdec_hip.iloc[i]*u.mas/u.yr) #mas/yr
    pmdechipel.append(err_pmdec_hip.iloc[i]*u.mas/u.yr)
    
    pmdecgaial.append(pmdec_gaia.iloc[i]*u.mas/u.yr) #mas/yr
    pmdecgaiael.append(err_pmdec_gaia.iloc[i]*u.mas/u.yr)
    
    pmdechgl.append(pmdec_hg.iloc[i]*u.mas/u.yr) #mas/yr
    pmdechgel.append(err_pmdec_hg.iloc[i]*u.mas/u.yr)
    
    rahipepochl.append(epoch_ra_hip.iloc[i]*u.yr) #yr
    ragaiaepochl.append(epoch_ra_gaia.iloc[i]*u.yr) #yr
    dechipepochl.append(epoch_dec_hip.iloc[i]*u.yr) #yr
    decgaiaepochl.append(epoch_ra_gaia.iloc[i]*u.yr) #yr
    
    plxl.append((parallax.iloc[i])*u.mas) #parallax in mas
    plxel.append((err_parallax.iloc[i])*u.mas)

# Determine the distance to each of the stars.
d_list = []
d_4_err = []
d_err_list = []

for i in range(len(plxl)):    
    d = plxl[i].to(u.parsec, equivalencies=u.parallax())
    d_list.append(d)

    a = 1/(plxl[i]*1e-3)
    b = str(a)[:-8]
    c = float(b)
    d_4_err.append(c)
    
    d = (plxel[i] / (plxl[i]**2))
    e = str(d)[:-8]
    f = float(e)
    d_err_list.append(f)

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
acc_ral, acc_rael, acc_decl, acc_decel = [], [], [], []

for i in range(len(acc_ra_numl)):
    acc_ral.append(acc_ra_num2[i] / acc_ra_denl[i])
    acc_decl.append(acc_dec_num2[i] / acc_dec_denl[i])
    
    err_acc_ra = np.sqrt((err_pmra_gaia[i]/pmra_gaia[i])**2 + (err_pmra_hg[i]/pmra_hg[i])**2 + (d_err_list[i]**2/d_4_err[i]**4))
    err_acc_dec = np.sqrt((err_pmdec_gaia[i]/pmdec_gaia[i])**2 + (err_pmdec_hg[i]/pmdec_hg[i])**2 + (d_err_list[i]**2/d_4_err[i]**4))
    
    acc_rael.append(err_acc_ra)
    acc_decel.append(err_acc_dec)

# Combine the acceleration in RA and Dec in quadrature to determine the astrometric acceleration, and save to a list.
astrometric_accel_quantity = []
err_astrometric_accel_quantity = []

for i in range(len(acc_ral)):
    astrometric_acc = np.sqrt(acc_ral[i] ** 2 + acc_decl[i] ** 2)
    astrometric_accel_quantity.append(astrometric_acc)
    
for i in range(len(acc_decel)):
    err_astrometric_acc = np.sqrt(acc_rael[i] ** 2 + acc_decel[i] ** 2)
    err_astrometric_accel_quantity.append(err_astrometric_acc)
    
astrometric_accel = []
astrometric_accel_err = []

for i in range(len(astrometric_accel_quantity)):
    str_i = str(astrometric_accel_quantity[i])
    str_ii = str(err_astrometric_accel_quantity[i])
    
    str_i_cut = str_i[0:-10]
    str_ii_cut = str_ii[0:-10]
    
    astrometric_accel.append(str_i_cut)
    astrometric_accel_err.append(str_ii_cut)

# Create a csv file with the acceleration column
header = ['acceleration', 'acceleration_err']
row = zip(astrometric_accel, astrometric_accel_err)
accel_file = pd.DataFrame(row, columns=header)
accel_file.to_csv('/Users/Jess/HGCA_survey_paper/accelerations.csv', index=False)


