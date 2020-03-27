# Necessary Modules 
import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt

koa_comps = pd.read_csv('/Users/Jess/HGCA_survey_paper/koa_companions_with_values.csv')
r = koa_comps['sep']
r_err = koa_comps['sep_err']
hip_id = koa_comps['hip_id']

full_sample = pd.read_csv('/Users/Jess/HGCA_survey_paper/final_spreadsheet.csv')
all_hip_id = full_sample['hip_id']
all_hip_id = list(all_hip_id)
parallax = full_sample['gaia_parallax']
para_err = full_sample['gaia_parallax_err']
astro_accel = full_sample['accel']
astro_accel_err = full_sample['accel_error']

G = 6.67e-11
print('Gravitational Constant in m^3kg^-1s^2$: ' + str(G))
M_S = 1.989e30
print('Mass of the Sun in kg: ' + str(M_S))
rv_accel = 0 

ind_for_para = []
for i in hip_id:
    if i in all_hip_id:
        index = all_hip_id.index(i)
        ind_for_para.append(index)
    else:
        continue
        
para_cut = []
para_error_cut = []
accel_cut = []
accel_error_cut = []
for i in ind_for_para:
    para_cut.append(parallax[i])
    para_error_cut.append(para_err[i])
    accel_cut.append(astro_accel[i])
    accel_error_cut.append(astro_accel_err[i])

distances_parsec = []
distances_error_parsec = []
min_mass = []
mass_error_list = []
AU_sep_list = []
AU_sep_list_error = []

for i in range(len(accel_error_cut)):
    rho = (r[i] * 1e-3 / 3600) * (math.pi / 180)
    rho_err = (r_err[i] * 1e-3 / 3600) * (math.pi / 180)
    
    dist = (1 / (para_cut[i] * 1e-3)) * 3.086e16
    dist_err = ((para_error_cut[i] * 1e-3) / ((para_cut[i] * 1e-3)**2)) * 3.086e16
    distances_parsec.append(dist/3.086e16)
    distances_error_parsec.append(dist_err/3.086e16)
    
    sep = rho * dist
    sep_in_AU = sep / 1.496e11
    AU_sep_list.append(sep_in_AU)
    sep_error = np.sqrt((rho_err/rho)**2 + (dist_err/dist)**2) * sep
    sep_error_AU = sep_error / 1.496e11
    AU_sep_list_error.append(sep_error_AU)
    
    a = accel_cut[i] / 3.154e7
    a_error = accel_error_cut[i] / 3.154e7
    
    M2 = (sep**2 * a) / G
    min_mass.append(M2/M_S)
    
    partial_S = (2 * sep * a) / G
    partial_a = sep**2 / a
    
    mass_error = np.sqrt((partial_S**2)*(sep_error**2) + (partial_a**2)*(a_error**2))
    mass_error_list.append(mass_error/M_S)   

# Create a table for these system parameters that can be fed into the compiled spreadsheet
rows = zip(hip_id, distances_parsec, distances_error_parsec, AU_sep_list, AU_sep_list_error, min_mass, mass_error_list)
header = ['hip_id', 'dist[pc]', 'dist_err[pc]', 'sep[au]', 'sep_err[au]', 'min_mass[msolar]', 'min_mass_err[msolar]']
mass_table = pd.DataFrame(rows, columns=header)
mass_table.to_csv('/Users/Jess/HGCA_survey_paper/minimum_masses_for_koa_companions.csv', index=False)
