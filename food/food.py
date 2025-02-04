############################################
#                                          #
##      EatS: Food and Calorie Tracker    ##
#                                          #
############################################
# Imports the important modules
import streamlit as st
import datetime
import json
import os
import pandas as pd

# Title Page
st.title("EatS' Food and Calorie Tracker")
st.subheader("Welcome to EatS! Track your food and calories.")

# Defines the folder path
folder_path = "Stored Data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loads the food data from JSON
try:
    with open(os.path.join(folder_path, "food_data.json"), "r") as f:
        food_data = json.load(f)
except FileNotFoundError:
    food_data = []

# Sets the date and time to real-time
today = datetime.date.today()
formatted_today = today.strftime("%B %d, %Y")

# Food and Calorie Input
food_item = st.text_input("Enter food item:")
calories = st.number_input("Enter calories:", min_value=0)

# Condition to see if input is valid 
if st.button("Log Food"):
    if food_item and calories:
        food_data.append({
            "date": formatted_today,
            "food": food_item,
            "calories": calories
        })

        with open(os.path.join(folder_path, "food_data.json"), "w") as f:
            json.dump(food_data, f, indent=4)

        st.success(f"Logged {food_item} ({calories} calories) for {formatted_today}")
    else:
        st.warning("Please enter both food item and calories.")


# Display food logs
if st.button("View Food Logs"):
    st.write("\nYour Food Logs:")
    if food_data:
        df = pd.DataFrame(food_data)
        st.table(df)
    else:
        st.write("No food data available.")

# Text Navigation to other pages
st.page_link("sleep/app.py", label="Go to the Sleep Tracker", icon=":material/bedtime:")
st.page_link("bmi.py", label="Go to the BMI Tracker", icon=":material/scale:")
