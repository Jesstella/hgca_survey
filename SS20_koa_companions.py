import pandas as pd 
import numpy as np

# Needs to check stars in this file against the stars in the companion koa file to see how many matches there are.
# NB: They will not all match as there may be multiple companions to a star.
our_stars = pd.read_csv('/Users/Jess/HGCA_survey_paper/new_keck_stars_edited.csv')
print('There are ' + str(len(our_stars)) + ' observations in KOA.')

stars_with_comps = pd.read_csv('/Users/Jess/Downloads/new_new_adam.csv') 
print(str(len(stars_with_comps)) + ' of these have companions.')

# Determine the unique file ID for each of the KOA stars. 
file_names = our_stars['File']
file_id = []

# Cycle through each file and cut down the string to create the list of unique file identifiers
for i in file_names:
    new_file_id = i[51:-10]
    file_id.append(new_file_id)
    
print('There are ' + str(len(file_id)) + ' entries in the whole KOA observations file.')
print(file_id[0:5])

# Now do the same for the stars with companions.
comp_stars = stars_with_comps['file']
file_id_comps = []

for i in comp_stars:
    new_file_id = i[3:]
    file_id_comps.append(new_file_id)
    
print('There are ' + str(len(file_id_comps)) + ' entries in the companion file.')
print(file_id_comps[0:5])

# Creat a set to remove doubles, where there are multiple stars.
file_id_comps_set = set(file_id_comps)

# Determine which of these file names overlap by comparing the lists of unique file names.
# If the file name appears in both lists, then it has a companion identified in KOA. 
list_1 = file_id 
list_2 = file_id_comps

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

print('There are ' + str(len(new_list)) + ' entries in the new file. This should be the same as ' + str(len(file_id_comps_set)) + '.')

# Create lists of RA and Dec 
ra_list = []
dec_list = []

for i in index_list:
    ra = our_stars['ra'][i]
    ra_list.append(ra)
    dec = our_stars['dec'][i]
    dec_list.append(dec)

# Now need to compare the RA and Dec in our sample with the ra and dec of the COMPANION stars in the KOA sample.
# The initial cross-match is necessary because the RA and Dec do not appear in the companion file
cross_match_file = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')
print('There are ' + str(len(cross_match_file)) + ' entries in the cross match.')

check_list = []

for (i, j) in zip(ra_list, dec_list):
    cut_cross_match = cross_match_file[((cross_match_file['ra'] >= i - 0.001) & (cross_match_file['dec'] >= j - 0.001) & (cross_match_file['ra'] <= i + 0.001) & (cross_match_file['dec'] <= j + 0.001))]
    check_list.append(cut_cross_match['hip_id'])

cut_cross_match = pd.concat(check_list)    

# Save new dataframe of stars which have companions in KOA
cut_cross_match.to_csv('/Users/Jess/HGCA_survey_paper/koa_hip_with_comps.csv')

# Need to make a column of stars with companions in KOA, so open new file and pull HIP IDs.
koa_comps = list(pd.read_csv('/Users/Jess/HGCA_survey_paper/koa_hip_with_comps.csv')['hip_id'])
our_names = list(cross_match_file['hip_id'])

list_1 = our_names
list_2 = koa_comps

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
