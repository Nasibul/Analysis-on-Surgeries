import setup as s
import records as r
array=[]
for i in range(0,len(s.diag_col)):
    for j in range(0,len(s.denominator_codes_diag)):
        temp=list(r.df.loc[r.df[s.diag_col[i]]==s.denominator_codes_diag[j]].encounter_key)
        array.append(temp)
#The diagnosis columns are searched first for the denominator patients using the diagnosis codes if given.
#The encounter keys for any matches are then appended to an array.
for i in range(0,len(s.PCS_col)):
    for j in range(0,len(s.denominator_codes_PCS)):
        temp=list(r.df.loc[r.df[s.PCS_col[i]]==s.denominator_codes_PCS[j]].encounter_key)
        array.append(temp)
#The procedure columns are then searched for denominator patients using the procedure codes if given.
#The encounter keys for any matches are then appended to aforementioned array.
array.append(list(r.procedures[r.procedures['procedure'].isin(s.denominator_codes_CPT)].encounter_key))
#The procedures column with CPT codes is searched and appended as well.
array2=[element for sub in array for element in sub]
array2.sort()
#The 2d array is turned into a 1d array and sorted.
exclude=[]
for i in range(0,len(s.diag_col)):
    for j in range(0,len(s.exclude_codes_diag)):
        temp=list(r.df.loc[r.df[s.diag_col[i]]==s.exclude_codes_diag[j]].encounter_key)
        exclude.append(temp)

for i in range(0,len(s.PCS_col)):
    for j in range(0,len(s.exclude_codes_PCS)):
        temp=list(r.df.loc[r.df[s.PCS_col[i]]==s.exclude_codes_PCS[j]].encounter_key)
        exclude.append(temp)
exclude.append(list(r.procedures[r.procedures['procedure'].isin(s.exclude_codes_CPT)].encounter_key))
exclude2=[element for sub in exclude for element in sub]
exclude2.sort()
#The same process is repeated but for codes that are to be excluded. In this case, the codes are for malignant polyps.
for i in exclude2:
    if i in array2:
        array2.remove(i)
#the indices for the specified exclude codes are then removed as they do not count towards the violation rate
dummy=[]
for i in array2:
    if i not in dummy:
        dummy.append(i)
array2=dummy
#Duplicates are removed by appending unique values into a dummy array and overwriting the array with it.
denominator=r.df[r.df['encounter_key'].isin(array2)]
denominator
#this is the dataframe containing all patients with benign polyps