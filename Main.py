from Scraper import Robinhood, Fidelity
from Excel import Spreadsheet
from os.path import isfile
import time

def start():
	#Navigates robinhood api for tesla holdings and ratios
	api = Robinhood()
	holdings = api.get_holdings()
	margin_initial_ratio = api.get_margin_initial_ratio()
	maintenance_ratio = api.get_maintenance_ratio()

	#Scrapes fidelity for tesla buy and sell orders
	scrape = Fidelity()
	scrape.initiate_browser()
	time.sleep(1)
	orders = scrape.find_tesla_orders()
	scrape.close_webdriver()

	#Puts data into spreadsheet
	write_data = Spreadsheet(holdings, margin_initial_ratio, maintenance_ratio, orders[0], orders[1])
	if isfile("Tesla Stock Logs.xlsx"):
		write_data.load_workbook()
	else:
		write_data.new_workbook()
	write_data.save_data()



if __name__ == '__main__':
	start()
