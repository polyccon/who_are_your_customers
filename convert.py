#!/usr/bin/env python

import geoip2.database
import glob
import gzip
import os
import pandas as pd
import sys

def main(data, pathtodatabase):
    data['city']=[]
    data['country']=[]

    geoip2_db_reader = geoip2.database.Reader(pathtodatabase)

    ip_array = data['IP']
	print ('Started looping over IP addresses for converting')

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
