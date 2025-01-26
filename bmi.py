import streamlit as st
import pandas as pd
import os

# Initialize the dataframe if it doesn't exist
if not os.path.exists("bmi_data.csv"):
    df = pd.DataFrame(columns=["Date", "Weight (kg)", "Height (cm)", "BMI", "Classification", "Suggestion"])
    df.to_csv("bmi_data.csv", index=False)

def calculate_bmi(weight, height):
    """Calculates BMI given weight and height."""
    try:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Invalid Input"
    except Exception as e:  # Catch any other unexpected error
        return f"Error: {e}"

def get_bmi_classification(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider increasing your calorie intake and consult a nutritionist or doctor."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Maintain a balanced diet and regular exercise."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Focus on a healthy diet, regular exercise, and consider consulting a healthcare professional."
    else:
        return "Obese", "Consult a doctor or a registered dietitian to develop a weight loss plan. Consider a combination of diet, exercise, and potentially medication."

st.title("BMI Tracker")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi}")

    classification, suggestion = get_bmi_classification(bmi)
    st.write(f"Classification: {classification}")
    st.write(f"Suggestion: {suggestion}")


    # Log the data in a dataframe
    new_data = {"Date": pd.Timestamp.now().strftime("%Y-%m-%d"),
                "Weight (kg)": weight,
                "Height (cm)": height,
                "BMI": bmi,
                "Classification": classification,
                "Suggestion": suggestion}

    df = pd.read_csv("bmi_data.csv")
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("bmi_data.csv", index=False)
    st.success("BMI logged successfully!")

# Display existing logs
if os.path.exists("bmi_data.csv"):
    st.subheader("BMI History")
    df = pd.read_csv("bmi_data.csv")
    st.dataframe(df)
else:
    st.info("No BMI data available.")
