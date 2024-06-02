import streamlit as st

def set_style():
    # Initialize session state for background color
    if 'bg_color' not in st.session_state:
        st.session_state['bg_color'] = '#000000'  # Initial background color is black
    if 'text_color' not in st.session_state:
        st.session_state['text_color'] = '#FFFFFF'  # Initial text color is white

    # Background color selection toggle
    if st.checkbox('White Background', key='bg_checkbox'):
        st.session_state['bg_color'] = '#FFFFFF'
        st.session_state['text_color'] = '#000000'
    else:
        st.session_state['bg_color'] = '#000000'
        st.session_state['text_color'] = '#FFFFFF'

    # Apply background color and additional styles using CSS
    st.markdown(
        f"""
        <style>
            :root {{
                --bg-color: {st.session_state['bg_color']};
                --text-color: {st.session_state['text_color']};
                --button-bg-color: {'#000000' if st.session_state['bg_color'] == '#FFFFFF' else '#FFFFFF'};
                --button-text-color: {st.session_state['bg_color']};
            }}
            .stApp {{
                background-color: var(--bg-color);
                color: var(--text-color);
            }}
            .fixed-bottom-right {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: var(--bg_color);
                color: var(--text_color);
                border: 2px solid var(--text_color);
                padding: 10px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
                width: 300px;
            }}
            label, .st-c3, .st-c4 {{
                color: var(--text-color) !important;
            }}
            .stTextInput>div>div>input {{
                color: var(--text-color) !important;
            }}
            .stButton>button {{
                background-color: var(--button-bg-color) !important;
                color: var(--button-text-color) !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page title
    st.markdown(
        f"<h1 style='color:{st.session_state['text_color']}'>CarbonFree</h1>", unsafe_allow_html=True
    )
