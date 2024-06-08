from firebase import firebase
import streamlit as st
from lib.crawler_module import *
from lib.network_carborn import *
import re
from PIL import Image
import os
import pickle
from style import set_style
from info import display_random_info



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

# View results button
if st.button("View results"):
    log, datasize = get_json_data(search_query)
    datasize["g of CO2"] = annual_carborn(log[-1]["Size"])
    # Storing and retrieving data in Firebase
    match = re.search(r'(?<=://)(.*?)(?=/|$)', search_query)  # 도메인 이름 추출을 위한 정규표현식
    if match:
        domain = match.group(1)  # 도메인 이름 추출
        modified_domain = domain.replace(".", "-")  # '.'을 '-'로 변경
        print(modified_domain)

    firebase.post(f'{modified_domain}/', datasize)
    #result = firebase.get(f'/{modified_domain}', '')

    if datasize["g of CO2"] <= cutoff[0]:
        image = Image.open('./assets/A+.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " , datasize["g of CO2"])
    elif datasize["g of CO2"] <= cutoff[1]:
        image = Image.open('./assets/A.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " ,datasize["g of CO2"])
    elif datasize["g of CO2"] <= cutoff[2]:
        image = Image.open('./assets/B.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " ,datasize["g of CO2"])
    elif datasize["g of CO2"] <= cutoff[3]:
        image = Image.open('./assets/C.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " ,datasize["g of CO2"])
    elif datasize["g of CO2"] <= cutoff[4]:
        image = Image.open('./assets/D.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " ,datasize["g of CO2"])
    else:
        image = Image.open('./assets/F.png')
        resized_image = image.resize((100, 100))
        st.image(resized_image, use_column_width=True)
        st.write("g of CO2: " ,datasize["g of CO2"])

    if datasize:
        visualize_data(datasize)