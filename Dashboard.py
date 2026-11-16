import fastf1
import streamlit as st

schedule = fastf1.get_event_schedule(2026) #caricamento del calendario della stagione 2026
st.set_page_config(layout="wide")

st.title("Calendario della stagione 2026")

st.dataframe(schedule)

scelta = st.text_input("Scegli una data")