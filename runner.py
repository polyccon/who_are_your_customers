import pandas as pd
import sys
import os

from data_parser import parse_data
from convert_ip import main
from parse_user_agent import parse_user_agent

def usage():
	print("Usage: python " + os.path.basename(__file__) + "path-to-source-data-directory")

def etl():

    if len(sys.argv)>= 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        usage()
        sys.exit(0)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        data = parse_data(filename)
        main(data)
        print ('Finished converting IP addresses')
        parse_user_agent(data)
        return data
    else:
        usage()
        sys.exit(2)


d = etl()
df = pd.DataFrame(data=d)

print ('Top 5 Countries based on number of events:')
print (df['country'].value_counts().head())

print ('Top 5 Cities based on number of events:')
print (df['city'].value_counts().head())

print ('Top 5 Browsers based on number of unique users:')
print (df.groupby('browser')['user_id'].nunique().sort_values(ascending=False).head())

print ('Top 5 OS based on number of unique users:')
print (df.groupby('os')['user_id'].nunique().sort_values(ascending=False).head())
