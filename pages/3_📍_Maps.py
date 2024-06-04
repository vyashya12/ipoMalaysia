import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
from urllib.parse import quote
import requests
from requests.structures import CaseInsensitiveDict



st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

def encode_address(address):
    stringed = str(address)
    return quote(stringed)

file = "./data/AllCompanyDataLatest.csv"
df = load_data()
df["encoded_address2"] = df["address2"].apply(encode_address)
print(df['encoded_address2'])
print(df['encoded_address2'][0])

url = "https://api.geoapify.com/v1/geocode/search?text=${n}&apiKey=60eb608d479f4216ae04f1e325d1ab2f".format(n=df['encoded_address2'][0])

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.json)

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

m = leafmap.Map(center=[40, -100], zoom=4)
cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

m.add_geojson(regions, layer_name='US Regions')
m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    color_column='region',
    icon_names=['gear', 'map', 'leaf', 'globe'],
    spin=True,
    add_legend=True,
)
        
m.to_streamlit(height=700)
