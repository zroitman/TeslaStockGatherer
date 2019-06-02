from openpyxl import Workbook, load_workbook
from datetime import date

class Spreadsheet:
	def __init__(self, holdings, margin_initial_ratio, maintenance_ratio, buy_orders, sell_orders):
		#Sets up data
		#
		self.holdings = holdings
		self.margin_initial_ratio = margin_initial_ratio
		self.maintenance_ratio = maintenance_ratio
		self.buy_orders = buy_orders
		self.sell_orders = sell_orders
		self.date = date.today()
		self.wb = None
		self.ws = None
		self.row = None

	def new_workbook(self):
		#Sets up new workbook to record data for first time
		#
		self.wb = Workbook()
		self.ws = self.wb.active
		self.ws.column_dimensions["A"].width = 11
		self.ws['A1'] = "Date"
		self.ws['B1'] = "Fidelity Holdings"
		self.ws['C1'] = "Margin Initial Ratio"
		self.ws['D1'] = "Maintenance Ratio"
		self.ws['E1'] = "Buy Orders"
		self.ws['F1'] = "Sell Orders"

	def load_workbook(self):
		#Opens up spreadsheet to write in new data
		#
		self.wb = load_workbook("Tesla Stock Logs.xlsx")
		self.ws = self.wb.active

	def save_data(self):
		#Saves data in spreadsheet
		#
		self.row = self.ws.max_row + 1
		self.ws.cell(column=1, row = self.row, value = self.date)
		self.ws.cell(column=2, row = self.row, value = self.holdings)
		self.ws.cell(column=3, row = self.row, value = self.margin_initial_ratio)
		self.ws.cell(column=4, row = self.row, value = self.maintenance_ratio)
		self.ws.cell(column=5, row = self.row, value = self.buy_orders)
		self.ws.cell(column=6, row = self.row, value = self.sell_orders)
		self.wb.save("Tesla Stock Logs.xlsx")