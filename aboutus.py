import streamlit as st
import random

st.title("EatS: Tracking Your Food and Sleep")
st.subheader("Home")
st.write("EatS is a website created by first year Computer Engineering Students from Cavite State University as a project. This website aims to contribute to a person's betterment of their health and fitness.")

st.page_link("sleep/app.py", label="Go to the Sleep Tracker", icon=":material/bedtime:")
st.page_link("food/food.py", label="Go to the Food Tracker", icon=":material/restaurant:")
st.page_link("bmi.py", label="Go to the BMI Tracker", icon=":material/scale:")

quotes_list = ("Matulog ka nang maaga, ‘wag ka magpupuyat magagalit ako >:(",
"How was your day? Kaya pa?... Kaya ‘yan!",
"Uy nakita ko food intake mo. Kumain ka nang mabuti ha",
"Guess what day today? Tama! Today is the day para unahin mo naman ang sarili mo!",
"Nakakapagod ‘no? Pahinga ka muna",
"Hoy may assignments ka pa HAHAHA Galaw galaw!",
"Kamusta ka naman so far?",
"Ayos lang magkaroon ng shortcomings, patuloy ka lang!",
"Tandaan: ‘Wag mag cramming! Gawin mo na agad ‘yan.",
"Buti pa streak naaalala mo, ‘yung homework mo hindi.",
"Kung sino-sino pa kinakausap mo nandito lang naman ako. Tutulungan kitang alagaan ang sarili mo.",
"Just in case wala pang nagtatanong sayo. Kumain ka na ba? <333",
"I'm proud of you! Always!",
"Bad day? Tara mag kwek-kwek!",
"I hope you're doing fine, mag-iingat ka lagi!",
"Kamusta pagkain mo? Naubos mo ba?",
"Don't skip a meal! Kumain ka kahit busy ka",
"Nagkabalikan na naman yung kaibigan mo at jowa niya? HAHAHAHA Balik ka na rin sa pag-track ng health mo 👉🏼👈🏼",
"Uy break na pala sila ano… Kaya ikaw, ‘wag kang magpupuyat sa maling tao!",
"Do your best today! Everyday!",
"Don't worry about what will come next, don't overthink yourself.",
"Everything will be fine, maybe not today nor tomorrow nor next week… But soon.",
"Padayon! May pangarap ka pang aabutin!",
"Bawi tayo next exam, I know you can do better!",
"Panis yang mga basher mo ‘pag inuna mo sarili mo",
"Don't be too harsh on yourself. Always take care of yourself. Learn to love yourself.",
"Matalino sa acads. Tanga sa pag-ibig. It's time na para uminom ka naman ng tubig.",
"Look outside, look at the moon. It's beautiful isn't it? Yiiieee that means gabi na, matulog ka nang maaga!",
"Subo mo ‘to, subo mo ‘to! Subo mo na ‘yang pagkain mo! ‘Wag puro selpon!",
"Look may progress ka na oh, patuloy ka lang <333",
"HAHAHA sige na ako na magsasabi. Sleep well ♥️",
"A well fit body comes with a great dietary.",
"Kain ka gulay para humaba ang iyong buhay, sasamahan pa kita sa pagtanda ;)",
"Oh ang tubig wag mo kakalimutan baka mauhaw ka sa atensyon ko :>",
"Anong oras na ay nako! Mas maigi ang matulog kesa mag relapse",
"Dedma sa bashers focus tayo sa goal",
"Awww wawa naman ang baby na yannn jogging tayo para gumaan ang pakiramdam mo?",
"Sabi ni mama kumain daw ng gulay para kasama mo ‘ko habang buhay",
"Kumain ka na masamang pinaghihintay ang grasya sige ka",
"Sama ka? shot tayo? (ng gatas at tubig)",
"Kain ka na ipinagluto kita daliiii",
"Goals ang hinahabol haaa, hindi ang maling tao",
"Alam ko na sad ka today pero hindi healthy para sayo yun. Kaya smile na ikaw haaa",
"Ang self-esteem mo ang priority ko kaya gusto ko na lagi kang confident 🫶🏼",
"Sabi nila pag maaga ka daw natulog mapapanaginipan mo na magka-cuddles tayo",
"Rank tayo daliii mythical glory nako sa health and fitness bubuhatin kita!",
"Congrats! dahil with honors ka sa eating vegetables, having enough sleep, and doing your daily exercise, i-ma-myday kita!",
"Fuel your body, nourish your soul, embrace health, find balance.",
"Are you hungry right now? How about we cook a very healthy meal while I hug you from the back :3",
"Dinner at olive garden? I’ll pick you up by 8pm <33")

st.caption(random.choice(quotes_list))
