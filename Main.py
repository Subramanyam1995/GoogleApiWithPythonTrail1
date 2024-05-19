import gspread
from google.oauth2.service_account import Credentials

scopess = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creads = Credentials.from_service_account_file("linkfile.json", scopes=scopess)
client = gspread.authorize(creads)

sheet_id = "1zXaPwVzrxH6YIAQRMKj2qDdpn1pxX8xVxglgUwuBqik"

sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)

print(values_list)


