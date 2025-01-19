iimport streamlit as st
import datetime
import json
import os
import pandas as pd

st.set_page_config(page_title="BMI Tracker")

st.title("BMI Tracker and Weight Progress")

#Initialize data storage
data_file = "bmi_data.json"
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        data = json.load(f)
else:
    data = []


def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.0, step=0.01)
today = datetime.date.today().strftime("%Y-%m-%d")

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

        # BMI Suggestions
        if bmi_category == "Underweight":
            st.write("Suggestions: Consider increasing your calorie intake and consulting a doctor or nutritionist.")
        elif bmi_category == "Overweight" or bmi_category == "Obese":
            st.write("Suggestions: Focus on a balanced diet, regular exercise, and consult a doctor or nutritionist.")
        else:
            st.write("Suggestions: Maintain a healthy lifestyle with balanced diet and regular exercise.")

        # Display weight progress
        if len(data) > 1:
            df = pd.DataFrame(data)
            st.line_chart(df, x="date", y="weight")
            st.write("Weight Progress")
    else:
        st.write("Please enter valid weight and height.")


# Display BMI logs
if st.button("View BMI Logs"):
    st.write("BMI Logs:")
    if data:
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.write("No data available.")
