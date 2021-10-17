import requests

response = requests.get("http://api.ipstack.com/check?access_key=ff1242bed2e914aaae2f8376037f4730").json()
response2 = requests.get("https://geo.ipify.org/api/v2/country,city,vpn?apiKey=at_P1XcCJV6KYh6sFzEiIkgjv9ZeffYb&ipAddress=", response['ip']).json()

#ipstack.com for IP address, type, geolocation
print("-Public IP Address Information-")
print("IP Address:\t", response['ip'])
print("Type:\t\t", response['type'])

print("\n-Geolocation Information-")
print("City:\t\t", response['city'])
print("Region:\t\t", response['region_name'])
print("Region Code:\t", response['region_code'])
print("Country:\t", response['country_name'])
print("Country Code:\t",response['country_code'])
print("Continent:\t", response['continent_name'])
print("Continent Code:\t", response['continent_code'])
print("Latitude:\t", response['latitude'])
print("Longitude:\t",response['longitude'])
print("Timezone:\t", response2['location']['timezone'])

#ipify.org for ISP Information
print("\n-ISP Information-")
print("ISP:\t", response2['isp'])
print("Domain:\t", response2['as']['domain'])
print("ASN:\t", response2['as']['asn'])
print("Route:\t", response2['as']['route'])