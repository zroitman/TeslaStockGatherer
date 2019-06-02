import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
	def __init__(self):
		#Launches chrome
		#
		self.url = 'https://eresearch.fidelity.com/eresearch/gotoBL/fidelityTopOrders.jhtml'
		self.driver = webdriver.Chrome(executable_path='.\\dependencies\\chromedriver.exe')
		self.options = Options()
		self.options.add_argument("--headless")
		self.options.add_argument("--window-size=1920x1080")

	def initiate_browser(self):
		#Gets fidelity page
		#
		self.driver.get(self.url)

	def find_tesla_orders(self):
		#Attempts to find tesla in table and gather orders
		#
		try:
			tesla = self.driver.find_element_by_id("t_trigger_TSLA7")
		except:
			return false

		table = self.driver.find_element_by_id("topOrdersTable")
		parent = tesla.find_element_by_xpath("../../../..")

		buy_orders = parent.find_element_by_class_name("fifth")
		sell_orders = parent.find_element_by_class_name("seventh")

		self.driver.quit()
		return [buy_orders.text, sell_orders.text]



if __name__ == '__main__':
	api = Robinhood()
	holdings = api.get_holdings()
	margin_initial_ratio = api.get_margin_initial_ratio()
	maintenance_ratio = api.get_maintenance_ratio()
	scrape = Fidelity()
	scrape.initiate_browser()
	orders = scrape.find_tesla_orders()
	print(orders)
