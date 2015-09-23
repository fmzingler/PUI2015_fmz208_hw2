import sys
import urllib2
import json
import csv

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'% (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	jsonFile = json.load(request)
	Bus = jsonFile["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude', 'Longitude', 'StopName', 'StopStatus'])
		
		for EachBus in Bus:
			Latitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			Longitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
			if EachBus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
				StopName = "N/A"
				StopStatus = "N/A"
			else:
				StopName = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
				StopStatus = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
			row = [Latitude, Longitude, StopName, StopStatus]
			writer.writerow(row)

