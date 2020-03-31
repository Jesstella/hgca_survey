import pandas as pd 
import numpy as np
import ads
from itertools import zip_longest
import collections

comps = pd.read_csv('/Users/Jess/HGCA_survey_paper/koa_wds_comps.csv')
hip_id = comps['hip_id']

hip_names_ads = []
for i in hip_id:
    name = 'full:"hip '  + str(i) + '"'
    hip_names_ads.append(name)

rows = []

for i in hip_names_ads:
    row = []
    papers = ads.SearchQuery(q=i)

    paper_list = []
    number_of_papers = []
    
    for paper in papers:
        number_of_papers.append(1)
        row.append(str(paper.first_author) + ', ' + str(paper.year))
        row.append(paper.bibcode)
    
    if sum(number_of_papers) == 0:
        row.append('No Papers')
        rows.append(row)
    else: 
        rows.append(row)

rows_2 = list(zip_longest(*rows))
ads_search = pd.DataFrame(rows_2, columns=hip_id)

ads_search.to_csv('/Users/Jess/HGCA_survey_paper/ads_search.csv', index=False)

multiple = pd.read_csv('/Users/Jess/HGCA_survey_paper/ads_search.csv')
multi = multiple.values.tolist()

flat_list = [item for sublist in multi for item in sublist]
flat_list = flat_list[58:]
cleanedList = [x for x in flat_list if str(x) != 'nan']

dictionary = collections.Counter(cleanedList)
if 'No Papers' in dictionary:
    del dictionary['No Papers']

keys_list = list(dictionary)
values = dictionary.values()
values_list = list(values)

papers_with_multiples = []
how_many_papers = []

for i in range(len(keys_list)):
    if values_list[i] == 1:
        continue
    else: 
        if keys_list[i][0] == str(1):
            continue
        elif keys_list[i][0] == str(2):
            continue
        else:    
            papers_with_multiples.append(keys_list[i])
            how_many_papers.append(values_list[i])

multi_rows = zip(papers_with_multiples, how_many_papers)
header = ['paper', 'repeat']

multi_rows = pd.DataFrame(multi_rows, columns=header)
multi_rows.to_csv('/Users/Jess/HGCA_survey_paper/multiple_references.csv', index=False)
