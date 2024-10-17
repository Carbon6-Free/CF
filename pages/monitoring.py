import streamlit as st
from lib.crawler_module import *
from lib.network_carborn import *
from lib.graph import *
from carbon_track import CarbonTrack

image_path = "./pic/multipc.png"
ct = CarbonTrack('cocl-pm-firebase.json', 'https://cocl-pm-default-rtdb.firebaseio.com/', 'True')
ct.collect()

log = ct.getdata()
n_pcs = len(log)

max_cols = 3
n_rows = (n_pcs + max_cols - 1) // max_cols

st.title("Tracking dashboard")

for idx, (pc_id, pc_data) in enumerate(log.items()):
    mem = round(pc_data['memory_usage'] * 100)
    pwr = round(pc_data['power_usage'] * 100)

    mem_fig = go.Figure(go.Pie(
        values=[mem, 100-mem],
        hole=0.6,
        marker=dict(colors=['#FF6361', 'rgba(0,0,0,0)'])
    ))
    mem_fig.update_layout(
        showlegend=False,
        annotations=[dict(text='Memory', x=0.5, y=0.5, font_size=20, showarrow=False)],
        width=300, 
        height=300
    )

    pwr_fig = go.Figure(go.Pie(
        values=[pwr, 100-pwr],
        hole=0.6,
        marker=dict(colors=['#FFA600', 'rgba(0,0,0,0)'])
    ))
    pwr_fig.update_layout(
        showlegend=False,
        annotations=[dict(text='Power', x=0.5, y=0.5, font_size=20, showarrow=False)],
        width=300, 
        height=300
    )

    col1, col2, col3 = st.columns(3)  # (이미지, 메모리, 전력)
    
    with col1:
        st.image(image_path, caption=f"PC {idx+1}", use_column_width=True)

    with col2:
        st.plotly_chart(mem_fig)

    with col3:
        st.plotly_chart(pwr_fig)
