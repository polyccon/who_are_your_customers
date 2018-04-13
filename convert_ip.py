#!/usr/bin/env python
import ipaddress
from geolite2 import geolite2

def isipvalid(ips):
    if len(ips) == 1:
        try:
            ip_valid = ipaddress.ip_address(ips[0])
            return [ip_valid]
        except:
            return None
    else:
        try:
            ip_valid_0 = ipaddress.ip_address(ips[0])
        except:
            ip_valid_0 = None
        try:
            ip_valid_1 = ipaddress.ip_address(ips[1])
        except:
            ip_valid_1 = None
        if all([ip_valid_0, ip_valid_1]):
            return [ip_valid_0, ip_valid_1]
        elif ip_valid_0 is not None:
            return [ip_valid_0]
        elif ip_valid_1 is not None:
            return [ip_valid_1]
        else:
            return None

def main(data):
    data['city'] = []
    data['country'] = []

    ip_array = data['IP']
    reader = geolite2.reader()

    print ('Starting IP conversion to city, country')
    
    for ip in ip_array:
        ips = ip.split(', ')
        ip_valid = isipvalid(ips)

        if ip_valid is not None and len(ip_valid) ==1:
            location = reader.get(ip_valid[0])
            if location is not None and 'country' in location.keys() and 'city' in location.keys():
                data['country'].append(location['country']['names']['en'])
                data['city'].append(location['city']['names']['en'])
            elif location is not None and 'country' in location.keys():
                data['country'].append(location['country']['names']['en'])
                data['city'].append('Unknown')
            elif location is not None and 'city' in location.keys():
                data['city'].append(location['city']['names']['en'])
                data['country'].append('Unknown')
            else:
                data['country'].append('Unknown')
                data['city'].append('Unknown')

        elif ip_valid is not None and len(ip_valid) >1:
            location_0 = reader.get(ip_valid[0])
            location_1 = reader.get(ip_valid[1])
            if location_0 is not None and 'country' in location_0.keys() and 'city' in location_0.keys():
                data['country'].append(location_0['country']['names']['en'])
                data['city'].append(location_0['city']['names']['en'])
            elif location_1 is not None and 'country' in location_1.keys() and 'city' in location_1.keys():
                data['country'].append(location_1['country']['names']['en'])
                data['city'].append(location_1['city']['names']['en'])
            elif location_1 is not None and 'country' in location_1.keys():
                data['country'].append(location_1['country']['names']['en'])
                data['city'].append('Unknown')
            elif location_1 is not None and 'city' in location_1.keys():
                data['city'].append(location_1['city']['names']['en'])
                data['country'].append('Unknown')
            else:
                data['country'].append('Unknown')
                data['city'].append('Unknown')

        else:
            data['country'].append('Unknown')
            data['city'].append('Unknown')
    geolite2.close()
    return data
