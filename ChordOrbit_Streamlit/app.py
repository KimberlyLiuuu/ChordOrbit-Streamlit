from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="和弦星图",
    page_icon="🎹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      header[data-testid="stHeader"] { background: transparent; }
      .stApp { background: #080b13; }
      .block-container { max-width: none; padding: 0; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("chord_orbit.html")
components.html(html_path.read_text(encoding="utf-8"), height=980, scrolling=True)
