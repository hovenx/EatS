######################################
#                                    #
##        EatS: Sleep Tracker       ##
#                                    #
######################################
# Imports the modules
import streamlit as st
import datetime
import json
import os
import pandas as pd

# Page Title
st.title("Sleep Tracker")
st.subheader("Welcome to the EatS' Sleep Tracker. Here we'll help you fix your body clock for better health.")

# Defines the folder path
folder_path = "Stored Data"
if not os.path.exists(folder_path):
  os.makedirs(folder_path)

# Loads the sleep data from JSON
try:
  with open(os.path.join(folder_path, "sleep_data.json"), "r") as f:
    sleep_data = json.load(f)
except FileNotFoundError:
  sleep_data = []

# Allow user to select the sleep type (Nap or Night)
sleep_type = st.radio("Select Sleep Type:", ("Nap", "Sleep"))

# Get target sleep hours based on selected type
if sleep_type == "Nap":
  target_hours = st.number_input("Enter your target nap hours (hours):", min_value=0, max_value = 5, step=1, key="target_hours_nap_input")
  target_minutes = st.number_input("Enter your target nap minutes:", min_value=0, max_value=59, step=1, key="target_minutes_nap_input")
elif sleep_type == "Sleep":
  target_hours = st.number_input("Enter your target night sleep hours (hours):", min_value=0, max_value = 24, step=1, key="target_hours_night_input")
  target_minutes = st.number_input("Enter your target night sleep minutes:", min_value=0, max_value=59, step=1, key="target_minutes_night_input")

if target_hours or target_minutes:  # Proceed if either target is entered
  for i in range(1):  # Collects data for two days
    today = datetime.date.today()
    formatted_today = today.strftime("%B %d, %Y")

    actual_hours = st.number_input(f"Enter your {sleep_type.lower()} hours yesterday ({formatted_today}) (hours):",
                                   min_value=0, step=1, key=f"actual_hours_{sleep_type.lower()}_input_{today}_{i}")
    actual_minutes = st.number_input(f"Enter your {sleep_type.lower()} minutes yesterday ({formatted_today}) (minutes):",
                                     min_value=0, max_value=59, step=1, key=f"actual_minutes_{sleep_type.lower()}_input_{today}_{i}")

    # Format actual_hours with leading zero
    formatted_actual_hours = f"{actual_hours:02d}" 

    # Calculate total sleep time in hours (with decimal for minutes)
    total_sleep_hours = actual_hours + actual_minutes / 60 if actual_hours is not None and actual_minutes is not None else None

    # Calculate target sleep time in hours
    target_sleep_hours = target_hours + target_minutes / 60 if target_hours is not None and target_minutes is not None else None

    if total_sleep_hours is not None:
      if total_sleep_hours < target_sleep_hours:
        sleep_status = "Underslept"
      elif total_sleep_hours > target_sleep_hours:
        sleep_status = "Overslept"
      else:
        sleep_status = "Adequate"

      sleep_data.append({
          "date": formatted_today,
          f"{sleep_type.lower()}_hours": int(total_sleep_hours) if total_sleep_hours is not None else None,
          f"{sleep_type.lower()}_status": sleep_status if total_sleep_hours is not None else None
      })

      st.write(f"Your {sleep_type.lower()} yesterday: {formatted_actual_hours} hours and {actual_minutes} minutes ({sleep_status})")
      
# Display sleep logs in a table
  if st.button("View Sleep Logs"):
    st.write("\nYour Sleep Logs:")
    if sleep_data:  # Check if there's any data to display
      df = pd.DataFrame(sleep_data)
      st.table(df)
      # Create a line chart (if data exists)
      if f"{sleep_type.lower()}_hours" in df.columns and not df[f"{sleep_type.lower()}_hours"].isnull().all():
        st.markdown(f"## {sleep_type} Hours Over Time") 
        st.line_chart(df, x='date', y=f"{sleep_type.lower()}_hours") 
    else:
      st.write("No sleep data available.")
  # Write sleep data to JSON file after the loop
  with open(os.path.join(folder_path, "sleep_data.json"), "w") as f:
    json.dump(sleep_data, f, indent=4)

  st.write("\nCome back tomorrow to track your sleep again.")

# Text navigation to other pages
st.page_link("food/food.py", label="Go to the Food Tracker", icon=":material/restaurant:")
st.page_link("bmi.py", label="Go to the BMI Tracker", icon=":material/scale:")
