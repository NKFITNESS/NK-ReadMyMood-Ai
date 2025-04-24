import streamlit as st
import requests
import json
from story_generator import generate_story  # GPT story gen

# Updated Firebase Web API Key
FIREBASE_API_KEY = "AIzaSyBVU1M5kTgtN8xOnEeyLjlW3km1S7q_m88"

st.set_page_config(page_title="NK ReadMyMood AI", layout="centered")

if "email_token" not in st.session_state:
    st.session_state.email_token = None
    st.session_state.email_user = ""

def register_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    return requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

def login_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    return requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

st.title("NK ReadMyMood AI - Login")
auth_choice = st.selectbox("Login or Register", ["Login", "Register"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Submit"):
    res = register_user(email, password) if auth_choice == "Register" else login_user(email, password)
    if res.status_code == 200:
        st.session_state.email_token = res.json()["idToken"]
        st.session_state.email_user = res.json()["email"]
        st.success(f"Logged in as {st.session_state.email_user}")
    else:
        st.error("Authentication failed. Check your credentials.")

if st.session_state.email_token:
    st.title("How are you feeling today?")
    mood = st.selectbox("Select your mood", [
        "Happy", "Sad", "Romantic", "Horny", "Comfortable",
        "Thriller", "Dark", "Motivated", "Fantasy", "Philosophical"
    ])
    
    if st.button("Generate Story"):
        st.markdown(f"### {mood} Mood Story")
        story = generate_story(mood)
        st.write(story)
