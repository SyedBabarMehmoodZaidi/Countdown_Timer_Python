import time
import streamlit as st

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 60

# Dark Theme CSS
dark_css = """
<style>
body {
    background-color: #121212;
}

.stApp {
    background-color: #121212;
    color: #ffffff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
    text-align: center;
    color: #00E5FF;
    font-size: 48px;
    margin-top: 20px;
    text-shadow: 2px 2px 8px #00E5FF44;
}

.timer-box {
    background-color: #1e1e1e;
    border-radius: 16px;
    padding: 40px;
    margin: 30px auto;
    width: 320px;
    text-align: center;
    color: #FFEB3B;
    font-size: 48px;
    font-weight: bold;
    box-shadow: 0 0 20px #00E5FF33;
}

p, label, .stNumberInput {
    color: #ccc !important;
    font-size: 18px;
}

div.stButton > button {
    background-color: #e81313;
    color: #000;
    font-size: 20px;
    padding: 12px 30px;
    border-radius: 10px;
    border: none;
    transition: 0.3s ease-in-out;
}

div.stButton > button:hover {
    background-color: #018786;
    transform: scale(1.05);
    color: white;
}
</style>
"""

st.markdown(dark_css, unsafe_allow_html=True)

# Page Title
st.markdown("<h1>⏱ OneTap Countdown Timer</h1>", unsafe_allow_html=True)

# Input field
if not st.session_state.running:
    st.markdown("<p>⏰ Enter countdown time in seconds:</p>", unsafe_allow_html=True)
    st.session_state.remaining_time = st.number_input("", min_value=1, step=1, value=st.session_state.remaining_time, format="%d")

# Countdown Timer Logic
def countdown_timer():
    st.session_state.running = True
    placeholder = st.empty()

    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        placeholder.markdown(
            f"<div class='timer-box'>⏳ {mins:02}:{secs:02}</div>",
            unsafe_allow_html=True,
        )
        time.sleep(1)
        st.session_state.remaining_time -= 1

    if st.session_state.running:
        placeholder.markdown("<div class='timer-box' style='color: #4CAF50;'>🎉 Time's Up!</div>", unsafe_allow_html=True)
    else:
        placeholder.markdown("<div class='timer-box' style='color: #FFC107;'>⏹ Timer Stopped</div>", unsafe_allow_html=True)

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Timer"):
        countdown_timer()
with col2:
    if st.button("🛑 Stop Timer"):
        st.session_state.running = False
