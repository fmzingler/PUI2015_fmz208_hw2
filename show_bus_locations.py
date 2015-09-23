import sys
import urllib2
import json

if __name__=='__main__':
    #must read 2 arguments: key and bus line
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'% (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	jsonFile = json.load(request)
	Bus = jsonFile["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

   	print "Number of Active Buses : %d" % len(Bus)
        #range(start, stop[, step])
    	for i in range(len(Bus)):
        	position = Bus[i]['MonitoredVehicleJourney']["VehicleLocation"]
        	lat = position['Latitude']
        	lon = position['Longitude']
        	print "Bus %d is at Latitude: %f and Longtitude: %f" % (i, lat, lon)



