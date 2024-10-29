import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get daily sales data
    """
    while True:
        print("Please enter the number of juices sold today")
        print("Data input should be in sequence of Mango, Apple, Guava, Pomegranate\n")

        data_str = input("Enter your daily sales here: ")
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            return sales_data

def validate_data(values):
    """ 
    Checks if input values can be converted into integers,
    raises ValueError if the input length isn't 4 or contains non-numeric values.
    """
    try:
        [int(value) for value in values]
        
        if len(values) != 4:
            raise ValueError(f"Exactly 4 values required, you provided {len(values)}")
        
    except ValueError as e:
        print(f"Invalid data: {e}, please enter the correct format.\n")
        return False
    return True

def update_worksheet(data, worksheet):
    """
    Update each worksheet with provided data
    """ 
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")

def calculate_wastage_data(sales_row):
    """
    Calculate total waste products by 
    production - sale = wastage of product.
    """
    print("Calculating wastage data...\n")
    production = SHEET.worksheet("production").get_all_values()
    production_row = production[-1]
    
    wastage_data = []
    for production, sales in zip(production_row, sales_row):
        wastage = int(production) - sales
        wastage_data.append(wastage)
    
    print("Wastage data calculated:", wastage_data)
    return wastage_data

def main():
    """
    Run all program functions
    """
    data = get_sales()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    wastage_data = calculate_wastage_data(sales_data)
    update_worksheet(wastage_data, "wastage")

print("Welcome to the Daily Record for Ovella Juice Program")
main()
