import os

INSTALLED_APPS = [
    'GSHEET',
    'RECIPE'
]

""" Sheet Settings """
columns = {
    'desc': 'A',
    'amount': 'C',
    'date': 'D',

    # cell
    'total': 'H16'
}

""" Telegram """
TOKEN = os.getenv('BOT_TOKEN')

""" Google Sheet """
WORKING_SHEET_ID = os.getenv('WORKING_SHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')
CREDS_JSON = os.getenv('CREDS_JSON')

""" Recipe API  """
RECIPE_URL = os.getenv('RECIPE_URL')
RECIPE_APP_ID = os.getenv('RECIPE_APP_ID')
RECIPE_APP_KEY = os.getenv('RECIPE_APP_KEY')
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]