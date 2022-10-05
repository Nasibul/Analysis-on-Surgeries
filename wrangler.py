def find_data(df, codes):
    temp=df[df.isin(codes).any(1)] 
    temp.drop_duplicates()
    patients=list(temp["encounter_key"])
    return patients

