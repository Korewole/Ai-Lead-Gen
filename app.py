import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("🚀 AI Lead Gen Command Center")

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

st.subheader("Current Leads")
st.dataframe(df)

if st.button("Start AI Research Loop"):
    st.info("AI Agents are now researching companies in your sheet...")
    # This is where you will call your CrewAI logic (see step 5)
    st.success("Research Complete! Check your Google Sheet.")
