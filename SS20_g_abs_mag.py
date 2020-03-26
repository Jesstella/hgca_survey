# Necessary Modules 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Open file to get data 
bigt = pd.read_csv('/Users/Jess/HGCA_survey_paper/final_spreadsheet.csv')
g_mag = bigt['phot_g_mean_mag']
para = bigt['gaia_parallax']
para_error = bigt['gaia_parallax_err']
flux = bigt['phot_g_mean_flux']
flux_err = bigt['phot_g_mean_flux_error']

# Calculate absolute magnitude using the distance modulus 
distance = 1 / (para * 10**-3)
G_mag = 5 + g_mag - (5 * np.log10(distance))

# Calculate the error on absolute magnitude 
distance_error = para_error / (para**2)
g_mag_error = flux_err/flux

partial_m = g_mag_error 
partial_d = -5/distance

G_mag_error = np.sqrt(partial_m**2 * ((partial_d**2)*(distance_error**2)))

rows = zip(G_mag, G_mag_error)
header = ['G_mag', 'G_mag_error']
mags = pd.DataFrame(rows, columns=header)
mags.to_csv('/Users/Jess/HGCA_survey_paper/absolute_g_mags.csv')
