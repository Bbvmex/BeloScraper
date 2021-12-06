from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime
import csv

def parseNumber(numberList):
    return [int(num.replace(',', '')) for num in numberList]

class scrapYahoo:
    def __init__(self, driver, tickers, fields):
        self.driver = driver
        self.tickers = tickers
        self.fields = fields
        self.webpage = 'https://finance.yahoo.com/quote/'
        self.tabs = ['financials', 'balance-sheet', 'cash-flow']
        self.output = {}
        self.dates = {}
    
    # Get the page in driver -> opens directly in Income Statement tab
    def get_page(self, ticker):
        self.driver.get(self.webpage+ticker+'/financials?p='+ticker)
        self.expand_all()
    
    # Get the desired tab
    def set_tab(self, tab):
        self.driver.find_element(By.XPATH, "//a[contains(@href, '"+tab+"')]").click()
        self.expand_all()

    # Organize data by quarters in page and wait for it to load
    def set_quarterly(self):
        # Sometimes it gets th button before the page is changed, getting a stale reference -> TODO find a better option for this wait
        time.sleep(2)
        quarterlyButton = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Quarterly')]"))
        )
        quarterlyButton.click()        
        # Wait for elements to load -> TODO find a better option for this wait
        time.sleep(5)
        # Checks if the annual not its a link
        # If not, repeat the procedure
        annualButton = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Annual')]"))
        )
        annualButton = annualButton.find_element(By.XPATH, '../..')
        if '$linkColor' in annualButton.get_attribute('class'):
            return
        else:
            self.set_quarterly()


    def expand_all(self):
        time.sleep(2)
        try:
            expandButton = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Expand')]"))
            )
            expandButton.click()
        except TimeoutException:
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Collapse')]"))
                )
            except TimeoutError:
                raise TimeoutError

    # Saves the dates of each column in self.dates to add to the output
    def get_dates(self):
        
        field_cell = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//span[starts-with(text(), 'Breakdown')]"))
        )
        cols = field_cell.find_elements(By.XPATH, '../..//div')
        elements = [col.text for col in cols]
        print(elements)
        values = [datetime.strftime(datetime.strptime(date, "%m/%d/%Y"), "%Y-%d-%m") for date in elements[-5:]]
        self.dates = {'Q0': values[-5],
                    'Q1': values[-4],
                    'Q2': values[-3],
                    'Q3': values[-2],
                    'Q4': values[-1]
                    }

    # Find desired field and return the row data
    def get_field_row_values(self, field):
        field_cell = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@title='"+field+"']"))
        )
        # Get all first order divs (columns) from second parent (row)
        cols = field_cell.find_elements(By.XPATH, '../..//div')
        elements = [col.text for col in cols]
        return elements

    # Q0 is the most recent quarter. Each index represents the data from index-quarters back
    def parse_row(self, elements):
        del(elements[1:3])
        values = [int(num.replace(',', ''))*1000 for num in elements[1:]]
        return {'Q0': values[-5],
                'Q1': values[-4],
                'Q2': values[-3],
                'Q3': values[-2],
                'Q4': values[-1]
                }
    
    # Scrap routine to get all the desired data
    def scrap_data(self):
        for ticker in self.tickers:
            print(ticker)
            self.output[ticker] = {}
            self.output[ticker]['scrapedate'] = datetime.strftime(datetime.now(), "%Y-%m-%d")
            fieldsLeft = self.fields.copy()
            self.get_page(ticker)
            for tab in self.tabs:
                # Skip default tab
                if tab != 'financials':
                    self.set_tab(tab)
                self.set_quarterly()
                self.get_dates()
                for field in fieldsLeft:
                    print(field)
                    self.output[ticker][field] = {}
                    try: 
                        data = self.get_field_row_values(field)
                        self.output[ticker][field]['quarters'] = self.parse_row(data)
                        self.output[ticker][field]['dates'] = self.dates
                        fieldsLeft.remove(field)
                    except TimeoutException:
                        continue
        self.driver.quit()
        return self.output

    # Generate CSV file with the scraped data -> external data or filename optional
    def generate_CSV(self, parsedData=None, outFile = 'output.csv'):
        if not parsedData:
            parsedData = self.output
        csv_list = []
        for ticker in parsedData:
            scrapeDate = parsedData[ticker]['scrapedate']
            for field in parsedData[ticker]:
                if field == 'scrapedate' or parsedData[ticker][field] == {}:
                    continue
                for quarter in parsedData[ticker][field]['quarters']:
                    value = parsedData[ticker][field]['quarters'][quarter]
                    date = parsedData[ticker][field]['dates'][quarter]
                    csv_list.append([ticker, field, value, date, scrapeDate])
        fields = ['Ticker', 'Field', 'Value', 'End Date', 'Scrape Date']
        with open(outFile, 'w', newline='') as outputFile:
            wr = csv.writer(outputFile)
            wr.writerow(fields)
            wr.writerows(csv_list)

          


if __name__ == '__main__':
    # Main routine, create a scraper Object and start scraping the fields and tickers bellow
    # .generate_csv can receive a filename to output the data
    # Using GeckoDriver in headless mode
    # TODO Add command line parameters to run the program
    # TODO More tries to catch possible problems
    # TODO make tests for the program
    # TODO Evaluate sleep code and speed up the scraping
    # TODO pass website and query as parameter for the object
    output = {}
    tickers = ["JNJ", "BRK-B", "JPM", "MMM", "ABBV", "DIS", "T", "PG", "LOW", "CI"]
    fields = ["Operating Income", "Net Income from Continuing Operations", "Retained Earnings", "Changes in Cash", "Net Borrowings"]

    options = Options()
    options.add_argument("--headless")

    with webdriver.Firefox(options=options) as driver:
        driver.implicitly_wait(10)
        scraper = scrapYahoo(driver, tickers, fields)
        scraper.scrap_data()
        scraper.generate_CSV(outFile = 'output7.csv')

