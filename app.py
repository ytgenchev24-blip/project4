import streamlit as st
st.title("Log in system")
name = st.text_input("Въведи име")
if st.button("Провери"):
  if name.strip() == " ":
    st.warning ("Моля въведи текст")
  elif not name is alpha():
st.warning("------")
else: st.success("Текста е въведен правилно")
