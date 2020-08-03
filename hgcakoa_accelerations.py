# Necessary modules 
import pandas as pd
import astropy.units as u
import numpy as np
import os 

os.remove('/Users/Jess/HGCA_survey_paper/accelerations_electronic_table.csv')

# Pulling the sample to search.
my_sample = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')
pmdec_hip_file = pd.read_csv('/Users/Jess/HGCA_survey_paper/pmdec_hip.csv')

parallax = my_sample['gaia_parallax']
err_parallax = my_sample['gaia_parallex_err']
hip_id = my_sample['hip_id']
pmra_hip = my_sample['pmra_hip']
err_pmra_hip = my_sample['pmra_hip_error']
pmdec_hip = pmdec_hip_file['pmdec_hip']
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
    decgaiaepochl.append(epoch_dec_gaia.iloc[i]*u.yr) #yr
    
    plxl.append((parallax.iloc[i])*u.mas) #parallax in mas
    plxel.append((err_parallax.iloc[i])*u.mas)

# Determine the distance to each of the stars.
d_list = []
d_err_list = []

for i in range(len(plxl)):    
    d = plxl[i].to(u.parsec, equivalencies=u.parallax())
    d_list.append(d)
    
    plxl_quant = plxl[i].to(u.parsec, equivalencies=u.parallax())
    plxl_err_quant = plxel[i].to(u.parsec, equivalencies=u.parallax())
    
    d = ((plxl_quant)**2) / (plxl_err_quant)
    d_err_list.append(d.to(u.pc))

# Set up lists for acceperations that will be calculated. 
acc_ra_numl, acc_ra_denl, acc_dec_numl, acc_dec_denl, acc_ra_num2, acc_dec_num2 = ([] for i in range(6))

# Cycle through all stars and determine the numerator and denominator of later equations. 
# del mu (in mas/yr) * parallax (in parsec) converted to (mas pc/yr)
for i in range(len(d_list)):
#    # Acceleration in RA
    acc_ra_numl.append((pmragaial[i] - pmrahgl[i]) * d_list[i]) # Numerator 
    acc_ra_denl.append((ragaiaepochl[i] - rahipepochl[i]) / 2) # Denominator
#    
#    # Acceleration in Dec
    acc_dec_numl.append((pmdecgaial[i] - pmdechgl[i]) * d_list[i]) # Numerator 
    acc_dec_denl.append((decgaiaepochl[i] - dechipepochl[i]) / 2) # Demoninator
#    
#    # Change the units in both of the numerators
    acc_ra_num2.append(acc_ra_numl[i].to(u.m / u.second, equivalencies=u.dimensionless_angles()))
    acc_dec_num2.append(acc_dec_numl[i].to(u.m / u.second, equivalencies=u.dimensionless_angles()))

# Use these numerators and denominators to determine the acceleration in RA and Dec
acc_ral, acc_rael, acc_decl, acc_decel =  [], [], [], []

for i in range(len(acc_ra_numl)):
    # Acceleration in RA and Dec
    acc_ral.append(acc_ra_num2[i] / acc_ra_denl[i]) # RA 
    acc_decl.append(acc_dec_num2[i] / acc_dec_denl[i]) # Dec)

ra_error = []
dec_error = []

for i in range(len(pmra_gaia)):
    const = 2 / (ragaiaepochl[i] - rahipepochl[i])
    
    term_1 = (d_list[i] * pmragaiael[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    term_2 = (d_list[i] * pmrahgel[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    term_3 = ((pmragaial[i] - pmrahgl[i]) * d_err_list[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    
    ra_err = const * np.sqrt((term_1)**2 + (term_2)**2 + (term_3)**2)
    ra_error.append(ra_err)
    
    const_2 = 2 / (decgaiaepochl[i] - dechipepochl[i])
    
    term_a = (d_list[i] * pmdecgaiael[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    term_b = (d_list[i] * pmdechgel[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    term_c = ((pmdecgaial[i] - pmdechgl[i]) * d_err_list[i]).to(u.m / u.second, equivalencies=u.dimensionless_angles())
    
    dec_err = const_2 * np.sqrt((term_a)**2 + (term_b)**2 + (term_c)**2)
    dec_error.append(dec_err)

# Combine the acceleration in RA and Dec in quadrature to determine the astrometric acceleration, and save to a list.
astrometric_accel_quantity = []

for i in range(len(acc_ral)):
    astrometric_acc = np.sqrt(acc_ral[i] ** 2 + acc_decl[i] ** 2)
    astrometric_accel_quantity.append(astrometric_acc)

accel_error = []

for i in range(len(ra_error)):
    term_1 = (acc_ral[i] / astrometric_accel_quantity[i])**2 * (ra_error[i])**2 
    
    term_2 = (acc_decl[i] / astrometric_accel_quantity[i])**2 * (dec_error[i])**2 
    covariance = np.cov([ra_error[i].value, dec_error[i].value])
    covariance_value = covariance * (u.m / u.second / u.year)**2
    
    term_3 = (2 * acc_ral[i] * acc_decl[i] * covariance_value) / astrometric_accel_quantity[i]**2
    
    error = np.sqrt(term_1 + term_2 + term_3)
    
    accel_error.append(error)
    
astrometric_accel = []
ra_acceleration = []
dec_acceleration = []
ra_acceleration_error = []
dec_acceleration_error = []
full_acceleration_error = []

for i in range(len(astrometric_accel_quantity)):
    str_i = str(astrometric_accel_quantity[i])
    str_i_cut = str_i[0:-11]
    astrometric_accel.append(float(str_i_cut))
    
    str_j = str(acc_ral[i])
    str_j_cut = str_j[0:-11]
    ra_acceleration.append(float(str_j_cut))
    
    str_k = str(acc_decl[i])
    str_k_cut = str_k[0:-11]
    dec_acceleration.append(float(str_k_cut))
    
    str_l = str(ra_error[i])
    str_l_cut = str_l[0:-11]
    ra_acceleration_error.append(float(str_l_cut))
    
    str_m = str(dec_error[i])
    str_m_cut = str_m[0:-11]
    dec_acceleration_error.append(float(str_m_cut))
    
    str_n = str(accel_error[i])
    str_n_cut = str_n[0:-11]
    full_acceleration_error.append(float(str_n_cut))

# Create a csv file with the acceleration column
header = ['hip_id', 'acceleration', 'accel_err', 'accel_ra', 'accel_dec', 'ra_err', 'dec_err']
row = zip(hip_id, astrometric_accel, full_acceleration_error, ra_acceleration, dec_acceleration, ra_acceleration_error, dec_acceleration_error)
accel_file = pd.DataFrame(row, columns=header)
accel_file.to_csv('/Users/Jess/HGCA_survey_paper/accelerations.csv', index=False)

header = ['hip_id', 'accel_ra', 'ra_err', 'accel_dec', 'dec_err', 'acceleration', 'accel_err']
row = zip(hip_id, ra_acceleration, ra_acceleration_error, dec_acceleration, dec_acceleration_error, astrometric_accel, full_acceleration_error)
accel_file = pd.DataFrame(row, columns=header)
accel_file.to_csv('/Users/Jess/HGCA_survey_paper/accelerations_electronic_table.csv', index=False)

print('Accelerations computed! Do not forget the electronic table header!')



