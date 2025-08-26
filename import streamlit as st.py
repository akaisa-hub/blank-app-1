import streamlit as st
import time

st.set_page_config(page_title="🎂 Doğum Günü Kartı 🎂", page_icon="🎉")

st.title("🎉🎂 Mutlu Yıllar! 🎂🎉")
st.subheader("Senin için özel bir sürpriz 💖")

# Animasyonlu yazı
message = "İyi ki doğdun, nice mutlu senelere! 🎁✨"
for i in range(1, len(message)+1):
    st.write(message[:i])
    time.sleep(0.05)

st.balloons()