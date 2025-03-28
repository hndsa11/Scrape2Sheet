import requests
from bs4 import BeautifulSoup
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Authentication Setup
def authenticate_google_sheet(sheet_url):
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # فتح الشيت باستخدام الرابط بدل من الإنشاء
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.sheet1 

    return worksheet

# Function to Scrape Data
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_data = []
    for item in soup.select('.product_pod'):
        name = item.h3.a['title']
        price = item.select_one('.price_color').text
        image = item.find('img')['src']

        product_data.append({
            'Name': name,
            'Price': price,
            'Image': image
        })

    return product_data

# Main Function
def main():
    sheet_url = "https://docs.google.com/spreadsheets/d/15JBDpVuF_rgyXu3PNWpNR2g_zJ-reRpRpK-rY1mpKuo/edit?gid=0#gid=0"
    worksheet = authenticate_google_sheet(sheet_url)

    url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    data = scrape_website(url)

    if data:
        df = pd.DataFrame(data)
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("✅ Data uploaded successfully to the existing Google Sheet!")
    else:
        print("❌ No data found.")

if __name__ == "__main__":
    main()
