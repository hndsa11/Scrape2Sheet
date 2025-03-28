# 🟢 Web Scraping and Google Sheets Integration

## 📜 Project Overview
This project demonstrates a simple web scraper using Python that extracts product data from a website and uploads it to a Google Sheet. It leverages `requests`, `BeautifulSoup`, and `gspread` to perform data extraction and cloud integration.

---

## 🚀 Features
- Scrapes product names, prices, and image links from a demo e-commerce website.
- Stores the scraped data in a Google Sheet.
- Automatically creates a new Google Sheet if it doesn’t exist.

---

## 🛠️ Prerequisites
Before running the project, ensure you have:
- Python 3.7+
- A Google Cloud Project with Service Account credentials.
- Installed required Python packages: `requests`, `beautifulsoup4`, `gspread`, `oauth2client`, and `pandas`.

---

## ⚙️ Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Place your `credentials.json` file in the project root directory.
4. Enable Google Sheets and Google Drive API from the Google Cloud Console.
5. Share the Google Sheet with your service account email.

---

## 🟢 Running the Project
Run the main script:
```bash
python main.py
```
If successful, the scraped data will be added to the Google Sheet.

---

## 📝 License
This project is open-source and available under the MIT License.