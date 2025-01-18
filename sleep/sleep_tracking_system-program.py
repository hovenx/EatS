import streamlit as st
import datetime
import json
import os

st.set_page_config(page_title = "EatS' Sleep Tracker")

st.subheader("Welcome to the EatS' Sleep Tracker. Here we'll help you fix your body clock for better health.")
st.title("EatS")
# Define the folder path where you want to save the JSON file
folder_path = "Stored Data" 

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

try:
    with open(os.path.join(folder_path, "sleep_data.json"), "r") as f:
        sleep_data = json.load(f)
except FileNotFoundError:
    sleep_data = []

target_hours = float(input("Enter your target hours of sleep: "))

for _ in range(2):
    today = datetime.date.today()

    try:
        actual_hours = float(input(f"Enter the number of hours you slept yesterday ({today}): "))
        if actual_hours < 0 or actual_hours > 24:
            raise ValueError("Invalid input. Please enter a number between 0 and 24.")

        if actual_hours < target_hours:
            sleep_status = "Underslept"
        elif actual_hours > target_hours:
            sleep_status = "Overslept"
        else:
            sleep_status = "Adequate"

        sleep_data.append({
            "date": today.strftime("%Y-%m-%d"),
            "hours": actual_hours,
            "status": sleep_status
        })

        print(f"You slept for {actual_hours} hours on {today}.")
        print(f"Sleep Status: {sleep_status}")

    except ValueError as e:
        print(e)

with open(os.path.join(folder_path, "sleep_data.json"), "w") as f:
    json.dump(sleep_data, f, indent=4)

print("\nCome back tomorrow to track your sleep again.")

# Ask user if they want to display logs
display_logs = input("Do you want to view your sleep logs? (y/n): ").lower()

if display_logs == 'y':
    print("\nYour Sleep Logs:")
    for entry in sleep_data:
        print(f"{entry['date']}: {entry['hours']} hours ({entry['status']})") 
