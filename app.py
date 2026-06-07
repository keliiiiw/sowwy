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
div.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button:first-child {
    background-color: #E2A9B4;
    color: white;
    border: none;
    border-radius: 30px; /* Ujung lebih melengkung elegan */
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease; /* Animasi transisi lebih halus */
    box-shadow: 0px 4px 12px rgba(226, 169, 180, 0.4); /* Bayangan/glow lembut */
}

/* Efek saat tombol disentuh (hover) */
div.stButton > button:first-child:hover {
    background-color: #C07C88;
    color: white;
    transform: translateY(-3px); /* Efek tombol melayang elegan */
    box-shadow: 0px 8px 18px rgba(192, 124, 136, 0.6); /* Glow memancar saat di-hover */
}

/* Efek saat tombol diklik/ditekan (active) - Meriah tapi minimalis */
div.stButton > button:first-child:active {
    transform: translateY(1px) scale(0.95); /* Efek membal ke dalam saat dipencet */
    box-shadow: 0px 2px 6px rgba(192, 124, 136, 0.4);
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

# Membuat 3 kolom agar tombol berada pas di tengah dan proporsional ukurannya
col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:
    # use_container_width=True memastikan tombol memenuhi tengah kolom secara simetris
    if st.button("Iya, aku maafin 💖", use_container_width=True):
        st.balloons() # Animasi balon meriah dari streamlit
        st.toast("Terima kasih sayang... ❤️", icon="💖") # Notifikasi pop-up kecil elegan di sudut
        
        # Pesan custom elegan (pengganti st.success bawaan yang warnanya hijau kaku)
        pesan_sukses = """
        <div style='text-align: center; padding: 20px; background-color: #FCE4EC; border-radius: 15px; color: #5E3A41; margin-top: 15px; border: 1px solid #F8BBD0; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);'>
            <b>Aku minta maaf banget cantik.. baca ini ya..<br>
            Aku minta maaf banget ya cantik buat hari ini, Aku ngga tau kenapa ngga bisa ngendaliin emosi dan ego aku 
            Ngga seharusnya aku negelakuin hal kaya tadi, bener bener kaya bocil banget, aku tau dari awal semuanya salah aku
            kamu di betein temen kamu, aku malah betingkah kaya gitu, aku malah ikutan bete bukannya nemenin kamu, disaat kamu bete
            aku malah kaya gitu, aku bener bener minta maaf ya sayang, kamu orang spesial buat aku cantik, aku mau kamu, aku mau andrea,
            bukan badan kamu, kamu bukan fantasi aku, kamu perempuan aku, kamu cantik nya aku, kamu imutnya aku, kamu manis nya aku, dan
            tetep jadi cewe yang ribet, yang sensian, yang gedein masalah, karena daya tarik kamu sebenernya disitu cantik, aku ngga mau
            kamu jadi orang lain di depan aku, aku mau andrea jadi andrea, tetep jadi cewe imut yang prengat prengut ya cantik, tetep jadi
            anak imut yang perasa dan bener bener merhatiin hal sekecil apapun, aku bener bener ngga mau kamu jadi orang lain, karena aku mau kamu
            bukan orang lain, aku bener bener minta maaf buat hari ini ya sayang, satu kesalahan yang bener bener fatal, tapi terus jujur ke aku
            ya cantik, aku mau perbaikin diri aku buat kamu, jangan di simpen simpenn dan di tahan tahan unek unek kamu, keluarin aja, biar aku
            jadi cowo yang kamu mau, ajarin aku, bimbing aku, aku bakal berubah demi kamu andrea.. dengan segala kekurangan dan kelemahan aku
            yang bahkan bisa di bilang sangat banyak, tapi aku bener bener mau berjuang buat kamu, walaupun aku bodoh, aneh, dan ngga jelas
            setidaknya tekad aku ada karena aku beneran sayang banget sama kamu..❤️
        </div>
        """
        st.markdown(pesan_sukses, unsafe_allow_html=True)
        
    st.write("") # Spasi antar tombol biar lega
        
    if st.button("Masih bete 😤", use_container_width=True):
        st.toast("Gapapa, aku ngerti... 🥺", icon="🌧️")
        
        # Pesan custom elegan (pengganti st.error bawaan yang warnanya merah kaku)
        pesan_error = """
        <div style='text-align: center; padding: 20px; background-color: #F5EAEB; border-radius: 15px; color: #5E3A41; margin-top: 15px; border: 1px solid #E2A9B4; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);'>
            <b>Gapapa kalau kamu masih marah.</b><br>
            Aku bakal terus usaha sampe kamu luluh. 😔🫶
        </div>
        """
        st.markdown(pesan_error, unsafe_allow_html=True)
