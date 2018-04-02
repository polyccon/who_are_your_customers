import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat',
    flags=pygeoip.const.MMAP_CACHE)

def ipquery(ip):
    data = gi.record_by_addr(ip)
    country = data['country_name']
    city = data['city']
    longi = data['longitude']
    lat = data['latitude']
    return (str(country), str(city))
