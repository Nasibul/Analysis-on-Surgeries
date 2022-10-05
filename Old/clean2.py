import setup as s
import records as r
import clean as c
#The process that was used for the denominator patients will now be used to find the numerator patients.
#However, the denominator df will be used as the violation rate is specifically the denominator patients who have had surgery. 
array_n=[]
for i in range(0,len(s.diag_col)):
    for j in range(0,len(s.numerator_codes_diag)):
        temp=list(c.denominator.loc[c.denominator[s.diag_col[i]]==s.numerator_codes_diag[j]].encounter_key)
        array_n.append(temp)
for i in range(0,len(s.PCS_col)):
    for j in range(0,len(s.numerator_codes_PCS)):
        temp=list(c.denominator.loc[c.denominator[s.PCS_col[i]]==s.numerator_codes_PCS[j]].encounter_key)
        array_n.append(temp)
filter=r.procedures[r.procedures['encounter_key'].isin(c.array2)]
array_n.append(filter[filter['procedure'].isin(s.numerator_codes_CPT)].encounter_key)
array2_n=[element for sub in array_n for element in sub]
array2_n.sort()
dummy=[]
for i in array2_n:
    if i not in dummy:
        dummy.append(i)
array2_n=dummy
numerator=c.denominator[c.denominator['encounter_key'].isin(array2_n)]
numerator