import sqlite3
import pandas as pd
connection=sqlite3.connect('claims.db')
df=pd.read_sql_query("SELECT * FROM medical_headers",connection)
procedures=pd.read_sql_query("SELECT * FROM medical_service_lines",connection)
#Selecting all the info as using fstrings would allow for sql injections on top of leaving the possibility for different codes to be requested