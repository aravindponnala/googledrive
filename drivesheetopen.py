import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/drive', 'https://spreadsheets.google.com/feeds', ]
creds = ServiceAccountCredentials.from_json_keyfile_name('service-account.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Doc_1_Sheet").sheet1

# Extract and print all of the values

cell = sheet.find("shiva")
row=str(cell.row)
col=str(cell.col)

value = cell.value
med=sheet.cell(6, 2).value
print(med)

#sheet.update('B6', 80)


