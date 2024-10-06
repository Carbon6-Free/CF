from firebase import firebase
import streamlit as st
from lib.crawler_module import *
from lib.network_carborn import *
import re
from PIL import Image
import os
import pickle
from style import set_style
from info import display_random_info, carbon_info
import json
from lib.graph import *
from dotenv import load_dotenv

with open('carbonfree.json') as f:
    data = json.load(f)

load_dotenv()

API_KEY=os.getenv("firebasekey")
firebase=firebase.FirebaseApplication(API_KEY, None)
with open("./cutoff.txt", 'rb') as lf:
    cutoff = pickle.load(lf)



# Apply the style settings
set_style()

# Search term input text box
search_query = st.text_input(label='url', value='')  # Entered URL address

# Display the random information
display_random_info()

# Change dataframe
data = preprocess_data(data)
df = pd.DataFrame([(website, detail_id, detail_data['css'], detail_data['fetch'], detail_data['g of CO2'], detail_data['img'], detail_data['link'], detail_data['script'], detail_data['video']) 
                   for website, details in data.items() 
                   for detail_id, detail_data in details.items()], 
                  columns=['Website', 'Detail ID', 'CSS', 'Fetch', 'CO2', 'Img', 'Link', 'Script', 'Video'])

df = df[df['CO2'] != 0]
sorted_df = df.sort_values(by='CO2')
datasets = convert_carbon_bound(sorted_df)

tier = ""
carbon_g = 0

# View results button
if st.button("View results"):
    log, datasize = get_json_data(search_query)
    carbon_g = annual_carborn(log[-1]["Size"])
    # Storing and retrieving data in Firebase
    match = re.search(r'(?<=://)(.*?)(?=/|$)', search_query)  # 도메인 이름 추출을 위한 정규표현식
    if match:
        domain = match.group(1)  # 도메인 이름 추출
        modified_domain = domain.replace(".", "-")  # '.'을 '-'로 변경
        print(modified_domain)

    firebase.post(f'{modified_domain}/', datasize)

    if carbon_g <= cutoff[0]:
        image = Image.open('./assets/A+.png')
        tier = "A+"
    elif carbon_g <= cutoff[1]:
        image = Image.open('./assets/A.png')
        tier = "A"
    elif carbon_g <= cutoff[2]:
        image = Image.open('./assets/B.png')
        tier = "B"
    elif carbon_g <= cutoff[3]:
        image = Image.open('./assets/C.png')
        tier = "C"
    elif carbon_g <= cutoff[4]:
        image = Image.open('./assets/D.png')
        tier = "D"
    else:
        image = Image.open('./assets/F.png')
        tier = "F"

    st.write("링크를 한번 방문할떄마다 " , carbon_g, "g의 탄소가 발생합니다.")

    

    carbon_info(carbon_g * 10)
    st.image(image, width=200)

    if datasize:
        plot_comparison(datasets, datasize, search_query, tier)
