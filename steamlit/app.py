import streamlit as st
import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os

# loading env for backend_url
load_dotenv() 
 
#  Introduction 
st.title("MoodFlag 🌥️")
st.subheader("What’s Mood Swing & Why It Matters")
st.markdown("<div style='text-align: justify;margin:20px 0px'>Mood swings are sudden and intense changes in emotional state — one moment you might feel great, and the next, overwhelmed, irritated, or down. While occasional shifts are normal for everyone, frequent or extreme mood swings can be a sign of deeper mental health challenges like depression, anxiety, or bipolar disorder.If your mood changes become too intense or start affecting your daily life, it’s not just “a phase” — it might be time to seek help or support. Early intervention and mental health treatment can make a big difference.That’s why we built this app — to help you track, understand, and predict mood swings based on your daily habits, stress levels, and lifestyle changes. The goal is to raise awareness and encourage people to take care of their mental well-being before things escalate.</div>",unsafe_allow_html=True)

# Demo and Instructions
st.subheader("How to Use MoodFlag ?")
st.markdown("""
<div style='text-align: justify;margin:20px 0px'>
This app uses a combination of personal background, lifestyle patterns, and mental health history to predict potential mood swing risks. By analyzing inputs like work stress, social habits, and previous mental health experiences, it helps identify individuals who might be at higher risk and could benefit from seeking support or treatment.
<br>
<div style='border:1px solid #202124; padding:10px;margin:40px 0px; border-radius: 5px;'>
<b style='color:#bcbcbd;'>We use the following factors for prediction:</b>
<ul>
<li><b>Demographics:</b> Gender, Country, Occupation, Self-employed status</li>
<li><b>Mental Health History:</b> Family history, past treatment, previous mental health issues</li>
<li><b>Lifestyle Indicators:</b> Days spent indoors, coping struggles, changes in daily habits</li>
<li><b>Mental Health Awareness:</b> Willingness to attend mental health interviews, knowledge of care options</li>
<li><b>Social & Work Patterns:</b> Interest in work, social weaknesses, increasing stress levels</li>
</div>
All these are captured through a simple form — once submitted, our model processes the data and provides a prediction about whether the individual is at high risk of mood swings and may need support.
</div>
""", unsafe_allow_html=True)

with st.container():    
    with st.form("prediction_form"):
        st.text("Please fill out the form below to predict mood swings:")
        col1, col2= st.columns(2)
        with col1:
            gender = st.selectbox("Gender ", ["Male", "Female"])
            country = st.selectbox("Country ", ["United States", "UK", "Canada", "Australia", "Netherlands", "Ireland", "Germany", "Sweden", "India", "France", 'Portugal', 'Brazil', 'Costa Rica', 'Russia', 'Germany',
            'Switzerland', 'Finland', 'Israel', 'Italy', 'Bosnia and Herzegovina',
            'Singapore', 'Nigeria', 'Croatia', 'Thailand', 'Denmark', 'Mexico', 'Greece',
             'Moldova', 'Colombia', 'Georgia', 'Czech Republic', 'Philippines'])
            occupation = st.selectbox("Occupation ", ["Student", "Corporate", "Business", "Housewife", "Other"])
            self_employed = st.selectbox("Self-Employed ", ["Yes", "No"])
            family_history = st.selectbox("Family history of Mental Illness ", ["Yes", "No"])
            treatment = st.selectbox("Have you ever sought treatment?", ["Yes", "No"])
            mental_health_interview = st.selectbox("Reveal mental health issue in interview?  ", ["Yes", "No", "Maybe"])
        with col2:
            days_indoors = st.selectbox("Days indoors ", ["1-14 days", "Go out Every day", "More than 2 months", "15-30 days"])
            growing_stress = st.selectbox("Growing Stress ", ["Yes", "No", "Maybe"])
            changes_habits = st.selectbox("Noticed habit changes ", ["Yes", "No", "Maybe"])
            mental_health_history = st.selectbox("Mental health history ", ["Yes", "No","Maybe"])
            coping_struggles = st.selectbox("Struggle with stress ", ["Yes", "No"])
            work_interest = st.selectbox("Lost interest in work ", ["Yes", "No","Maybe"])
            social_weakness = st.selectbox("Avoiding social interaction ", ["Yes", "No", "Maybe"])        
        care_options = st.selectbox("Know mental health care options ", ["Yes", "No", "Not sure"])

        submit = st.form_submit_button("Predict", use_container_width=True , type="secondary")

if submit:
    user_data = {
        "Gender": gender,
        "Country": country,
        "Occupation": occupation,
        "self_employed": self_employed,
        "family_history": family_history,
        "treatment": treatment,
        "Days_Indoors": days_indoors,
        "Growing_Stress": growing_stress,
        "Changes_Habits": changes_habits,
        "Mental_Health_History": mental_health_history,
        "Coping_Struggles": coping_struggles,
        "Work_Interest": work_interest,
        "Social_Weakness": social_weakness,
        "mental_health_interview": mental_health_interview,
        "care_options": care_options
    }
    input_df = pd.DataFrame([user_data])
    transposed_df = input_df.T.rename(columns={0: "Your Data"})
    st.dataframe(transposed_df, use_container_width=True)
    
    # services :connecting to backend for prediction
    # ENV = os.getenv("BACKEND_URL")
    ENV = "https://moodflag-api.onrender.com/"  
    try:
        response = requests.post(f"{ENV}/predict", json=user_data)
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(3)   
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.badge("Success", icon=":material/check:", color="green")
            # 0 -> high , 1 -> low , 2 -> medium
            if( prediction == 0):
                st.warning("High risk of mood swings detected. It’s important to seek support or talk to a mental health professional.")
            elif prediction == 1:
                st.success("Low risk of mood swings detected. Keep up the good habits!")
            elif prediction == 2:
                st.info("Medium risk of mood swings detected. Consider monitoring your mental health and seeking support if needed.")
        else:
            st.error(f"Error: {response.json()['detail']}")
    except Exception as e:
        st.error(f"Failed to connect to prediction API: {e}")
    
st.html("""
<hr style='margin-top: 30px; margin-bottom: 40px; background-color: #202124; height: 1px; border: none;'>
<div style='text-align: justify; font-size: 14px; color: #888; margin-bottom: 20px;'>
Disclaimer:
This app is a personal hobby project created for educational and demonstration purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.
If you're experiencing emotional distress or struggling with your mental health, please consult with a licensed therapist, counselor, or mental health professional.
Your well-being matters.</div>
""")

st.markdown("""
<div style='text-align: center; font-size: 14px; color: #888
; margin-bottom: 20px;'>
Developed by ...
</div>
""",unsafe_allow_html=True)