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

@st.cache_data
def load_data2():
    df = pd.read_csv(file2)
    return df

def encode_address(address):
    stringed = str(address)
    return quote(stringed)

file = "./data/AllCompanyDataLatest.csv"
file2 = "./data/CompanyWithLongLat.csv"
df = load_data()
df2 = load_data2()

# df["encoded_address2"] = df["address2"].apply(encode_address)
# print(df['encoded_address2'])
# print(df['encoded_address2'][0])

# url = "https://api.geoapify.com/v1/geocode/search?text=${n}&apiKey=60eb608d479f4216ae04f1e325d1ab2f".format(n=df2['encoded_address2'][0])

# headers = CaseInsensitiveDict()
# headers["Accept"] = "application/json"

# resp = requests.get(url, headers=headers)

# json_resp = resp.json()

# longitude = json_resp["features"][0]["geometry"]["coordinates"][0]
# latitude = json_resp["features"][0]["geometry"]["coordinates"][1]
# data1 = [[longitude, latitude]]
# df2 = pd.DataFrame(data1, columns=['Longitude', 'Latitude'])

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("Maps")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

csv_file1 = "CompanyWithLongLat.csv"

df_cleaned = leafmap.csv_to_df(csv_file1)

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[4, -100], zoom=6)
        in_shp = "https://github.com/opengeos/leafmap/raw/master/examples/data/countries.zip"
        m.add_shp(in_shp, "Countries")
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        my_cities= "../data/MalaysiaCities.csv"
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

        m.add_geojson(regions, layer_name='Malaysia Regions')
        m.add_xy_data(
            df_cleaned,
            x="longitude",
            y="latitude",
            # color_column='region',
            # icon_names=['gear', 'map', 'leaf', 'globe'],
            # spin=True,
            # add_legend=True,
        )
        
m.to_streamlit(height=700)
