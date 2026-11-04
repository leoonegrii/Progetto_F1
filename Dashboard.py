import streamlit as st
import fastf1

schedule = fastf1.get_event_schedule(2026)
st.write("Ciao mondo questa è una dashboard per le sessioni telemetriche di F1")
st.write(schedule)
print()
st.write(schedule.columns)