import requests

class Robinhood:
	def __init__(self):
		self.tesla_id = 'e39ed23a-7bd1-4587-b060-71988d9ef483'
		self.tesla_holdings_url = 'https://api.robinhood.com/instruments/popularity/'
		self.tesla_instruments_url = f'https://api.robinhood.com/instruments/{self.tesla_id}/'

	def get_holdings(self):
		#Requesting page where holdings are found with tesla id
		r = requests.get(self.tesla_holdings_url, params={'ids':self.tesla_id})

		#Putting data into readable format (dict)
		data = r.json()

		#Extracting number of holdings
		holdings = data['results'][0]["num_open_positions"]

		return holdings

	def get_margin_initial_ratio(self):
		#Requesting tesla instruments page
		r = requests.get(self.tesla_instruments_url)

		#Putting data into readable format (dict)
		data = r.json()

		#Extract margin initial ratio
		margin_initial_ratio = data['margin_initial_ratio']

		return margin_initial_ratio

	def get_maintenance_ratio(self):
		#Requesting tesla instruments page
		r = requests.get(self.tesla_instruments_url)

		#Putting data into readable format (dict)
		data = r.json()

		#Extract maintence ratio
		maintenance_ratio = data['maintenance_ratio']

		return maintenance_ratio

class Fidelity:
	pass