import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import streamlit_pandas as sp


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

st.set_page_config(layout="wide", page_title="Exabytes Target Database", page_icon="./exabytes.svg")

# Customize page title
st.title("Companies Data Hub")

st.markdown(
    """
    This hub contains data on all the public listed companies in Malaysia
    """
)

st.header("Instructions")

markdown = """
1. Enjoy collecting data on all the public listed companies of Malaysia
2. Search for a company that you are interested in and select it to view details
3. The companies are displayed in a random order below, please use the filter
4. The table underneath has the columns, revenueGrowth, sector, industry, website and revenue
"""

st.markdown(markdown)

st.markdown("***")

file = "./data/AllCompanyDataLatest.csv"
df = load_data()

create_data = {"longName": "multiselect",
                "city": "multiselect",
                "sector": "multiselect",
                }

all_widgets = sp.create_widgets(df, create_data, ignore_columns=["address1", "industry", "regularMarketOpen", "fullTimeEmployees", "CompanyExecutives", "totalRevenue", "totalRevenueInt", "address2", "zip", "country", "phone", "fax", "website", "longBusinessSummary", "companyOfficers", "compensationAsOfEpochDate", "maxAge", "priceHint", "beta", "previousClose", "open", "dayLow", "dayHigh", "regularMarketPreviousClose", "regularMarketDayLow", "regularMarketDayHigh", "dividendRate", "dividendYield", "exDividendDate", "payoutRatio", "fiveYearAvgDividendYield", "forwardPE", "volume", "regularMarketVolume", "averageVolume", "averageVolume10days", "averageDailyVolume10Day", "bid", "ask","marketCap","fiftyTwoWeekLow","fiftyTwoWeekHigh","priceToSalesTrailing12Months","fiftyDayAverage","twoHundredDayAverage","trailingAnnualDividendRate","trailingAnnualDividendYield","currency","enterpriseValue","profitMargins","floatShares","sharesOutstanding","heldPercentInsiders","heldPercentInstitutions","bookValue","priceToBook","lastFiscalYearEnd", "nextFiscalYearEnd","mostRecentQuarter","earningsQuarterlyGrowth","netIncomeToCommon","trailingEps","forwardEps","pegRatio","enterpriseToRevenue","enterpriseToEbitda","exchange","quoteType","symbol","underlyingSymbol","shortName","firstTradeDateEpochUtc","timeZoneFullName","timeZoneShortName","uuid","gmtOffSetMilliseconds","currentPrice","targetHighPrice","targetLowPrice","targetMeanPrice","targetMedianPrice","recommendationMean","recommendationKey","numberOfAnalystOpinions","totalCash","totalCashPerShare","ebitda","totalDebt","quickRatio","currentRatio","debtToEquity","revenuePerShare","returnOnAssets","returnOnEquity","freeCashflow","operatingCashflow","earningsGrowth","revenueGrowth" ,"grossMargins" , "ebitdaMargins" ,"operatingMargins" ,"financialCurrency" ,"trailingPegRatio"])

cols_to_move = ['longName', 'sector', 'industry', 'city']

all_columns = cols_to_move + [col for col in df.columns if col not in cols_to_move]

df = df.reindex(columns=all_columns)

res = sp.filter_df(df, all_widgets)

# st.write(df)

# mongodb+srv://vyashya:vyashya12@ipodb.gfm7e1m.mongodb.net/?retryWrites=true&w=majority&appName=IPODB


st.write(res)