import pandas as pd
import sys

from data_parser import parse_data
from convert import main
from parse_user_agent import parse_user_agent

def etl(filename):
    data = parse_data(filename)
    main(data)
    print ('Finished converting IP addresses')
    parse_user_agent(data)
    return data

d = etl(sys.argv[1])


print ('country', len(d['country']))
print ('city', len(d['city']))
print ('user_id', len(d['user_id']))
print ('browser', len(d['browser']))
print ('os', len(d['os']))

df = pd.DataFrame(data={'country': d['country'], 'city': d['city'],
    'user_id':d['user_id'], 'browser': d['browser'], 'os': d['os']})
print (df.head())
print (df['country'].value_counts().head())
print (df['city'].value_counts().head())
print (df.groupby(['user_id'])['browser'].value_counts().sort_values(ascending=False).head())
print (df.groupby(['user_id'])['os'].value_counts().sort_values(ascending=False).head())
