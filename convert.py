from ipquery import ipquery

def convert_ip(data):
    data['converted_city'] = []
    data['converted_country'] = []
    error_count = 0
    empty_count = 0

    for IP in data['IP']:
        try:
            if IP.find(',') == -1:
                data['converted_country'] = ipquery(IP)[0]
                data['converted_city'] = ipquery(IP)[1]
            elif len(IP) < 7:
                data['converted_country'] = None
                data['converted_city'] = None
                print (len(IP))
                empty_count +=1
            else:
                try:
                    ips = IP.split(', ')
                    data['converted_country'] = ipquery(ips[0])[0]
                    data['converted_city'] = ipquery(ips[0])[1]

                except:
                    data['converted_country'] = ipquery(ips[1])[0]
                    data['converted_city'] = ipquery(ips[1])[1]


        except:
                data['converted_country'] = None
                data['converted_city'] = None
                error_count += 1
    print ('error', error_count, 'empty', empty_count)
