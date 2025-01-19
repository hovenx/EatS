import streamlit as st
import datetime
import json
import os
import pandas as pd

st.subheader("Welcome to EatS! Track your food and calories.")
st.title("EatS' Food and Calorie Tracker")

folder_path = "Stored Data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

try:
    with open(os.path.join(folder_path, "bmi_data.json"), "r") as f:
        bmi_data = json.load(f)
except FileNotFoundError:
    bmi_data = []


today = datetime.date.today()
formatted_today = today.strftime("%B %d, %Y")

weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.0, step=0.01)


if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

        # Store data
        data.append({
            "date": today,
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": bmi_category
        })

        with open(data_file, "w") as f:
            json.dump(data, f, indent=4)

        st.write(f"Your BMI is: {bmi:.2f} ({bmi_category})")


if st.button("View BMI Logs"):
    st.write("BMI Logs:")
    if data:
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.write("No data available.")
