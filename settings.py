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
WORKING_SHEET_ID = os.environ.get('WORKING_SHEET_ID')
SHEET_NAME = os.environ.get('SHEET_NAME')
CREDS_JSON = os.environ.get('CREDS_JSON')
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

""" Recipe API  """
RECIPE_URL = os.environ.get('RECIPE_URL')
RECIPE_APP_ID = os.environ.get('RECIPE_APP_ID')
RECIPE_APP_KEY = os.environ.get('RECIPE_APP_KEY')
