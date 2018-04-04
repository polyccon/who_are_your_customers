#!/usr/bin/env python

import geoip2.database
import glob
import gzip
import os
import pandas as pd
from user_agents import parse
import sys


def usage():

	print("Usage: python " + os.path.basename(__file__) + "path-to-source-data-directory path-to-geolite2-city-database")

def main(data):
    data['city']=[]
    data['country']=[]

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        usage()
        sys.exit(0)
    if len(sys.argv) == 3:
        dir       = sys.argv[1]
        geoip2_db = sys.argv[2]
    else:
        usage()
        sys.exit(2)

    print("Finding GZIP files to load...")
    file_list = sorted(glob.glob(dir + "/" + "*.gz"))

    print("Loading GeoLite2-City database...")
    
    geoip2_db_reader = geoip2.database.Reader(geoip2_db)

    ip_array = data['IP']

    for ip in ip_array:
        ip = ip.split(", ")[0]
        try:

            geoip2_response = geoip2_db_reader.city(ip)
        except:

            geoip2_city    = "Unknown"
            geoip2_country = "Unknown"


        try:

            if geoip2_response.city.name:
                geoip2_city_exists = 1

            else:
                geoip2_city_exists = 0

        except:

            geoip2_city_exists = 0
        if geoip2_city_exists == 1:
            if geoip2_response.city.name:
                geoip2_city    = geoip2_response.city.name

            else:
                geoip2_city = "Unknown"

        else:
            geoip2_city = "Unknown"

        try:

            if geoip2_response.country.name:
                geoip2_country_exists = 1

            else:
                geoip2_country_exists = 0

        except:
            geoip2_country_exists = 0

        if geoip2_country_exists == 1:
            if geoip2_response.country.name:
                geoip2_country = geoip2_response.country.name

            else:
                geoip2_country = "Unknown"
        else:
            geoip2_country = "Unknown"

        data['city'].append(geoip2_city)
        data['country'].append(geoip2_country)

    return data


if __name__ == "__main__":
    main()
