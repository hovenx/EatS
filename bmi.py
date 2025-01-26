import streamlit as st
import pandas as pd
import os

# Initialize the dataframe if it doesn't exist
if not os.path.exists("bmi_data.csv"):
    df = pd.DataFrame(columns=["Date", "Weight (kg)", "Height (cm)", "BMI"])
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


st.title("BMI Tracker")


# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi}")

    # Log the data in a dataframe
    new_data = {"Date": pd.Timestamp.now().strftime("%Y-%m-%d"),
                "Weight (kg)": weight,
                "Height (cm)": height,
                "BMI": bmi}

    df = pd.read_csv("bmi_data.csv")
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("bmi_data.csv", index=False)
    st.success("BMI logged successfully!")
    
if bmi < 18.5:
    st.write("Suggestions (Underweight): ")
    st.write("Consider increasing your calorie intake and consulting a doctor or nutritionist.")
    st.write("For extra calories, add extras to your meals, like nut butter on whole-grain bread or cheese in casseroles. For more calories and protein, you can also add liquid or dry milk to food. Soups and mashed potatoes are two examples.")
    st.write("Start eating five to six smaller meals throughout the day gradually. To identify when you might be hungry, try to pay attention to your body. Even if you're not really hungry, you might need to schedule mealtimes.")
    st.write("Drinks have the power to fill you up. If it applies to you, refrain from drinking right before or during meals. However, be sure to consume adequate amounts of liquids throughout the day.")
    st.write("By increasing your muscle mass, exercise—especially strength training—can aid in weight growth. Additionally, exercise may increase your hunger.")
elif bmi >= 25.0:
    st.write("Suggestions (Overweight/Obese): ")
    st.write("Sports drinks, soda, juice, and sweet tea are examples of sugary beverages that have little to no nutritional benefit and add extra calories. Overweight is more common among those who use sugary drinks on a daily basis. Most of the time, go for water or low-fat milk.")
    st.write("Frequent exercise helps you look and feel good and can help you lose weight since it burns calories and builds muscle. Cycling to school, walking the family dog, and engaging in other activities that boost your daily activity level can have an impact. Increase the intensity of your workout and incorporate some muscle-building strength exercises if you want to burn more calories.")
    st.write("The likelihood of being overweight is higher for those who spend a lot of time in front of screens. Limit how much time you spend on non-school-related activities on computers, phones, and tablets, as well as how much time you spend playing video games and watching TV. For a better night's sleep, turn off all screens at least an hour before bed.")
    st.write("Large servings add up extra calories, which can lead to weight gain. Pick smaller servings, particularly when consuming high-calorie snacks. Try splitting an entree or bringing half of your meal home with you when dining out.")
    st.write("There is more to fruits and vegetables than just vitamins and minerals. They also fill you up since they are high in fiber. Additionally, you're less prone to overeat when you consume a lot of fruits and vegetables.")
 else:
    st.write("Suggestions: Maintain a healthy lifestyle with balanced diet and regular exercise.")
            
# Display existing logs
if os.path.exists("bmi_data.csv"):
    st.subheader("BMI History")
    df = pd.read_csv("bmi_data.csv")
    st.dataframe(df)
else:
    st.info("No BMI data available.")
