import  streamlit as st
import random
import string

def generator_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits #add numbers (0-9)  if selected

    if use_special:
        characters += string.punctuation #add special characters  if selected

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password length", min_value=4,  max_value=50, value=12)

use_digits= st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    Password = generator_password(length,use_digits,use_special)
    st.write(f"Generated password: `{Password}`")
st.write("-------------------------------")
st.write("Made with by ✨[Khizra Iqbal](https://github.com/KHIZRA-IQBAL)")


