import streamlit as st

x = st.slider("Select a number", 0, 100, 50)

st.write(f"x square is {x  ** 2}")


y = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])

if y is not None:
    st.write(f"Uploaded file name: {y.name}")
    st.image(y)
