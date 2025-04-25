import streamlit as st import random

st.set_page_config(page_title="NK ReadMyMood AI", layout="centered")

st.title("NK ReadMyMood AI - Story Generator")

st.write("### How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Horny", "Comfortable", "Angry"])

if st.button("Generate Story"): story_bank = { "Happy": [ "Once upon a time, in a village full of sunflowers and sunshine, everyone danced and sang every morning...", "There was a kid who laughed so much that even the birds started mimicking him. His joy spread through the valley." ], "Sad": [ "She watched the last train leave the station, knowing he was never coming back...", "The rain didn’t stop that day, and neither did her tears. But in the distance, a rainbow waited." ], "Horny": [ "They locked eyes across the crowded room, and the tension was electric...", "The way he whispered her name made her skin tingle like poetry on fire." ], "Comfortable": [ "Wrapped in a warm blanket, sipping hot chocolate, she felt the world slow down...", "The sound of the fireplace crackling and the faint hum of music made the night feel perfect." ], "Angry": [ "His fists clenched, teeth gritted—he walked out, knowing this time he wouldn’t come back...", "The storm outside matched the one inside him—unforgiving and wild." ] }

if mood in story_bank:
    story = random.choice(story_bank[mood])
    st.markdown(f"### {mood} Mood Story")
    st.write(story)
else:
    st.error("Mood not recognized. Please try again.")

