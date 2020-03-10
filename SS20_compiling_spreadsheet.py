# Necessary Modules 
from pandas import read_csv as rc
import pandas as pd

# Opening all the files created 
path = '/Users/Jess/HGCA_survey_paper/'

bigt = rc(path + 'completed_cross_match.csv')
wds = rc(path + 'wds_values.csv')
simbad = rc(path + 'simbad_data.csv')
gaia = rc(path + 'gaia_companions.csv')
koa = rc(path + 'koas.csv')
accels = rc(path + 'accelerations.csv')
sigma = rc(path + 'sigma_values.csv')
pmdechip = rc(path + 'pmdec_hip.csv') 
interesting = rc(path + 'interesting.csv')

print('The amount of total HGCA stars to compile is: ' + str(len(bigt)))
print('There are: ' + str(len(koa)) + ' matches in KOA.')
print('There are: ' + str(len(simbad)) + ' matches in SIMBAD.')
print('There are: ' + str(len(gaia))+ ' matches in Gaia.')
print('I have worked out: ' + str(len(accels)) + ' acceleration values.')
print('I have worked out: ' + str(len(sigma)) + ' sigma values.')
print('I have worked out: ' + str(len(pmdechip)) + ' pmdec_hip values.')
print('There are ' + str(len(interesting)) + ' systems in the interesting file.')

# Collecting, in order, the data for each column in the spreadsheet.
# Also allocates a column name in the header. 
header = []

interesting = list(interesting['interesting'])
header.append('interesting')

hip_id = list(bigt['hip_id'])
header.append('hip_id')

wds_names = list(wds['wds_names'])
header.append('wds_names')

gaia_id = list(bigt['gaia_id'])
header.append('gaia_id')

simbad_ot = list(simbad['object_types'])
header.append('sim_obs')

simbad_comps = list(simbad['simbad_companions'])
header.append('sim_comp')

wds_comps = list(wds['wds_companions'])
header.append('wds_comps')

gaia_comps = list(gaia['gaia_comps'])
header.append('gaia_comps')

koas = list(koa['koa_comps'])
header.append('koa')

acc = list(accels['acceleration'])
header.append('accel')

sig_ra_g = list(sigma['sigma_ra_g'])
header.append('sigma_ra_g')

sig_dec_g = list(sigma['sigma_dec_g'])
header.append('sig_dec_g')

sig_ra_hip = list(sigma['sigma_ra_hip'])
header.append('sig_ra_hip')

sig_dec_hip = list(sigma['sigma_dec_hip'])
header.append('sig_dec_hip')

ruwe = list(bigt['ruwe'])
header.append('ruwe')

prim_mag = list(wds['mag1'])
header.append('prim_mag')

sec_mag = list(wds['mag2'])
header.append('sec_mag')

mag_diff = list(wds['mag_diff'])
header.append('mag_diff')

obs1 = list(wds['obs1'])
header.append('obs1')

obs2 = list(wds['obs2'])
header.append('obs2')

sep1 = list(wds['sep1'])
header.append('sep1')

sep2 = list(wds['sep2'])
header.append('sep2')

pa1 = list(wds['pa1'])
header.append('pa1')

pa2 = list(wds['pa2'])
header.append('pa2')

g_ra = list(bigt['ra'])
header.append('ra')

g_ra_err = list(bigt['ra_error'])
header.append('ra_error')

g_dec = list(bigt['dec'])
header.append('dec')

g_dec_err = list(bigt['dec_error'])
header.append('dec_error')

rv = list(bigt['rad_vel'])
header.append('rad_vel')

rv_err = list(bigt['rad_vel_err'])
header.append('rad_vel_err')

rv_nb_transits = list(bigt['rv_nb_transits'])
header.append('rv_nb_transits')

rv_template_teff = list(bigt['rv_template_teff'])
header.append('rv_template_teff')

rv_template_logg = list(bigt['rv_template_logg'])
header.append('rv_template_logg')

rv_template_fe_h = list(bigt['rv_template_fe_h'])
header.append('rv_template_fe_h')

gaia_parallax = list(bigt['gaia_parallax'])
header.append('gaia_parallax')

gaia_parallax_err = list(bigt['gaia_parallax_err'])
header.append('gaia_parallax_err')

parallax_over_error = list(bigt['parallax_over_error'])
header.append('parallax_over_error')

pmra_gaia = list(bigt['pmra_gaia'])
header.append('pmra_gaia')

pmdec_gaia = list(bigt['pmdec_gaia'])
header.append('pmdec_gaia')

pmra_gaia_err = list(bigt['pmra_gaia_err'])
header.append('pmra_gaia_err')

pmdec_gaia_err = list(bigt['pmdec_gaia_err'])
header.append('pmdec_gaia_err')

pmra_pmdec_gaia = list(bigt['pmra_pmdec_gaia'])
header.append('pmra_pmdec_gaia')

pmra_hg = list(bigt['pmra_hg'])
header.append('pmra_hg')

pmdec_hg = list(bigt['pmdec_hg'])
header.append('pmdec_hg')

pmra_hg_error = list(bigt['pmra_hg_error'])
header.append('pmra_hg_error')

pmdec_hg_error = list(bigt['pmdec_hg_error'])
header.append('pmdec_hg_error')

pmra_hip = list(bigt['pmra_hip'])
header.append('pmra_hip')

pmra_hip_error = list(bigt['pmra_hip_error'])
header.append('pmra_hip_error')

pmdec_hip = list(pmdechip['pmdec_hip'])
header.append('pm_dec_hip')

pmdec_hip_error = list(bigt['pmdec_hip_error'])
header.append('pmdec_hip_error')

pmra_pmdec_hip = list(bigt['pmra_pmdec_hip'])
header.append('pmra_pmdec_hip')

epoch_ra_gaia = list(bigt['epoch_ra_gaia'])
header.append('epoch_ra_gaia')

epoch_dec_gaia = list(bigt['epoch_dec_gaia'])
header.append('epoch_dec_gaia')

epoch_ra_hip = list(bigt['epoch_ra_hip'])
header.append('epoch_ra_hip')

epoch_dec_hip = list(bigt['epoch_dec_hip'])
header.append('epoch_dec_hip')

ref_epoch = list(bigt['ref_epoch'])
header.append('ref_epoch')

crosscal_pmra_hip = list(bigt['crosscal_pmra_hip'])
header.append('crosscal_pmra_hip')

crosscal_pmdec_hip = list(bigt['crosscal_pmdec_hip'])
header.append('crosscal_pmdec_hip')

crosscal_pmra_hg = list(bigt['crosscal_pmra_hg'])
header.append('crosscal_pmra_hg')

crosscal_pmdec_hg = list(bigt['crosscal_pmdec_hg'])
header.append('crosscal_pmdec_hg')

nonlinear_dpmra = list(bigt['nonlinear_dpmra'])
header.append('nonlinear_dpmra')

nonlinear_dpmdec = list(bigt['nonlinear_dpmdec'])
header.append('nonlinear_dpmdec')

ra_dec_corr = list(bigt['ra_dec_corr'])
header.append('ra_dec_corr')

ra_parallax_corr = list(bigt['ra_parallax_corr'])
header.append('ra_parallax_corr')

dec_parallax_corr = list(bigt['dec_parallax_corr'])
header.append('dec_parallax_corr')

ra_pmra_corr = list(bigt['ra_pmra_corr'])
header.append('ra_pmra_corr')

ra_pmdec_corr = list(bigt['ra_pmdec_corr'])
header.append('ra_pmdec_corr')

dec_pmra_corr = list(bigt['dec_pmra_corr'])
header.append('dec_pmra_corr')

dec_pmdec_corr = list(bigt['dec_pmdec_corr'])
header.append('dec_pmdec_corr')

parallax_pmra_corr = list(bigt['parallax_pmra_corr'])
header.append('parallax_pmra_corr')

parallax_pmdec_corr = list(bigt['parallax_pmdec_corr'])
header.append('parallax_pmdec_corr')

pmra_pmdec_corr = list(bigt['pmra_pmdec_corr'])
header.append('pmra_pmdec_corr')

astrometric_n_obs_al = list(bigt['astrometric_n_obs_al'])
header.append('astrometric_n_obs_al')

astrometric_n_obs_ac = list(bigt['astrometric_n_obs_ac'])
header.append('astrometric_n_obs_ac')

astrometric_n_good_obs_al = list(bigt['astrometric_n_good_obs_al'])
header.append('astrometric_n_good_obs_al')

astrometric_n_bad_obs_al = list(bigt['astrometric_n_bad_obs_al'])
header.append('astrometric_n_bad_obs_al')

astrometric_gof_al = list(bigt['astrometric_gof_al'])
header.append('astrometric_gof_al')

astrometric_chi2_al = list(bigt['astrometric_chi2_al'])
header.append('astrometric_chi2_al')

astrometric_excess_noise = list(bigt['astrometric_excess_noise'])
header.append('astrometric_excess_noise')

astrometric_excess_noise_sig = list(bigt['astrometric_excess_noise_sig'])
header.append('astrometric_excess_noise_sig')

astrometric_params_solved = list(bigt['astrometric_params_solved'])
header.append('astrometric_params_solved')

astrometric_primary_flag = list(bigt['astrometric_primary_flag'])
header.append('astrometric_primary_flag')

astrometric_weight_al = list(bigt['astrometric_weight_al'])
header.append('astrometric_weight_al')

astrometric_pseudo_colour = list(bigt['astrometric_pseudo_colour'])
header.append('astrometric_pseudo_colour')

astrometric_pseudo_colour_error = list(bigt['astrometric_pseudo_colour_error'])
header.append('astrometric_pseudo_colour_error')

mean_varpi_factor_al = list(bigt['mean_varpi_factor_al'])
header.append('mean_varpi_factor_al')

astrometric_matched_observations = list(bigt['astrometric_matched_observations'])
header.append('astrometric_matched_observations')

visibility_periods_used = list(bigt['visibility_periods_used'])
header.append('visibiity_periods_used')

astrometric_sigma5d_max = list(bigt['astrometric_sigma5d_max'])
header.append('astrometric_sigma5d_max')

frame_rotator_object_type = list(bigt['frame_rotator_object_type'])
header.append('frame_rotator_object_type')

matched_observations = list(bigt['matched_observations'])
header.append('matched_observations')

duplicated_source = list(bigt['duplicated_source'])
header.append('duplicated_sources')

phot_g_n_obs = list(bigt['phot_g_n_obs'])
header.append('phot_g_n_obs')

phot_g_mean_flux = list(bigt['phot_g_mean_flux'])
header.append('phot_g_mean_flux')

phot_g_mean_flux_error = list(bigt['phot_g_mean_flux_error'])
header.append('phot_g_mean_flux_error')

phot_g_mean_flux_over_error = list(bigt['phot_g_mean_flux_over_error'])
header.append('phot_g_mean_flux_over_error')

phot_g_mean_mag = list(bigt['phot_g_mean_mag'])
header.append('phot_g_mean_mag')

phot_bp_n_obs = list(bigt['phot_bp_n_obs'])
header.append('phot_bp_n_obs')

phot_bp_mean_flux = list(bigt['phot_bp_mean_flux'])
header.append('phot_bp_mean_flux')

phot_bp_mean_flux_error = list(bigt['phot_bp_mean_flux_error'])
header.append('phot_bp_mean_flux_error')

phot_bp_mean_flux_over_error = list(bigt['phot_bp_mean_flux_over_error'])
header.append('phot_bp_mean_flux_over_error')

phot_bp_mean_mag = list(bigt['phot_bp_mean_mag'])
header.append('phot_bp_mean_mag')

phot_rp_n_obs = list(bigt['phot_rp_n_obs'])
header.append('phot_rp_n_obs')

phot_rp_mean_flux = list(bigt['phot_rp_mean_flux'])
header.append('phot_rp_mean_flux')

phot_rp_mean_flux_error = list(bigt['phot_rp_mean_flux_error'])
header.append('phot_rp_mean_flux_error')

phot_rp_mean_flux_over_error = list(bigt['phot_rp_mean_flux_over_error'])
header.append('phot_rp_mean_flux_over_error')

phot_rp_mean_mag = list(bigt['phot_rp_mean_mag'])
header.append('phot_rp_mean_mag')

phot_bp_rp_excess_factor = list(bigt['phot_bp_rp_excess_factor'])
header.append('phot_bp_rp_excess_factor')

phot_proc_mode = list(bigt['phot_proc_mode'])
header.append('phot_proc_mode')

bp_rp = list(bigt['bp_rp'])
header.append('bp_rp')

bp_g = list(bigt['bp_g'])
header.append('bp_g')

g_rp = list(bigt['g_rp'])
header.append('g_rp')

phot_variable_flag = list(bigt['phot_variable_flag'])
header.append('phot_variable_flag')

#abs g mag and abs g mag error go here 

l = list(bigt['l'])
header.append('l')

b = list(bigt['b'])
header.append('b')

ecl_lon = list(bigt['ecl_lon'])
header.append('ecl_lon')

ecl_lat = list(bigt['ecl_lat'])
header.append('ecl_lat')

priam_flags = list(bigt['priam_flags'])
header.append('priam_flags')

teff_val = list(bigt['teff_val'])
header.append('teff_val')

teff_percentile_lower = list(bigt['teff_percentile_lower'])
header.append('teff_percentile_lower')

teff_percentile_upper = list(bigt['teff_percentile_upper'])
header.append('teff_percentile_upper')

a_g_val = list(bigt['a_g_val'])
header.append('a_g_val')

a_g_percentile_lower = list(bigt['a_g_percentile_lower'])
header.append('a_g_percentile_lower')

a_g_percentile_upper = list(bigt['a_g_percentile_upper'])
header.append('a_g_percentile_upper')

e_bp_min_rp_val = list(bigt['e_bp_min_rp_val'])
header.append('e_bp_min_rp_val')

e_bp_min_rp_percentile_lower = list(bigt['e_bp_min_rp_percentile_lower'])
header.append('e_bp_min_rp_percentile_lower')

e_bp_min_rp_percentile_upper = list(bigt['e_bp_min_rp_percentile_upper'])
header.append('e_bp_min_rp_percentile_upper')

flame_flags = list(bigt['flame_flags'])
header.append('flame_flags')

radius_val = list(bigt['radius_val'])
header.append('radius_val')

radius_percentile_lower = list(bigt['radius_percentile_lower'])
header.append('radius_percentile_lower')

radius_percentile_upper = list(bigt['radius_percentile_upper'])
header.append('radius_percentile_upper')

lum_val = list(bigt['lum_val'])
header.append('lum_val')

lum_percentile_lower = list(bigt['lum_percentile_lower'])
header.append('lum_percentile_lower')

lum_percentile_upper = list(bigt['lum_percentile_upper'])
header.append('lum_percentile_upper')

datalink_url = list(bigt['datalink_url'])
header.append('datalink_url')

epoch_photometry_url = list(bigt['epoch_photometry_url'])
header.append('epoch_photometry_url')

Proxy = list(bigt['Proxy'])
header.append('Proxy')

RAhms = list(bigt['RAhms'])
header.append('RAhms')

DEdms = list(bigt['DEdms'])
header.append('DEdms')

Vmag = list(bigt['Vmag'])
header.append('Vmag')

VarFlag = list(bigt['VarFlag'])
header.append('VarFlag')

r_Vmag = list(bigt['r_Vmag'])
header.append('r_Vmag')

RAICRS = list(bigt['RAICRS'])
header.append('RAICRS')

DEICRS = list(bigt['DEICRS'])
header.append('DEICRS')

AstroRef = list(bigt['AstroRef'])
header.append('AstroRef')

Plx = list(bigt['Plx'])
header.append('Plx')

pmRA = list(bigt['pmRA'])
header.append('pmRA')

pmDE = list(bigt['pmDE'])
header.append('pmDE')

e_RAICRS = list(bigt['e_RAICRS'])
header.append('e_RAICRS')

e_DEICRS = list(bigt['e_DEICRS'])
header.append('e_DEICRS')

e_Plx = list(bigt['e_Plx'])
header.append('e_Plx')

e_pmRA = list(bigt['e_pmRA'])
header.append('e_pmRA')

e_pmDE = list(bigt['e_pmDE'])
header.append('e_pmDE')

DE_RA = list(bigt['DE:RA'])
header.append('DE_RA')

Plx_RA = list(bigt['Plx:RA'])
header.append('Plx_RA')

Plx_DE = list(bigt['Plx:DE'])
header.append('Plx_DE')

pmRA_RA = list(bigt['pmRA:RA'])
header.append('pmRA_RA')

pmRA_DE = list(bigt['pmRA:DE'])
header.append('pmRA_DE')

pmRA_Plx = list(bigt['pmRA:Plx'])
header.append('pmRA_Plx')

pmDE_RA = list(bigt['pmDE:RA'])
header.append('pmDE_RA')

pmDE_DE = list(bigt['pmDE:DE'])
header.append('pmDE_DE')

pmDE_Plx = list(bigt['pmDE:Plx'])
header.append('pmDE_Plx')

pmDE_pmRA = list(bigt['pmDE:pmRA'])
header.append('pmDE_pmRA')

F1 = list(bigt['F1'])
header.append('F1')

F2 = list(bigt['F2'])
header.append('F2')

BTmag = list(bigt['BTmag'])
header.append('BTmag')

e_BTmag = list(bigt['e_BTmag'])
header.append('e_BTmag')

VTmag = list(bigt['VTmag'])
header.append('VTmag')

e_VTmag = list(bigt['e_VTmag'])
header.append('e_VTmag')

m_BTmag = list(bigt['m_BTmag'])
header.append('m_BTmag')

B_V = list(bigt['B-V'])
header.append('B_V')

e_B_V = list(bigt['e_B-V'])
header.append('e_B_V')

r_B_V = list(bigt['r_B-V'])
header.append('r_B_V')

V_I = list(bigt['V-I'])
header.append('V_I')

e_V_I = list(bigt['e_V-I'])
header.append('e_V_I')

r_V_I = list(bigt['r_V-I'])
header.append('r_V_I')

CombMag = list(bigt['CombMag'])
header.append('CombMag')

Hpmag = list(bigt['Hpmag'])
header.append('Hpmag')

e_Hpmag = list(bigt['e_Hpmag'])
header.append('e_Hpmag')

Hpscat = list(bigt['Hpscat'])
header.append('Hpscat')

o_Hpmag = list(bigt['o_Hpmag'])
header.append('o_Hpmag')

m_Hpmag = list(bigt['m_Hpmag'])
header.append('m_Hpmag')

Hpmax = list(bigt['Hpmax'])
header.append('Hpmag')

HPmin = list(bigt['HPmin'])
header.append('HPmin')

Period = list(bigt['Period'])
header.append('Period')

HvarType = list(bigt['HvarType'])
header.append('HvarType')

moreVar = list(bigt['moreVar'])
header.append('moreVar')

morePhoto = list(bigt['morePhoto'])
header.append('morePhoto')

CCDM = list(bigt['CCDM'])
header.append('CCDM')

n_CCDM = list(bigt['n_CCDM'])
header.append('n_CCDM')

Nsys = list(bigt['Nsys'])
header.append('Nsys')

Ncomp = list(bigt['Ncomp'])
header.append('Ncomp')

MultFlag = list(bigt['MultFlag'])
header.append('MultFlag')

Source = list(bigt['Source'])
header.append('Source')

Qual = list(bigt['Qual'])
header.append('Qual')

m_HIP = list(bigt['m_HIP'])
header.append('m_HIP')

theta = list(bigt['theta'])
header.append('theta')

rho = list(bigt['rho'])
header.append('rho')

e_rho = list(bigt['e_rho'])
header.append('e_rho')

dHp = list(bigt['dHp'])
header.append('dHp')

e_dHp = list(bigt['e_dHp'])
header.append('e_dHp')

Survey = list(bigt['Survey'])
header.append('Survey')

Chart = list(bigt['Chart'])
header.append('Chart')

Notes = list(bigt['Notes'])
header.append('Notes')

HD = list(bigt['HD'])
header.append('HD')

BD = list(bigt['BD'])
header.append('BD')

CoD = list(bigt['CoD'])
header.append('CoD')

CPD = list(bigt['CPD'])
header.append('CPD')

V_I_red = list(bigt['(V-I)red'])
header.append('V_I_red')

SpType = list(bigt['SpType'])
header.append('SpType')

r_SpType = list(bigt['r_SpType'])
header.append('r_SpType')

HIPep = list(bigt['HIPep'])
header.append('HIPep')

Erratum = list(bigt['Erratum'])
header.append('Erratum')

_RA_icrs = list(bigt['_RA.icrs'])
header.append('_RA_icrs')

_DE_icrs = list(bigt['_DE.icrs'])
header.append('_DE_icrs')

lee_n_HIP = list(bigt['lee_n_HIP'])
header.append('lee_n_HIP')

lee_Sn = list(bigt['lee_Sn'])
header.append('lee_Sn')

lee_So = list(bigt['lee_So'])
header.append('lee_So')

lee_Nc = list(bigt['lee_Nc'])
header.append('lee_Nc')

lee_RArad = list(bigt['lee_RArad'])
header.append('lee_RArad')

lee_e_RArad = list(bigt['lee_e_RArad'])
header.append('lee_e_RArad')

lee_DErad = list(bigt['lee_DErad'])
header.append('lee_DErad')

lee_e_DErad = list(bigt['lee_e_DErad'])
header.append('lee_e_DErad')

lee_Plx = list(bigt['lee_Plx'])
header.append('lee_Plx')

lee_e_Plx = list(bigt['lee_e_Plx'])
header.append('lee_e_Plx')

lee_pmRA = list(bigt['lee_pmRA'])
header.append('lee_pmRA')

lee_e_pmRA = list(bigt['lee_e_pmRA'])
header.append('lee_e_pmRA')

lee_pmDE = list(bigt['lee_pmDE'])
header.append('lee_pmDE')

lee_e_pmDE = list(bigt['lee_e_pmDE'])
header.append('lee_e_pmDE')

lee_Ntr = list(bigt['lee_Ntr'])
header.append('lee_Ntr')

lee_F2 = list(bigt['lee_F2'])
header.append('lee_F2')

lee_F1 = list(bigt['lee_F1'])
header.append('lee_F1')

lee_var = list(bigt['lee_var'])
header.append('lee_var')

lee_Hpmag = list(bigt['lee_Hpmag'])
header.append('lee_Hpmag')

lee_e_Hpmag = list(bigt['lee_e_Hpmag'])
header.append('lee_e_Hpmag')

lee_sHp = list(bigt['lee_sHp'])
header.append('lee_sHp')

lee_VA = list(bigt['lee_VA'])
header.append('lee_VA')

lee_B_V = list(bigt['lee_B_V'])
header.append('lee_B_V')

lee_e_B_V = list(bigt['lee_e_B_V'])
header.append('lee_e_B_V')

lee_V_I = list(bigt['lee_V_I'])
header.append('lee_V_I')

lee_HIP1 = list(bigt['lee_HIP1'])
header.append('lee_HIP1')

lee_Phot = list(bigt['lee_Phot'])
header.append('lee_phot')

# Collect all columns together
all_cols = zip(interesting, hip_id, wds_names, gaia_id, simbad_ot, simbad_comps, wds_comps, gaia_comps, koas, acc, sig_ra_g, sig_dec_g, sig_ra_hip, sig_dec_hip, ruwe, prim_mag, sec_mag, mag_diff, obs1, obs2, sep1, sep2, pa1, pa2, g_ra, g_ra_err, g_dec, g_dec_err, rv, rv_err, rv_nb_transits, rv_template_teff, rv_template_logg, rv_template_fe_h, gaia_parallax, gaia_parallax_err, parallax_over_error, pmra_gaia, pmdec_gaia, pmra_gaia_err, pmdec_gaia_err, pmra_pmdec_gaia, pmra_hg, pmdec_hg, pmra_hg_error, pmdec_hg_error, pmra_hip, pmra_hip_error, pmdec_hip, pmdec_hip_error, pmra_pmdec_hip, epoch_ra_gaia, epoch_dec_gaia, epoch_ra_hip, epoch_dec_hip, ref_epoch, crosscal_pmra_hip, crosscal_pmdec_hip, crosscal_pmra_hg, crosscal_pmdec_hg, nonlinear_dpmra, nonlinear_dpmdec, ra_dec_corr, ra_parallax_corr, dec_parallax_corr, ra_pmra_corr, ra_pmdec_corr, dec_pmra_corr, dec_pmdec_corr, parallax_pmra_corr, parallax_pmdec_corr, pmra_pmdec_corr, astrometric_n_obs_al, astrometric_n_obs_ac, astrometric_n_good_obs_al, astrometric_n_bad_obs_al, astrometric_gof_al, astrometric_chi2_al, astrometric_excess_noise, astrometric_excess_noise_sig, astrometric_params_solved, astrometric_primary_flag, astrometric_weight_al, astrometric_pseudo_colour, astrometric_pseudo_colour_error, mean_varpi_factor_al, astrometric_matched_observations, visibility_periods_used, astrometric_sigma5d_max, frame_rotator_object_type, matched_observations, duplicated_source, phot_g_n_obs, phot_g_mean_flux, phot_g_mean_flux_error, phot_g_mean_flux_over_error, phot_g_mean_mag, phot_bp_n_obs, phot_bp_mean_flux, phot_bp_mean_flux, phot_bp_mean_flux_error, phot_bp_mean_flux_over_error, phot_rp_n_obs, phot_rp_mean_flux, phot_rp_mean_flux_error, phot_rp_mean_flux_over_error, phot_rp_mean_mag, phot_bp_rp_excess_factor, phot_proc_mode, bp_rp, bp_g, g_rp, phot_variable_flag, l, b, ecl_lon, ecl_lat, priam_flags, teff_val, teff_percentile_lower, teff_percentile_upper, a_g_val, a_g_percentile_lower, a_g_percentile_upper, e_bp_min_rp_val, e_bp_min_rp_percentile_lower, e_bp_min_rp_percentile_upper, flame_flags, radius_val, radius_percentile_lower, radius_percentile_upper, lum_val, lum_percentile_lower, lum_percentile_upper, datalink_url, epoch_photometry_url, Proxy, RAhms, DEdms, Vmag, VarFlag, r_Vmag, RAICRS, DEICRS, AstroRef, Plx, pmRA, pmDE, e_RAICRS, e_DEICRS, e_Plx, e_pmRA, e_pmDE, DE_RA, Plx_RA, Plx_DE, pmRA_RA, pmRA_DE, pmRA_Plx, pmDE_RA, pmDE_DE, pmDE_Plx, pmDE_pmRA, F1, F2, BTmag, e_BTmag, VTmag, e_VTmag, m_BTmag, B_V, e_B_V, r_B_V, V_I, e_V_I, r_V_I, CombMag, Hpmag, e_Hpmag, Hpscat, o_Hpmag, m_Hpmag, Hpmax, HPmin, Period, HvarType, moreVar, morePhoto, CCDM, n_CCDM, Nsys, Ncomp, MultFlag, Source, Qual, m_HIP, theta, rho, e_rho, dHp, e_dHp, Survey, Chart, Notes, HD, BD, CoD, CPD, V_I_red, SpType, r_SpType, HIPep, Erratum, _RA_icrs, _DE_icrs, lee_n_HIP, lee_Sn, lee_So, lee_Nc, lee_RArad, lee_e_RArad, lee_DErad, lee_e_DErad, lee_Plx, lee_e_Plx, lee_pmRA, lee_e_pmRA, lee_pmDE, lee_e_pmDE, lee_Ntr, lee_F2, lee_F1, lee_var, lee_Hpmag, lee_e_Hpmag, lee_sHp, lee_VA, lee_B_V, lee_e_B_V, lee_V_I, lee_HIP1, lee_Phot)

# Create the final spreadsheet and save it
final_spreadsheet = pd.DataFrame(all_cols, columns=header)
final_spreadsheet.to_csv(path + 'final_spreadsheet.csv', index=False)
