import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

st.title("Company Data Charts")


markdown = """
    Charts that use the companies data 
"""

st.markdown(markdown)

file = "./data/AllCompanyDataLatest.csv"
df = load_data()
sector_counts = df['sector'].value_counts()

# Creating lists for sectors and number of companies
sectors = sector_counts.index.tolist()
number_of_companies = sector_counts.values.tolist()
data = list(zip(sectors, number_of_companies))
df_sectors = pd.DataFrame(data, columns=['Sectors', 'Number_of_companies'])

st.markdown("<div style='text-align: center; margin-bottom: 20px;'>Sectors and the Number of Companies</div>", unsafe_allow_html=True)

st.area_chart(df_sectors, x="Sectors", y="Number_of_companies")

st.bar_chart(df_sectors, x="Sectors", y="Number_of_companies")

df['totalRevenueInt'] = df['totalRevenueInt'].replace(',', '')

# Group by 'sector' and sum the 'totalRevenueInt'
sector_revenue_sum = df.groupby('sector')['totalRevenueInt'].sum().reset_index()

# Rename the columns for clarity
sector_revenue_sum.columns = ['Sectors', 'Total_Revenue']

# Display the DataFrame in Streamlit
st.markdown("<div style='text-align: center; margin-bottom: 20px;'>Sectors and the total amount of Revenue</div>", unsafe_allow_html=True)

st.area_chart(sector_revenue_sum, x="Sectors", y="Total_Revenue")

st.bar_chart(sector_revenue_sum, x="Sectors", y="Total_Revenue")


