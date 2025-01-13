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
    Get daily sales data
    """
    while True:
        print("Please enter the number of juices sold today")
        print("Data input should be in sequence of Mango, Apple, Guava, Pomegranate\n")

        data_str = input("Enter your daily sales here:\n ")
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

def get_last_5_entries_sales():
    """
    Collect last 5 entries from each column in the 'sales' sheet and return them as a list.
    """    
    sales = SHEET.worksheet("sales")
    columns = []

    for ind in range(1, 5):
        column = sales.col_values(ind)
        columns.append(column[-5:])  # Collect last 5 entries from each column
   
    return columns

def main():
    """
    Run all program functions
    """
    data = get_sales()
    sales_data = [int(num) for num in data]  # Ensure sales data is a list of integers
    update_worksheet(sales_data, "sales")
    wastage_data = calculate_wastage_data(sales_data)
    update_worksheet(wastage_data, "wastage")

    # Optionally, retrieve and print the last 5 sales entries
    columns = get_last_5_entries_sales()
    print("Last 5 entries in each sales column:")
    print("Mango | Apple | Guava | Pome |\n"
            f"{columns[0][0]}    |  {columns[0][1]}    |  {columns[0][2]}    |  {columns[0][3]}    |\n"
            f"{columns[1][0]}    |  {columns[1][1]}    |  {columns[1][2]}    |  {columns[1][3]}    |\n"
            f"{columns[2][0]}    |  {columns[2][1]}    |  {columns[2][2]}    |  {columns[2][3]}    |\n"
            f"{columns[3][0]}    |  {columns[3][1]}    |  {columns[3][2]}    |  {columns[3][3]}    |\n"
            )

print("Welcome to the Daily Record for Ovella Juice Program")
main()