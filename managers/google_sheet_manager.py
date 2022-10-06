from operator import irshift, itemgetter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd



WORKING_SHEET_ID = '1c-7po7AO-psTWGvFhHdH6EL6-C0Vat0LYScSx2e1Qn4'
ITEM_SHEET = 'octubre'
CLIENT_SHEET = 'clients'
CREDS_JSON = 'creeds.json'

class Gsheet_Helper:
    def __init__(self):
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
,
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            CREDS_JSON,
            scope
        )
        
        self.client = gspread.authorize(creds)
        self.gsheet = self.client.open_by_key(WORKING_SHEET_ID)

    def get_items(self):
        items = self.get_sheet(ITEM_SHEET)
        return items

    def get_sheet(self, sheet_name):
        sheet = self.gsheet.worksheet(sheet_name)
        items = pd.DataFrame(sheet.get_all_values())
        print(items)
        return items
    


#print("empieza")
#print(Gsheet_Helper().get_items())