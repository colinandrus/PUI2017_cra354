import os
import sys
import json
try:
	import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

mta_key = sys.argv[1]
bus_line = sys.argv[2]

# url is contains personal key and bus_line
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
    mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

# Get dictionary from url and json object
response = urllib.urlopen(url)
mta_data = response.read().decode("utf-8")
mta_data = json.loads(mta_data)

# Get part of dictionary we are interested in
try:
	subset_data = mta_data['Siri']['ServiceDelivery']\
	['VehicleMonitoringDelivery'][0]['VehicleActivity']
# If the bus_line you provide is not correct or not running to avoid errors
except:
	print('No busses found with line ID : ' + bus_line)
	subset_data = []


# Print out text to console for route
print('Bus Line : ' + bus_line)
print('Number of Active Buses : ' + str(len(subset_data)))
# Print text to console for each bus
for i in range(len(subset_data)):
    lati = str((subset_data[i]['MonitoredVehicleJourney']\
    	['VehicleLocation']['Latitude']))
    longi = str((subset_data[i]['MonitoredVehicleJourney']\
    	['VehicleLocation']['Longitude']))
    print('Bus ' + str(i) + ' is at latitude' + lati + ' and longtidue ' + longi)
