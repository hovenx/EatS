import streamlit as st
from streamlit_option_menu import option_menu 

st.set_page_config(page_title="EatS", page_icon = ":material/fitness_center:")

selected = option_menu(
    menu_title = None,
    options=["Home", "Food Tracker", "BMI Tracker", "Sleep Tracker"],
    orientation="Horizontal",
)

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

bmi_track = st.Page(
    page="bmi.py",
    title="BMI Tracker",
    icon=":material/scale:",
)

#--------- NAVIGATION SETUP ---------
pg = st.navigation(
    {
        "Information": [about_us],
        "Services": [food_track, sleep_track, bmi_track],
    }
)

pg.run()

