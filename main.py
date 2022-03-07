import StudiKasus2
import os
import pandas as pd

case = StudiKasus2.StudiKasus2('localhost', '3306', 'root', '')
df = case.import_csv('username.csv')
print(case.create_db('nameUs3'))
print(case.create_table('nameUs3', 'The_Data', df))
print(case.load_data('nameUs3', 'The_Data'))
print("did it")