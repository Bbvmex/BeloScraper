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

