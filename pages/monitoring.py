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

# CPU 도넛 차트
cpu_fig = go.Figure(go.Pie(
    values=[20, 80],
    hole=0.6,
    marker=dict(colors=['#FF6361', 'rgba(0,0,0,0)'])  # 나머지 부분을 투명하게 설정
))
cpu_fig.update_layout(
    showlegend=False,
    annotations=[dict(text='CPU', x=0.5, y=0.5, font_size=20, showarrow=False)],
    width=300, 
    height=300
)

# GPU 도넛 차트
gpu_fig = go.Figure(go.Pie(
    values=[40, 60],
    hole=0.6,
    marker=dict(colors=['#FFA600', 'rgba(0,0,0,0)'])  # 나머지 부분을 투명하게 설정
))
gpu_fig.update_layout(
    showlegend=False,
    annotations=[dict(text='GPU', x=0.5, y=0.5, font_size=20, showarrow=False)],
    width=300, 
    height=300
)

# 도넛차트 추가
# Streamlit에 양옆 배치
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(cpu_fig)

with col2:
    st.plotly_chart(gpu_fig)