import streamlit as st
import datetime
import json
import os
import pandas as pd

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

        # BMI Suggestions
        if bmi_category == "Underweight":
            st.write("Suggestions: ")
            st.write("Consider increasing your calorie intake and consulting a doctor or nutritionist.")
            st.write("For extra calories, add extras to your meals, like nut butter on whole-grain bread or cheese in casseroles. For more calories and protein, you can also add liquid or dry milk to food. Soups and mashed potatoes are two examples.")
            st.write("Start eating five to six smaller meals throughout the day gradually. To identify when you might be hungry, try to pay attention to your body. Even if you're not really hungry, you might need to schedule mealtimes.")
            st.wirte("Drinks have the power to fill you up. If it applies to you, refrain from drinking right before or during meals. However, be sure to consume adequate amounts of liquids throughout the day.")
            st.write("By increasing your muscle mass, exercise—especially strength training—can aid in weight growth. Additionally, exercise may increase your hunger.")
        elif bmi_category == "Overweight" or bmi_category == "Obese":
            st.write("Suggestions: ")
            st.write("Sports drinks, soda, juice, and sweet tea are examples of sugary beverages that have little to no nutritional benefit and add extra calories. Overweight is more common among those who use sugary drinks on a daily basis. Most of the time, go for water or low-fat milk.")
            st.write("Frequent exercise helps you look and feel good and can help you lose weight since it burns calories and builds muscle. Cycling to school, walking the family dog, and engaging in other activities that boost your daily activity level can have an impact. Increase the intensity of your workout and incorporate some muscle-building strength exercises if you want to burn more calories.")
            st.write("The likelihood of being overweight is higher for those who spend a lot of time in front of screens. Limit how much time you spend on non-school-related activities on computers, phones, and tablets, as well as how much time you spend playing video games and watching TV. For a better night's sleep, turn off all screens at least an hour before bed.")
            st.write("Large servings add up extra calories, which can lead to weight gain. Pick smaller servings, particularly when consuming high-calorie snacks. Try splitting an entree or bringing half of your meal home with you when dining out.")
            st.write("There is more to fruits and vegetables than just vitamins and minerals. They also fill you up since they are high in fiber. Additionally, you're less prone to overeat when you consume a lot of fruits and vegetables.")
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
