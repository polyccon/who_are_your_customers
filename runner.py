import pandas as pd
import sys

from data_parser import parse_data
from convert import main
from parse_user_agent import parse_user_agent

def etl(filename):
    data = parse_data(filename)
    main(data)
    parse_user_agent(data)
    return data

d = etl(sys.argv[1])


print ('country', len(d['country']))
print ('city', len(d['city']))
print ('user_id', len(d['user_id']))
print ('browser', len(d['browser']))
print ('os', len(d['os']))

df = pd.DataFrame(data=d)
print (df.head())

print (df['converted_country'].value_counts().head())
print (df['converted_city'].value_counts().head())
print (df['browser'].groupby(['user_id']).value_counts().head())
print (df['os'].groupby(['user_id']).value_counts().head())
