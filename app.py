import streamlit as st

st.title("Unit Converter")

st.write("Convert Length units (Meter, Kilometer, Mile)")

value = st.number_input("Enter value to convert:")

from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Mile"])
to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Mile"])

if st.button("Convert"):
    # Conversion logic
    if from_unit == "Meter" and to_unit == "Kilometer":
        result = value / 1000
    elif from_unit == "Kilometer" and to_unit == "Meter":
        result = value * 1000
    elif from_unit == "Meter" and to_unit == "Mile":
        result = value / 1609
    elif from_unit == "Mile" and to_unit == "Meter":
        result = value * 1609
    elif from_unit == to_unit:
        result = value
    else:
        result = "Conversion not supported yet."

    st.success(f"{value} {from_unit} = {result} {to_unit}")
