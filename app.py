import streamlit as st
from emotion_analysis import detect_emotion
from voice_input import get_voice_input
from health_model import predict_risk
from database import save_data,create_table
create_table()



st.title("🧬 EMOCARE – Emotion Driven Health Risk Prediction")

st.write("Monitor emotional and lifestyle health risks")

if "user_text" not in st.session_state:
    st.session_state.user_text=""
# Voice Input
if st.button("🎤 Speak Emotion"):
    text = get_voice_input()
    st.session_state.user_text = text
    st.write("You said:", text)
else:
    text = st.text_area("How are you feeling today?",
                        value=st.session_state.user_text,
                        key="emotion_box")

sleep = st.slider("Sleep Hours",0,12,6)
exercise = st.slider("Exercise Days",0,7,2)
junk = st.slider("Junk Food Times per Week",0,10,3)

def health_suggestions(emotion, sleep, exercise, junk, risk):

    suggestions = []

    # Emotion suggestions
    if emotion == "negative":
        suggestions.append("Practice meditation or deep breathing for 10 minutes daily.")
        suggestions.append("Talk with friends or family to reduce stress.")

    # Sleep suggestions
    if sleep < 6:
        suggestions.append("Try to sleep at least 7–8 hours for better health.")

    # Exercise suggestions
    if exercise < 3:
        suggestions.append("Exercise at least 30 minutes for 3–5 days per week.")

    # Junk food suggestions
    if junk > 3:
        suggestions.append("Reduce junk food and include fruits and vegetables in your diet.")

    # Risk suggestions
    if risk == "high":
        suggestions.append("High risk detected. Maintain healthy habits and consult a doctor if needed.")

    elif risk == "moderate":
        suggestions.append("Moderate risk. Improve lifestyle habits gradually.")

    else:
        suggestions.append("Your health condition looks good. Maintain your current healthy routine.")

    return suggestions

if st.button("Predict Health Risk"):

    emotion = detect_emotion(text)

    risk = predict_risk(emotion,sleep,exercise,junk)
    suggestions = health_suggestions(emotion,sleep,exercise,junk,risk)

    save_data(emotion,sleep,exercise,junk,risk)

    st.subheader("Results")

    st.write("Detected Emotion:",emotion)
    st.write("Predicted Health Risk:",risk)

    if risk == "high":
        st.warning("High risk detected. Improve sleep, reduce stress.")
    elif risk == "moderate":
        st.info("Moderate risk. Maintain healthy habits.")
    else:
        st.success("Low risk. Keep up your healthy lifestyle.")
    st.subheader("Health Suggestions")
    for s in suggestions:

        st.write(".",s)