import requests
from datetime import datetime
import json



# Auxiliary tools: Notepad++

def requestsTest():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept": "*/*",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Referer": "https://finance.yahoo.com/quote/JNJ/financials?p=JNJ",
    "Origin": "https://finance.yahoo.com",
    "DNT": "1",
    "Connection": "keep-alive",
    #"Cookie": "B=98ahsihgqk6pl&b=3&s=80; A1=d=AQABBDUbqmECEJGLzKn0nbfkMC7NmII64IsFEgEBAQFsq2GzYQAAAAAA_eMAAAcINRuqYZQ8KpQ&S=AQAAAs2ispaaHmN5CWqjIFDKL9g; A3=d=AQABBDUbqmECEJGLzKn0nbfkMC7NmII64IsFEgEBAQFsq2GzYQAAAAAA_eMAAAcINRuqYZQ8KpQ&S=AQAAAs2ispaaHmN5CWqjIFDKL9g; A1S=d=AQABBDUbqmECEJGLzKn0nbfkMC7NmII64IsFEgEBAQFsq2GzYQAAAAAA_eMAAAcINRuqYZQ8KpQ&S=AQAAAs2ispaaHmN5CWqjIFDKL9g&j=WORLD; GUC=AQEBAQFhq2xhs0IgMQTU; thamba=1; cmp=t=1638538044&j=0; PRF=t%3DJNJ",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"}

    link = 'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/'
    queryOriginal = 'JNJ?lang=en-US&region=US&symbol=JNJ&padTimeSeries=true&type=quarterlyTaxEffectOfUnusualItems%2CtrailingTaxEffectOfUnusualItems%2CquarterlyTaxRateForCalcs%2CtrailingTaxRateForCalcs%2CquarterlyNormalizedEBITDA%2CtrailingNormalizedEBITDA%2CquarterlyNormalizedDilutedEPS%2CtrailingNormalizedDilutedEPS%2CquarterlyNormalizedBasicEPS%2CtrailingNormalizedBasicEPS%2CquarterlyTotalUnusualItems%2CtrailingTotalUnusualItems%2CquarterlyTotalUnusualItemsExcludingGoodwill%2CtrailingTotalUnusualItemsExcludingGoodwill%2CquarterlyNetIncomeFromContinuingOperationNetMinorityInterest%2CtrailingNetIncomeFromContinuingOperationNetMinorityInterest%2CquarterlyReconciledDepreciation%2CtrailingReconciledDepreciation%2CquarterlyReconciledCostOfRevenue%2CtrailingReconciledCostOfRevenue%2CquarterlyEBITDA%2CtrailingEBITDA%2CquarterlyEBIT%2CtrailingEBIT%2CquarterlyNetInterestIncome%2CtrailingNetInterestIncome%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyInterestIncome%2CtrailingInterestIncome%2CquarterlyContinuingAndDiscontinuedDilutedEPS%2CtrailingContinuingAndDiscontinuedDilutedEPS%2CquarterlyContinuingAndDiscontinuedBasicEPS%2CtrailingContinuingAndDiscontinuedBasicEPS%2CquarterlyNormalizedIncome%2CtrailingNormalizedIncome%2CquarterlyNetIncomeFromContinuingAndDiscontinuedOperation%2CtrailingNetIncomeFromContinuingAndDiscontinuedOperation%2CquarterlyTotalExpenses%2CtrailingTotalExpenses%2CquarterlyRentExpenseSupplemental%2CtrailingRentExpenseSupplemental%2CquarterlyReportedNormalizedDilutedEPS%2CtrailingReportedNormalizedDilutedEPS%2CquarterlyReportedNormalizedBasicEPS%2CtrailingReportedNormalizedBasicEPS%2CquarterlyTotalOperatingIncomeAsReported%2CtrailingTotalOperatingIncomeAsReported%2CquarterlyDividendPerShare%2CtrailingDividendPerShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyDilutedEPSOtherGainsLosses%2CtrailingDilutedEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardDilutedEPS%2CtrailingTaxLossCarryforwardDilutedEPS%2CquarterlyDilutedAccountingChange%2CtrailingDilutedAccountingChange%2CquarterlyDilutedExtraordinary%2CtrailingDilutedExtraordinary%2CquarterlyDilutedDiscontinuousOperations%2CtrailingDilutedDiscontinuousOperations%2CquarterlyDilutedContinuousOperations%2CtrailingDilutedContinuousOperations%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyBasicEPSOtherGainsLosses%2CtrailingBasicEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardBasicEPS%2CtrailingTaxLossCarryforwardBasicEPS%2CquarterlyBasicAccountingChange%2CtrailingBasicAccountingChange%2CquarterlyBasicExtraordinary%2CtrailingBasicExtraordinary%2CquarterlyBasicDiscontinuousOperations%2CtrailingBasicDiscontinuousOperations%2CquarterlyBasicContinuousOperations%2CtrailingBasicContinuousOperations%2CquarterlyDilutedNIAvailtoComStockholders%2CtrailingDilutedNIAvailtoComStockholders%2CquarterlyAverageDilutionEarnings%2CtrailingAverageDilutionEarnings%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyOtherunderPreferredStockDividend%2CtrailingOtherunderPreferredStockDividend%2CquarterlyPreferredStockDividends%2CtrailingPreferredStockDividends%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyMinorityInterests%2CtrailingMinorityInterests%2CquarterlyNetIncomeIncludingNoncontrollingInterests%2CtrailingNetIncomeIncludingNoncontrollingInterests%2CquarterlyNetIncomeFromTaxLossCarryforward%2CtrailingNetIncomeFromTaxLossCarryforward%2CquarterlyNetIncomeExtraordinary%2CtrailingNetIncomeExtraordinary%2CquarterlyNetIncomeDiscontinuousOperations%2CtrailingNetIncomeDiscontinuousOperations%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyEarningsFromEquityInterestNetOfTax%2CtrailingEarningsFromEquityInterestNetOfTax%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyOtherNonOperatingIncomeExpenses%2CtrailingOtherNonOperatingIncomeExpenses%2CquarterlySpecialIncomeCharges%2CtrailingSpecialIncomeCharges%2CquarterlyGainOnSaleOfPPE%2CtrailingGainOnSaleOfPPE%2CquarterlyGainOnSaleOfBusiness%2CtrailingGainOnSaleOfBusiness%2CquarterlyOtherSpecialCharges%2CtrailingOtherSpecialCharges%2CquarterlyWriteOff%2CtrailingWriteOff%2CquarterlyImpairmentOfCapitalAssets%2CtrailingImpairmentOfCapitalAssets%2CquarterlyRestructuringAndMergernAcquisition%2CtrailingRestructuringAndMergernAcquisition%2CquarterlySecuritiesAmortization%2CtrailingSecuritiesAmortization%2CquarterlyEarningsFromEquityInterest%2CtrailingEarningsFromEquityInterest%2CquarterlyGainOnSaleOfSecurity%2CtrailingGainOnSaleOfSecurity%2CquarterlyNetNonOperatingInterestIncomeExpense%2CtrailingNetNonOperatingInterestIncomeExpense%2CquarterlyTotalOtherFinanceCost%2CtrailingTotalOtherFinanceCost%2CquarterlyInterestExpenseNonOperating%2CtrailingInterestExpenseNonOperating%2CquarterlyInterestIncomeNonOperating%2CtrailingInterestIncomeNonOperating%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlyOtherOperatingExpenses%2CtrailingOtherOperatingExpenses%2CquarterlyOtherTaxes%2CtrailingOtherTaxes%2CquarterlyProvisionForDoubtfulAccounts%2CtrailingProvisionForDoubtfulAccounts%2CquarterlyDepreciationAmortizationDepletionIncomeStatement%2CtrailingDepreciationAmortizationDepletionIncomeStatement%2CquarterlyDepletionIncomeStatement%2CtrailingDepletionIncomeStatement%2CquarterlyDepreciationAndAmortizationInIncomeStatement%2CtrailingDepreciationAndAmortizationInIncomeStatement%2CquarterlyAmortization%2CtrailingAmortization%2CquarterlyAmortizationOfIntangiblesIncomeStatement%2CtrailingAmortizationOfIntangiblesIncomeStatement%2CquarterlyDepreciationIncomeStatement%2CtrailingDepreciationIncomeStatement%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlySellingAndMarketingExpense%2CtrailingSellingAndMarketingExpense%2CquarterlyGeneralAndAdministrativeExpense%2CtrailingGeneralAndAdministrativeExpense%2CquarterlyOtherGandA%2CtrailingOtherGandA%2CquarterlyInsuranceAndClaims%2CtrailingInsuranceAndClaims%2CquarterlyRentAndLandingFees%2CtrailingRentAndLandingFees%2CquarterlySalariesAndWages%2CtrailingSalariesAndWages%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue%2CquarterlyExciseTaxes%2CtrailingExciseTaxes%2CquarterlyOperatingRevenue%2CtrailingOperatingRevenue'
    queryStart = 'JNJ?lang=en-US&region=US&symbol=JNJ&padTimeSeries=true&type='
    # Specified: Operating Income, Net Income from Continuing Operations, Retained Earnings, Change in Cash, Net Borrowings
    query = ['OperatingIncome',  'NetIncomeContinuousOperations', 'RetainedEarnings', 'ChangesInCash']
    # Specified: Get only quarterly values
    #query = ['quarterly'+qItem+'%2Ctrailing'+qItem for qItem in query]
    query = '%2C'.join(query)
    #queryEnd = '&merge=false&period1=493590046&period2=1638539342&corsDomain=finance.yahoo.com'
    queryEnd = '&merge=false&period1=493590046&period2=1638636962&corsDomain=finance.yahoo.com'

    def parseQuarterly(data):
        # Parse the data from one quarter to a dictionary
        output = {}
        original_key = data['meta']['type']
        timestamps = data['timestamp']
        quarters_data = data[original_key]
        #Remove quarterly from the key name
        new_key = original_key.replace('quarterly','')
        for i in range(len(timestamps)):
            quarter = timestamps[i]
            output[new_key][quarter] = data[original_key][i]['reportedValue']['raw']
        return output



    final_output = {}

    r = requests.get(link+queryStart+query+queryEnd, headers = header)

    full_response = json.loads(r.text)['timeseries']
    if not full_response['error']:
        # List of dictionaries
        result = full_response['result']
        for row in range(len(result)):
            final_result = result[row]

    else:
        error = full_response['error']
        print (error['code'])
        print(error['description'])

    # git teste


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
    output = {}
    tickers = ["JNJ", "BRK-B", "JPM", "MMM", "ABBV", "DIS", "T", "PG", "LOW", "CI"]
    #tickers = ["JNJ"]
    fields = ["Operating Income", "Net Income from Continuing Operations", "Retained Earnings", "Changes in Cash", "Net Borrowings"]

    options = Options()
    options.add_argument("--headless")
    with webdriver.Firefox(options=options) as driver:
        driver.implicitly_wait(10)
        scraper = scrapYahoo(driver, tickers, fields)
        scraper.scrap_data()
        scraper.generate_CSV(outFile = 'output7.csv')
#    scraper.get_page(scraper.tickers[0])
#    scraper.set_quarterly()
#    elements = scraper.get_field_row_values(scraper.fields[0])
#TODO format result as expected from Belo