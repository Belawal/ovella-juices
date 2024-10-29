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
        # Message display for user's input prompt    
        print("Please enter the number of juices sold today")
        print("Data input should be in sequence of Mango, Apple, Guava, Pomegranate\n")

        # User input daily sales
        data_str = input("Enter your daily sales here: ")

        # Daily sales display in set i.e. "10", "5", "10", "20".
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            return sales_data  # Return the sales data when valid

def validate_data(values):
    """ 
    Checks if input values can be converted into integers,
    raises ValueError if the input length isn't 4 or contains non-numeric values.
    """
    try:
        # Check if all values are integers
        [int(value) for value in values]
        
        if len(values) != 4:
            raise ValueError(
                f"Exactly 4 values required, you provided {len(values)}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please enter the correct format.\n")
        return False  # Indicate invalid data
    return True  # Data is valid

# This section will update sales on the sales Google worksheet

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new data on new rows with list data.
    """
    print("Updating sales worksheet... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated.\n")

def update_wastage_worksheet(data):
    """
    Update wastage worksheet, add new data on new rows with list data.
    """
    print("Updating wastage worksheet... \n")
    wastage_worksheet = SHEET.worksheet("wastage")
    wastage_worksheet.append_row(data)
    print("wastage worksheet updated.\n")    

def calculate_wastage_data(sales_row):
    """
    Calculate total waste products by 
    production - sale = wastage of product.
    """
    print("Calculating wastage data...\n")
    production = SHEET.worksheet("production").get_all_values()
    production_row = production[-1]
    print(production_row)

    wastage_data = []
    for production, sales in zip(production_row,sales_row):
        wastage = int(production) - sales
        wastage_data.append(wastage)
    print(wastage_data)    





# Main program flow
def main():
    """
    Run all program functions
    """
    data = get_sales()  # get_sales now returns sales data when valid
    sales_data = [int(num) for num in data]  # Convert each entry to an integer
    update_sales_worksheet(sales_data)
    calculate_wastage_data(sales_data)
    new_wastage_data = calculate_wastage_data(sales_data)
    update_wastage_worksheet(new_wastage_data)

print("Welcome to the Daily Record for Ovella Juice Program")
main()
