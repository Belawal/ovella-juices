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
    # Message display for user's input prompt    
    print("Please enter the number of juices sold today")
    print("Data input should be in sequence of Mango, Apple, Guava, Pomegranate\n")

    # User input daily sales
    data_str = input("Enter your daily sales here: ")

    # Daily sales display in set i.e. "10", "5", "10", "20".
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """ 
    Checks if input values can be converted into integers,
    raises ValueError if the input length isn't 4 or contains non-numeric values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(f"Exactly 4 values required, you provided {len(values)}")
        
        # Check if all values are integers
        [int(value) for value in values]  # This will raise ValueError if a value is not an integer
        
    except ValueError as e:
        print(f"Invalid data: {e}, please enter the correct format.\n")
        return False  # Indicate invalid data
    return True  # Data is valid

get_sales()
