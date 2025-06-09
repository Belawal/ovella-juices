<h1>Ovella Juice Inventory Manager</h1>
<img src="/assets/readmeimage.jpg">
<h2>Introduction</h2>
Ovella Juice Inventory Manager is an easy-to-use program that helps small business owners keep track of their juice production, sales, and wastage on a daily basis.
It records data for Mango, Apple, Guava, and Pomegranate juices. 
This application builds on my earlier project, Ovella, and takes inspiration from the Love Sandwiches project, which helped me design a simple and organized way to enter and track daily records.

<h2>What This Program Can Do</h2>
Record Sales: Enter the daily number of juices sold for each type of juice.
Log Production: Record how much of each juice type was produced each day.
Calculate Wastage: The program calculates how much juice was wasted by subtracting the number of juices sold from the number produced.
Reliable Data Entry: The program makes sure you enter exactly four numbers, so data is always complete.

<h2>How It Works</h2>
Enter Data: When asked, you’ll enter the number of juices sold in this order: Mango, Apple, Guava, and Pomegranate.
Data Check: The program checks your entries to make sure they’re numbers and that all four types are included.
Google Sheets Connection: Your data will be saved to a Google Sheet where it’s easy to view.
Wastage Calculation: After you enter sales and production data, the program will calculate wastage and save it in the Google Sheet.

<h2>Flowchart</h2>
![Flowchart]<img src="/assets/flowchart_PP3.jpg">

The Ovella Juice sales tracking program follows this structured workflow:

User Input
-Collects comma-separated sales data for 4 juice flavors (Mango, Apple, Guava, Pomegranate).

Validation
-Ensures input has exactly 4 integers. Loops until valid.

Google Sheets Updates
-Writes validated sales to the "sales" worksheet.
-Calculates wastage (Production - Sales) and updates "wastage" worksheet.

Output
-Displays the last 5 sales entries for review.

<h2>Tools Used</h2>
Python: The main programming language used.
Google Sheets API: Used to save and view data in Google Sheets.
gspread: A tool that helps connect Python with Google Sheets.
Google OAuth2: Keeps your data secure by allowing safe access to Google Sheets.

<h2>Inspiration</h2>
This project was inspired by the Love Sandwiches project, which provided a helpful framework for organizing data and checking that entries are correct. 
Adapting its design to Ovella Juice Inventory Manager made it easier to set up daily records for juices.

<h2>>How to Set It Up</h2>
Install Tools:

pip install gspread google-auth
Get Google Sheets Access:

Enable Google Sheets API for your account.
Download the credentials file (creds.json) and save it in your project folder.

<h2>Summary</h2>
Ovella Juice Inventory Manager is designed to help small businesses record and manage daily production, sales, and wastage of juice products. 
It’s easy to use, stores data securely in Google Sheets, and can be accessed online with Heroku.
