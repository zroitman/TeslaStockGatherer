from openpyxl import Workbook, load_workbook
from datetime import date

class Spreadsheet:
	def __init__(self, holdings, margin_initial_ratio, maintenance_ratio, buy_orders, sell_orders):
		#Sets up data
		#
		self.holdings = holdings
		self.margins = margin_initial_ratio
		self.maintenance_ratio = maintenance_ratio
		self.buy_orders = buy_orders
		self.sell_orders = sell_orders

	def new_workbook(self):
		#Sets up new workbook to record data for first time
		#
		wb = Workbook()
		ws = wb.active
		ws.column_dimensions["A"].width = 11
		row = ws.max_row

	def load_workbook(self):
		#Opens up spreadsheet to write in new data
		#
		wb = load_workbook("Stock Logs.xlsx")
		ws = wb.active
		row = ws.max_row + 1


# ws = wb.active
# ws.cell(column=1, row = row, value = date.today())
# ws.cell(column=2, row = row, value = holdings)
# wb.save("Stock Info.xlsx")