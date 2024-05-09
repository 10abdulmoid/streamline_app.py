import streamlit as st

# Title and Text
st.title("Hello, Streamlit World!")
st.write("This is a simple Streamlit app to get you started.")

# Input and Button
user_name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {user_name}! Welcome to Streamlit.")

# Checkbox and Radio
fruit_selection = st.checkbox("Do you like fruits?")
if fruit_selection:
    favorite_fruit = st.radio("What's your favorite fruit?", ("Apple", "Banana", "Orange"))
    st.write(f"Your favorite fruit is {favorite_fruit}.")

# Image and Video
st.image("image.jpg", use_column_width=True)  # Replace with your image path
st.video("video.mp4", controls=True)  # Replace with your video path
