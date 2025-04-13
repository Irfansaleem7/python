import streamlit as st

# Set page title
st.title("Counter App")

# Initialize counter in session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Display counter value
st.write(f"### Count: {st.session_state.count}")

# Buttons to increase or reset the counter
col1, col2 = st.columns(2)
with col1:
    if st.button("Increase"):
        st.session_state.count += 1

with col2:
    if st.button("Reset"):
        st.session_state.count = 0
