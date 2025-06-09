# Ovella Juice Inventory Manager

![Ovella Juice Banner](/assets/readmeimage.jpg)

## Introduction

Ovella Juice Inventory Manager is a simple, beginner-friendly program that helps small business owners track daily juice production, sales, and wastage. It works with four juice flavors: Mango, Apple, Guava, and Pomegranate.

This project builds on my earlier "Ovella" project and was inspired by the Love Sandwiches walkthrough. That example helped me structure the flow, use Google Sheets, and keep things easy to understand.

## What This Program Can Do

* **Record Sales:** Enter daily sales for each juice.
* **Log Production:** Enter how many were produced.
* **Calculate Wastage:** It subtracts sales from production to find waste.
* **Reliable Input:** You must enter exactly 4 numbers to avoid missing data.

## How It Works

* The program first asks you to enter 4 numbers (comma-separated) for either sales or production: Mango, Apple, Guava, and Pomegranate.
* It checks the input to make sure it includes only 4 valid numbers.
* It then connects to a Google Sheet and logs the sales or production.
* Finally, it calculates wastage and stores that too.

## Tools Used

* **Python**
* **gspread** (to connect to Google Sheets)
* **Google Sheets API**
* **Google OAuth2 Credentials**

## How to Set It Up

### 1. Install Required Packages:

```bash
pip install gspread google-auth
```

### 2. Connect Google Sheets:

* Go to Google Developers Console
* Enable Google Sheets API
* Download your `creds.json` file
* Put it inside your project folder

## Flowchart

![Flowchart](/assets/flowchart_PP3.jpg)

This is the basic structure:

1. User inputs 4 numbers (sales or production)
2. Data is validated
3. Data is sent to the correct worksheet
4. Wastage is calculated (production - sales)
5. Output is shown in terminal

## Testing

I tested both valid and invalid inputs to make sure everything runs as expected.

###  Valid Input Example:

* Input: `10,20,15,12`
* Result: Accepted and added to sheet

###  Invalid Input Examples:

* Input: `10,20` → Rejected (not enough values)
* Input: `ten,20,15,12` → Rejected (non-numeric)
* Input: `10,20,15,12,5` → Rejected (too many values)

*Screenshots of both successful and failed run*
![SucessfulRun](/assets/workingcode.jpg)
![FailedRun](/assets/notvalid.jpg)


## Deployment

You can run this program both locally and on the web.

###  Live Demo:

[Heroku App](https://ovella-juices-pp3-19c88964a8ee.herokuapp.com/)

###  GitHub Repo:

[GitHub Repository](https://github.com/Belawal/ovella-juices.git)

###  Google Sheet:

[View Data on Google Sheets](https://docs.google.com/spreadsheets/d/1iZJMOZc5QaWu379VZvac05KP6WkeNSqpYpsCl0uzLbI/edit?usp=sharing)

## Inspiration

The Love Sandwiches walkthrough gave me the idea of organizing the program into small, clear steps and connecting Python to Google Sheets in a safe and secure way.

## Summary

Ovella Juice Inventory Manager is built to make your daily stock-taking easier. Whether you're checking how much juice you sold or figuring out what went to waste, this tool helps you log it all in one place—and you can access your records online too.

No fancy dashboards or extra fluff. Just clean, useful tracking for your juice business.
