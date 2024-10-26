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
# message display for user's input prompt    
print("Please enter the number of juices sold today")
print("Data input shoud in sequence wise of Mango, Apple, Guava, Pome\n")

# user input daily sales
data_str = input("enter your daily sales here: ")

# daily sales display in set i.e "10", "5", "10", "20".
sales_data = data_str.split(",")
validate_data(sales_data)


def validate_data(values):
    """ 
    checks Input value can be converted into integers,
    if not then raises ValueError 
    or the volume of value isn't in set of 4. 
    """
    try:
    if len(values) != 4:
        raise ValueError(
            f"Exactly 4 values required, you provided {len(values)}"
             )
             except ValueError as e:
    print(f"Invaid data: {e}, please enter the correct format.\n")

get_sales()
 