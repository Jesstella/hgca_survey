from astroquery.simbad import Simbad
import pandas as pd
import numpy as np

hip_id = pd.read_csv('/Users/Jess/HGCA_survey_paper/completed_cross_match.csv')['hip_id']
print('There are ' + str(len(hip_id)) + ' stars in this list.')

full_hip_name = []
for i in range(len(hip_id)):
    new_name = 'HIP ' + str(hip_id[i])
    full_hip_name.append(new_name)

customSimbad = Simbad()
customSimbad.add_votable_fields('otypes')
customSimbad.get_votable_fields()

result_table = customSimbad.query_objects(full_hip_name)
object_types = np.array(list(result_table['OTYPES']))

# Qualifying whether each star is a binary by searching object types. 
simbad_companions = []

# These object types are considerd binaries.
substring_1 = '**'
substring_2 = 'SB*'
substring_3 = 'bL*'
substring_4 = 'LXB'
substring_5 = 'Al*'
substring_6 = 'EB*'
substring_7 = '*i*'
substring_8 = 'WU*'

for i in range(len(object_types)):
    
    a = str(object_types[i]).find(substring_1)
    b = str(object_types[i]).find(substring_2)
    c = str(object_types[i]).find(substring_3)
    d = str(object_types[i]).find(substring_4)
    e = str(object_types[i]).find(substring_5)
    f = str(object_types[i]).find(substring_6)
    g = str(object_types[i]).find(substring_7)
    h = str(object_types[i]).find(substring_8)

    # If none of the substrings match in the object row, then the sum will be -8.
    sum_letters = a + b + c + d + e + f + g + h
    if sum_letters > -8:
        simbad_companions.append('YES')
    else:
        simbad_companions.append('NO')
        
# Saving this list to a csv file.
header = ['object_types', 'simbad_companions']
rows = list(zip(object_types, simbad_companions))
rows = pd.DataFrame(rows, columns=header)
rows.to_csv('/Users/Jess/HGCA_survey_paper/simbad_data.csv', index=False)

print('completed')
