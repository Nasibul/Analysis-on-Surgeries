import sqlite3
import pandas as pd

def get_records(database_file, med_query, procedures_query):   
    connection = sqlite3.connect(database_file)
    appointments = pd.read_sql_query(med_query, connection)
    procedures = pd.read_sql_query(procedures_query, connection)
    return appointments, procedures
#Selecting all the info as using fstrings would allow for sql injections on top of leaving the possibility for different codes to be requested