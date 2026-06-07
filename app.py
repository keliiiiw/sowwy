import streamlit as st

# Mengatur tab browser
st.set_page_config(page_title="Maafin Aku Ya", page_icon="🥺")

# Judul dan isi pesan
st.title("Halo Sayang... 🥺")
st.write("Aku tau aku salah, dan aku bener-bener minta maaf ya.")
st.write("Aku bikin web kecil ini khusus buat kamu supaya kamu tau aku serius minta maaf.")

# Tombol interaktif
if st.button("Pencet ini dong kalo kamu mau maafin aku"):
    st.balloons()
    st.success("Makasih sayang! Aku janji bakal lebih baik lagi ❤️")
    
# Opsi kalau dia masih marah
if st.button("Masih ngambek 😤"):
    st.error("Yaudah, aku bakal terus minta maaf sampe kamu luluh. 😔")
