mport streamlit as st

st.title("BMI Goal Helper")

current_bmi = st.number_input("Enter your current BMI:", min_value=0.0)
goal_bmi = st.number_input("Enter your goal BMI:", min_value=0.0)

if st.button("Get Suggestions"):
    if current_bmi > goal_bmi:
        st.subheader("Suggestions for Weight Loss:")
        st.write("- *Increase physical activity:* Aim for at least 150 minutes of moderate-intensity or 75 minutes of vigorous-intensity aerobic exercise per week. Consider activities like brisk walking, jogging, swimming, cycling, or dancing.")
        st.write("- *Follow a balanced diet:* Focus on whole, unprocessed foods, including fruits, vegetables, lean proteins, and whole grains. Limit processed foods, sugary drinks, and unhealthy fats.")
        st.write("- *Strength training:* Incorporate strength training exercises 2-3 times per week to build muscle mass, which helps boost metabolism.")
        st.write("- *Mindful eating:* Pay attention to your hunger and fullness cues, and avoid distractions while eating.")
        st.write("- *Get enough sleep:* Aim for 7-9 hours of quality sleep per night.")
        st.write("- *Consult a professional:* Consider consulting a doctor or a registered dietitian for personalized guidance.")

    elif current_bmi < goal_bmi:
        st.subheader("Suggestions for Weight Gain:")
        st.write("- *Increase calorie intake:* Consume more calories than you burn. Focus on nutrient-rich foods that provide healthy calories.")
        st.write("- *Strength training:* Lift weights regularly to build muscle mass.")
        st.write("- *Eat frequently:* Consume smaller, more frequent meals throughout the day to help increase calorie intake.")
        st.write("- *Include healthy fats:* Incorporate healthy fats, such as avocados, nuts, and seeds, into your diet.")
        st.write("- *Consult a professional:* Consider consulting a doctor or a registered dietitian for personalized guidance.")

    else:
        st.write("Your current BMI and goal BMI are the same. Maintain your healthy lifestyle!")

if st.button("View BMI Logs"):
    st.write("BMI Logs:")
    if data:
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.write("No data available.")
