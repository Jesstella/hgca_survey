# Necessary Modules 
import pandas as pd
import numpy as np

completed_comparison_file = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')
pmdec_hip = pd.read_csv('/Users/Jess/HGCA_survey_paper/pmdec_hip.csv')

#sig_ra_g 
numerator = completed_comparison_file['pmra_gaia'] - completed_comparison_file['pmra_hg']
denominator = np.sqrt(completed_comparison_file['pmra_gaia_err']**2 + completed_comparison_file['pmra_hg_error']**2)
sigma_ra_g = numerator/denominator

#sig_dec_g 
numerator = completed_comparison_file['pmdec_gaia'] - completed_comparison_file['pmdec_hg']
denominator = np.sqrt(completed_comparison_file['pmdec_gaia_err']**2 + completed_comparison_file['pmdec_hg_error']**2)
sigma_dec_g = numerator/denominator

#sig_ra_hip 
numerator = completed_comparison_file['pmra_hip'] - completed_comparison_file['pmra_hg']
denominator = np.sqrt(completed_comparison_file['pmra_hip_error']**2 + completed_comparison_file['pmra_hg_error']**2)
sigma_ra_hip = numerator/denominator

#sig_dec_hip 
numerator = pmdec_hip - completed_comparison_file['pmdec_hg']
denominator = np.sqrt(completed_comparison_file['pmdec_hip_error']**2 + completed_comparison_file['pmdec_hg_error']**2)
sigma_dec_hip = numerator/denominator

rows = list(zip(sigma_ra_g, sigma_dec_g, sigma_ra_hip, sigma_dec_hip))
header = ['sigma_ra_g', 'sigma_dec_g', 'sigma_ra_hip', 'sigma_dec_hip']
sigma_values = pd.DataFrame(rows, columns=header)
sigma_values.to_csv('/Users/Jess/HGCA_survey_paper/sigma_values.csv', index=False)
