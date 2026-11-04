import streamlit as st
import fastf1

schedule = fastf1.get_event_schedule(2026) #caricamento del calendario della stagione 2026
st.set_page_config(layout="wide")

st.title("Calendario della stagione 2026")

st.dataframe(schedule)

#st.write(schedule.columns)