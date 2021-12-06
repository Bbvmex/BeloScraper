# BeloScraper

As proposed by Belo, this is a test of web scraping
The idea is to scrape the Yahoo Finances website

Specified tickers and fields
Tickers = [“JNJ”, “BRK.B”, “JPM”, “MMM”, “ABBV”, “DIS”, “T”, “PG”, “LOW”, “CI”]
Fields = [Operating Income, Net Income From Continuing Operations, Retained
Earnings, Change In Cash, Net Borrowings]
Webpage = https://finance.yahoo.com/quote/Ticker/financials?p=Ticker

Get data from the last 4 quarters (and most recent)

Observations:
- As the test says that the data can't be scraped by the API, the code was written using Selenium
- All the quarters were scraped
- The field Net Borrowings was not found in any ticker
- The data is outputed as a .csv file
- TODOs were added of steps to improve code
