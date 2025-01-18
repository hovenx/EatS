import streamlit as st

st.set_page_config(page_title="EatS", page_icon = ":material/fitness_center:")

#--------- PAGE SETUP ---------
about_us = st.Page(
    page = "aboutus.py",
    title = "About Us",
    icon = ":material/diversity_3:",
    default = True,
)

sleep_track = st.Page(
    page = "sleep/app.py",
    title = "Sleep Tracker",
    icon = ":material/bedtime:",
)

food_track = st.Page(
    page="food/food.py",
    title="Food Tracker",
    icon=":material/restaurant:",
)

#--------- NAVIGATION SETUP ---------
pg = st.navigation(
    {
        "Information": [about_us],
        "Services": [sleep_track, food_track],
    }
)

pg.run()

