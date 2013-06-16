import requests
import json
import configparser 

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
from subprocess import *

# Parse config for API keys
confParser = configparser.ConfigParser()
confParser.read('apiKeys.cfg')
apiTrafikverket = confParser["api"]["trafikverket"]

# Setup
lcd = AdaFruit_CharLCD()

# Used for finding name of stations
def searchStation(name):
	url = 'https://api.trafiklab.se/trafikverket/traininfo/stations/search'
	payload = {'key':apiTrafikverket, 'name':name}
	headers = {'Accept' : 'application/json'}

	response = requests.get(url, params=payload, headers=headers)
	
	#with open('stations.txt','w') as outfile:
	#	json.dump(response.json(), outfile)

def getDepartures(stationName, toStation, companyFilter):
	url = 'https://api.trafiklab.se/trafikverket/traininfo/stations/name/{0}/departures'.format(stationName)
	payload = {'key':apiTrafikverket, 'maxItems':20, 'maxHours': 24}
	headers = {'Accept' : 'application/json'}

	response = requests.get(url, params=payload, headers=headers)
	r = response.json()
	departures = []
	
	# Filter respons to only UL
	for trafikLage in r['LpvTrafiklagen']['Trafiklage']:
		company = trafikLage['TrafikInfoAgareNamn']
		till = trafikLage['Till']
		if companyFilter in company:
			if toStation in till:
				departures.append(trafikLage)

	return departures

def getNextDepartures(fromStation, toStation, count):
	r = getDepartures(fromStation, toStation, "UL/DSB Uppland")
	for item in r[:count]:
		time = item['AnnonseradTidpunktAvgang']
		time = time[11:16]
		r =  time, item['Till']
	return r
#Examples

#getNextDepartures('Uppsala C', '\u00d6rbyhus', 5)
#print("###############")
#getNextDepartures('\u00d6rbyhus', 'Uppsala', 1)

lcd.begin(16,1)

while 1:
	lcd.clear()
	departure = getNextDepartures('\u00d6rbyhus', 'Uppsala', 1)
	
	lcd.message(datetime.now().strftime('%b %d %H:%M:S\n'))
	lcd.message('Next: %s' %(departure[0]) )
	lcd.message('To: %s' %(departure[1]) )
	lcd.message( 'No weather info atm' )

	sleep(20)