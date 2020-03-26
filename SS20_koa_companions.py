import pandas as pd 
import numpy as np

# Needs to check stars in this file against the stars in the companion koa file to see how many matches there are.
# NB: They will not all match as there may be multiple companions to a star.
our_stars = pd.read_csv('/Users/Jess/HGCA_survey_paper/koa_file_crossmatch.csv')
print('There are ' + str(len(our_stars)) + ' KOA observations that contain a HGCA star.')
print('There are ' + str(len(set(our_stars['hip_id']))) + ' unique stars in our sample.')
print('There are ' + str(len(our_stars['koa_file']) - len(set(our_stars['koa_file']))) + ' KOA observations containing multiple HGCA stars.')

stars_with_comps = pd.read_csv('/Users/Jess/HGCA_survey_paper/new_tables/multitable_hgca_edited.csv', delimiter='&') 
print('There are ' + str(len(stars_with_comps)) + ' observations of companions, over ' + str(len(set(stars_with_comps['Name']))) + ' systems.')
print('This means that ' + str(len(stars_with_comps) - len(set(stars_with_comps['Name']))) + ' stars have multiple companions.')

# Pulling the file names for the stars in our sample and formatting them.
file_id = list(set(our_stars['koa_file']))

# Pulling the file names for the stars in Adam's sample.
comp_stars = list(stars_with_comps['file'])

# Determine which of these file names overlap by comparing the lists of unique file names.
# If the file name appears in both lists, then it has a companion identified in KOA. 
list_1 = file_id
list_2 = comp_stars

# Create list for file IDs and for indexes of these stars 
new_list = []
index_list = []

# Cycle through each of the stars in KOA
for i in range(len(list_1)):
    
    # If the star in KOA is also in te comps file
    if list_1[i] in list_2:
        
        # Then add the file name to the new list and add the index of the filename to a new list. 
        new_list.append(list_1[i])
        index_list.append(int(i))
        
    else: 
        continue

print('There are ' + str(len(new_list)) + ' stars in our sample with companions.')

# Using the index of the file names to determine the corresponding HIP ID. 
hip_with_koa_comp = []

for i in index_list:
    hip_with_koa_comp.append(our_stars['hip_id'][i])

print('There are ' + str(len(set(hip_with_koa_comp))) + ' unique stars that have companions.')

companion_file_index = []

for i in new_list:
    ind = comp_stars.index(i)
    companion_file_index.append(ind)

file_name = []
sep = []
sep_err = []
pa = []
pa_err = []
del_mag = []
del_mag_err = []

for i in companion_file_index: 
    file_name.append(stars_with_comps['file'][i])
    sep.append(stars_with_comps['sep'][i])
    sep_err.append(stars_with_comps['sep_err'][i])
    pa.append(stars_with_comps['pa'][i])
    pa_err.append(stars_with_comps['pa_err'][i])
    del_mag.append(stars_with_comps['del_mag'][i])
    del_mag_err.append(stars_with_comps['del_mag_err'][i])

# Create a file with the companion data 
rows = zip(hip_with_koa_comp, file_name, sep, sep_err, pa, pa_err, del_mag, del_mag_err)
header = ['hip_id', 'file', 'sep', 'sep_err', 'pa', 'pa_err', 'del_mag', 'del_mag_err']
koa_comps_file = pd.DataFrame(rows, columns=header)
koa_comps_file.to_csv('/Users/Jess/HGCA_survey_paper/koa_companions_with_values.csv', index=False)

# Create a column for the compiled file, showing which stars have companions. 
cross_match_file = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')
print('There are ' + str(len(cross_match_file)) + ' entries in the cross match.')

list_1 = cross_match_file['hip_id']
list_2 = set(hip_with_koa_comp)

new_column = []

# Cycle through each of the stars in KOA
for i in range(len(list_1)):
    
    # If the star in KOA is also in te comps file
    if list_1[i] in list_2:
        new_column.append(1)
    else: 
        new_column.append(0)

koas = pd.DataFrame(new_column, columns=['koa_comps'])
koas.to_csv('/Users/Jess/HGCA_survey_paper/koas.csv', index=False)
