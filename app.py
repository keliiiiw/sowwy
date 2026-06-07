import streamlit as st

# Konfigurasi tab browser
st.set_page_config(page_title="Maafin Aku Ya...", page_icon="🎀", layout="centered")

# --- CSS KUSTOM UNTUK TEMA PINK ELEGAN ---
tema_pink = """
<style>
/* Mengubah warna background utama menjadi soft lavender blush */
[data-testid="stAppViewContainer"] {
    background-color: #FFF0F5;
}

/* Membuat background header transparan */
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

/* Mengubah font dan warna teks secara keseluruhan (cokelat elegan) */
html, body, [class*="css"] {
    color: #5E3A41;
    font-family: 'Georgia', serif;
}

/* Desain khusus untuk judul */
h1 {
    color: #C07C88 !important;
    text-align: center;
    font-family: 'Georgia', serif;
    padding-bottom: 10px;
}

/* Memusatkan teks paragraf */
p {
    text-align: center;
    font-size: 18px;
    line-height: 1.6;
}

/* Menyembunyikan menu bawaan Streamlit agar terlihat seperti web profesional */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Desain untuk Tombol */
div.stButton > button:first-child {
    background-color: #E2A9B4;
    color: white;
    border: none;
    border-radius: 20px; /* Membuat ujung tombol melengkung halus */
    padding: 10px 24px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.05); /* Bayangan lembut */
}

/* Efek saat tombol disentuh (hover) */
div.stButton > button:first-child:hover {
    background-color: #C07C88;
    color: white;
    transform: translateY(-2px); /* Efek tombol sedikit terangkat */
}

/* Membuat kotak pesan sukses/error lebih melengkung */
[data-testid="stNotification"] {
    border-radius: 15px;
}
</style>
"""
# Memasukkan CSS ke dalam web
st.markdown(tema_pink, unsafe_allow_html=True)


# --- KONTEN WEB ---
st.markdown("<h1>Halo Sayang... 🎀</h1>", unsafe_allow_html=True)
st.write("---")

st.write("Aku tau aku salah, dan aku bener-bener minta maaf ya.")
st.write("Website kecil ini aku buat khusus buat kamu, sebagai tanda kalau aku serius mau perbaikin semuanya.")
st.write("Aku sayang banget sama kamu.")

st.write("") # Spasi kosong biar rapi

# Membuat 3 kolom agar tombol berada pas di tengah dan tidak terlalu panjang
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Iya, aku maafin 💖"):
        st.balloons()
        st.success("Makasih banyak sayang! Aku janji bakal lebih baik lagi. I love you! ❤️")
        
    st.write("") # Spasi antar tombol
        
    if st.button("Masih bete 😤"):
        st.error("Gapapa kalau kamu masih marah. Aku bakal terus usaha sampe kamu luluh. 😔🫶")
