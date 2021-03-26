import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(page_title="Streamlit Getting Started Guide", initial_sidebar_state="expanded")

state = st.get_state()

options = ("🏃‍♀️Getting Started",
    "⬇️ Installing Streamlit",
    "🏗 Basic Functions",
    "🎨 Layout and Themes",
    "🏎 App Performance",
    "🚀 Deploying your App",
    "🎈 More Resources")

nav = st.sidebar.selectbox("Choose a section", options, key="nav")

def on_next_click():
    state.nav = options[options.index(state.nav) + 1]

