import streamlit as st

st.title("BMI Tracker")

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

        st.subheader("Tips:")
        st.write("Sports drinks, soda, juice, and sweet tea are examples of sugary beverages that have little to no nutritional benefit and add extra calories. Overweight is more common among those who use sugary drinks on a daily basis. Most of the time, go for water or low-fat milk.")
        st.write("Frequent exercise helps you look and feel good and can help you lose weight since it burns calories and builds muscle. Cycling to school, walking the family dog, and engaging in other activities that boost your daily activity level can have an impact. Increase the intensity of your workout and incorporate some muscle-building strength exercises if you want to burn more calories.")
        st.write("The likelihood of being overweight is higher for those who spend a lot of time in front of screens. Limit how much time you spend on non-school-related activities on computers, phones, and tablets, as well as how much time you spend playing video games and watching TV. For a better night's sleep, turn off all screens at least an hour before bed.")
        st.write("Large servings add up extra calories, which can lead to weight gain. Pick smaller servings, particularly when consuming high-calorie snacks. Try splitting an entree or bringing half of your meal home with you when dining out.")
        st.write("There is more to fruits and vegetables than just vitamins and minerals. They also fill you up since they are high in fiber. Additionally, you're less prone to overeat when you consume a lot of fruits and vegetables.")

    elif current_bmi < goal_bmi:
        st.subheader("Suggestions for Weight Gain:")
        st.write("- *Increase calorie intake:* Consume more calories than you burn. Focus on nutrient-rich foods that provide healthy calories.")
        st.write("- *Strength training:* Lift weights regularly to build muscle mass.")
        st.write("- *Eat frequently:* Consume smaller, more frequent meals throughout the day to help increase calorie intake.")
        st.write("- *Include healthy fats:* Incorporate healthy fats, such as avocados, nuts, and seeds, into your diet.")
        st.write("- *Consult a professional:* Consider consulting a doctor or a registered dietitian for personalized guidance.")

        st.subheader("Tips:")
        st.write("Consider increasing your calorie intake and consulting a doctor or nutritionist.")
        st.write("For extra calories, add extras to your meals, like nut butter on whole-grain bread or cheese in casseroles. For more calories and protein, you can also add liquid or dry milk to food. Soups and mashed potatoes are two examples.")
        st.write("Start eating five to six smaller meals throughout the day gradually. To identify when you might be hungry, try to pay attention to your body. Even if you're not really hungry, you might need to schedule mealtimes.")
        st.wirte("Drinks have the power to fill you up. If it applies to you, refrain from drinking right before or during meals. However, be sure to consume adequate amounts of liquids throughout the day.")
        st.write("By increasing your muscle mass, exercise—especially strength training—can aid in weight growth. Additionally, exercise may increase your hunger.")

    else:
        st.write("Your current BMI and goal BMI are the same. Maintain your healthy lifestyle!")

if st.button("View BMI Logs"):
    st.write("BMI Logs:")
    if data:
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.write("No data available.")
