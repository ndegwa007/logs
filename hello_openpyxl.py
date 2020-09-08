from openpyxl import Workbook

workbook = Workbook() 

sheet = workbook.active #activate excel sheets


sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx") #create excel docs