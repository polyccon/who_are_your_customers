#!/usr/bin/env python

import gzip
import sys

def parse_data(filename):
    print ('Reading input data file')

    with gzip.open(filename, 'rb') as f:
         data = f.read()
         lines = data.decode("utf-8").replace("\n", "\\n").split("\\")
         f.close()

    print ('Finished reading input data file')

    d= { 'date' : [], 'time' : [], 'user_id' : [], 'url' : [], 'IP' : [],
    'ua_string' : []}
    print ('Parsing data started')
    for line in lines:
        line_params = line.split('\t')
        if len(line_params) == 6:
            (date, time, user_id, url, IP, user_agent_string) = line.split('\t')

            d['date'].append(date)
            d['time'].append(time)
            d['user_id'].append(user_id)
            d['url'].append(url)
            d['IP'].append(IP)
            d['ua_string'].append(user_agent_string)

        else:
            continue

    print ('Finished parsing data ')
    return d
