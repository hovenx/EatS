#########################################
#                                       #
##           EatS: HOMEPAGE            ##
#                                       #
#########################################
# Imports the streamlit module
import streamlit as st

# Sets the page title (displays on browser tab)
st.set_page_config(page_title="EatS", page_icon = ":material/fitness_center:")

# Page Setup - Sets each page directory
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

# Setting the navigation tab 
pg = st.navigation(
    {
        "Information": [about_us],
        "Services": [food_track, sleep_track, bmi_track],
    }
)

pg.run()

