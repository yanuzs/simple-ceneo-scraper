
# Price Scraper and Database Updater

This script scrapes product prices from the Ceneo.pl website and updates the prices in a MySQL database. It utilizes BeautifulSoup for web scraping and SQLAlchemy to interact with the database.

## Features

- **Web Scraping:** The script scrapes product prices from individual product pages on Ceneo.pl.
- **Database Integration:** It connects to a MySQL database to retrieve product IDs and updates the price for each product in the database.
- **Price Formatting:** It handles the conversion of price data from the website (e.g., removing currency symbols, converting commas to dots).

## Technologies Used

- **Python Libraries:** `requests`, `BeautifulSoup`, `SQLAlchemy`
- **Database:** MySQL (using `pymysql` for connection)
- **Web Scraping:** BeautifulSoup for parsing HTML
- **SQLAlchemy:** To manage database operations and updates

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/price-scraper.git
   ```

2. **Install dependencies:**
   You need to install the required Python libraries. You can do this using pip:
   ```bash
   pip install requests beautifulsoup4 sqlalchemy pymysql
   ```

3. **Configure Database:**
   - The script expects a MySQL database with the following table structure:
     ```sql
     CREATE TABLE produkty (
         SKU VARCHAR(255),
         Ceneo_ID INT,
         Ceneo_Cena FLOAT
     );
     ```
   - Ensure that the connection string in the script points to your MySQL instance:
     ```python
     engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/myapp')
     ```

4. **Run the script:**
   After configuring the database and installing dependencies, run the script:
   ```bash
   python scraper.py
   ```

## How It Works

1. **Scraping:** The script retrieves the product page from Ceneo using the `get_html` function. It extracts the price using BeautifulSoup by targeting the appropriate HTML elements.
2. **Updating Database:** After retrieving the price, the `update_price_in_db` function updates the corresponding product's price in the database using SQLAlchemy.
