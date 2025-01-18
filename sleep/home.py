import streamlit as st

st.title("EatS")

#--------- PAGE SETUP ---------
sleep_track = st.Page(
    page = "Sleep Tracker/app.py",
    title = "Sleep Tracker",
    icon = ":material/bedtime:",
    default=True,
)

#--------- NAVIGATION SETUP ---------
pg = st.navigation(pages=[sleep_track])
