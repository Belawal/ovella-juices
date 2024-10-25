import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ovella_juices')

def get_sales():
    """
    Get Daily sales data 
    """
print("Please enter the number of juices sold today")
print("Data input shoud in sequence wise of Mango, Apple, Guava, Pome\n")

data_str = input("enter your daily sales here: ")
print(f"The Sale are {data_str}")

get_sales()
