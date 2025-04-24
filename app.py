import streamlit as st
import requests
import json

FIREBASE_API_KEY = "AlzaSyBVU1M5kTgtN8xOnEeyLjW3km1S7q_m88"

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
    mood = st.selectbox("How are you feeling today?", [
        "Happy", "Sad", "Romantic", "Horny", "Comfortable", "Thriller", "Dark", "Motivated", "Fantasy", "Philosophical"
    ])
    if st.button("Generate Story"):
        st.markdown(f"### {mood} Mood Story")
        if mood == "Comfortable":
            st.write("Lara sat at the kitchen table, hands sticky with cookie dough, her heart full of secret feelings she’d never dare say aloud...")
        else:
            st.write(f"This will be an AI-generated story matching the {mood.lower()} vibe. (Coming soon!)")
