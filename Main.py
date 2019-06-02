from Scraper import Robinhood, Fidelity
from Excel import Spreadsheet
from os.path import isfile

def start():
	scraper = Robinhood()
	holdings = scraper.get_holdings()
	margin_initial_ratio = scraper.get_margin_initial_ratio()
	maintenance_ratio = scraper.get_maintenance_ratio()
	write_data = Spreadsheet(holdings, margin_initial_ratio, maintenance_ratio, 0, 0)
	if isfile("Stock Logs.xlsx"):
		write_data.load_workbook():
	else:
		write_data.new_workbook():



if __name__ == '__main__':
	start()
