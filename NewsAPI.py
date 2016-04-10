import requests
import time
import datetime
from yahoo_finance import Share
from pprint import pprint

class NewsAPI:
	#Default Constructor
	def __init__(self,ms,ds,ys,me,de,ye,company,apikey):
		#Start Date in int (Month, Day, Year)
		self.ms = ms
		self.ds = ds
		self.ys = ys
		#End Date in int (Month, Day, Year)
		self.me = me
		self.de = de
		self.ye = ye
		#Company Name and AlchemyAPI key
		self.company = company
		self.apikey = apikey
		#Results global variable
		self.rawdata = ''
		self.rawjson = ''
		self.results = ''
	#Try to get the data
	def startGetData(self):
		start = datetime.date(self.ys,self.ms,self.ds)
		startunix = str(time.mktime(start.timetuple()))[0:10]

		end = datetime.date(self.ye,self.me,self.de)
		endunix = str(time.mktime(end.timetuple()))[0:10]
		#Sent the API address
		url = 'https://access.alchemyapi.com/calls/data/GetNews?apikey=' + self.apikey + '&return=enriched.url.enrichedTitle.docSentiment&start=' + startunix + '&end=' + endunix + '&q.enriched.url.enrichedTitle.entities.entity=|text=' + self.company + ',type=company|&q.enriched.url.enrichedTitle.docSentiment.type=positive&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=finance&count=25&outputMode=json'
		#Request the data
		self.raw = requests.get(url)
	
		#I will change with for loop, so that we can have a set number of try to get the info given the response is taking long
		
		while (self.raw.status_code != 200):
			sleep(1)
			
		self.rawjson = self.raw.json()
		
		if (self.rawjson['status'] == 'ERROR'):
			return 'Cannot Get the DATA'
		else:	
			self.results = self.rawjson['result']['docs']
			return 'success'


	def getTimeStamp(self):
		times = []
		for time in self.results:
				timeszzz = time['timestamp']
				times.append(timeszzz)
		return times

	def getSentiment(self):
		sentiment = []
		for sent in self.results:
			sentimentzzz = sent['source']['enriched']['url']['enrichedTitle']['docSentiment']['score']
			sentiment.append(sentimentzzz)
		return sentiment
		
	 def getClosingPrice(self):
	 	closing = []
	 	shareName = Share(self.company)

	 	for t in times:
	 		startDate = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
	 		endDate=startDate
	 		hist = shareName.get_historical(startDate, endDate)
	 		closingPrice = hist[0].['Close']
	 		closing.append(closingPrice)
	 	return closing
