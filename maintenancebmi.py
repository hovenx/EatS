import streamlit as st
import datetime
import json
import os
import pandas as pd


st.set_page_config(page_title="EatS' Food & Calorie Tracker")

st.subheader("Welcome to EatS! Track your food and calories.")
st.title("EatS")

# Define the folder path
folder_path = "Stored Data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Load food data from JSON
try:
    with open(os.path.join(folder_path, "food_data.json"), "r") as f:
        food_data = json.load(f)
except FileNotFoundError:
    food_data = []

today = datetime.date.today()
formatted_today = today.strftime("%B %d, %Y")

food_item = st.text_input("Enter food item:")
calories = st.number_input("Enter calories:", min_value=0)


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


st.set_page_config(page_title="BMI Tracker")

st.title("BMI Tracker and Weight Progress")

# Initialize data storage
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

        # BMI Suggestions (Improved)
        if bmi_category == "Underweight":
            st.write("Suggestions: Increase calorie intake and consult a doctor or nutritionist.")
        elif bmi_category == "Overweight" or bmi_category == "Obese":
            st.write("Suggestions: Reduce calorie intake, increase physical activity, and consult a doctor or nutritionist.")
        else:
            st.write("Suggestions: Maintain a healthy lifestyle with balanced diet and regular exercise.")
            
        #Detailed suggestions based on category
        if bmi_category == "Underweight":
            st.write("Tips: Consider increasing your calorie intake and consulting a doctor or nutritionist. Add extras to your meals, like nut butter on whole-grain bread.")
        elif bmi_category == "Overweight" or bmi_category == "Obese":
            st.write("Tips: Reduce sugary drinks, increase exercise, limit screen time, and choose smaller portions. Prioritize fruits, vegetables, and lean protein.")


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
