#!/usr/bin/env python

import gzip
import sys

def parse_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = f.read()
        lines = data.decode("utf-8").replace("\n", "\\n").split("\\")
        f.close()

        d= { 'date' : [], 'time' : [], 'user_id' : [], 'url' : [], 'IP' : [],
    'ua_string' : [], 'ip_query': []}

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
        return d
