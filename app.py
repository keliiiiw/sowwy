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
    color: #5E3A41 !important;
    font-family: 'Georgia', serif;
}

/* Desain khusus untuk judul */
h1 {
    color: #C07C88 !important;
    text-align: center;
    font-family: 'Georgia', serif;
    padding-bottom: 10px;
}

/* Memusatkan teks paragraf bagian atas dan MEMAKSA warna cokelat agar tidak hilang di mode gelap HP */
p {
    color: #5E3A41 !important;
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
    background-color: #E2A9B4 !important;
    color: white !important;
    border: none;
    border-radius: 30px;
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 12px rgba(226, 169, 180, 0.4);
}

/* Efek saat tombol disentuh (hover) */
div.stButton > button:first-child:hover {
    background-color: #C07C88 !important;
    color: white !important;
    transform: translateY(-3px);
    box-shadow: 0px 8px 18px rgba(192, 124, 136, 0.6);
}

/* Efek saat tombol diklik/ditekan (active) */
div.stButton > button:first-child:active {
    transform: translateY(1px) scale(0.95);
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
st.write("Website kecil ini aku buat khusus buat alea :) , aku serius mau minta maaf dan bener bener kangen sama kamu alea.")
st.write("Aku sayang banget sama kamu.")

st.write("") # Spasi kosong biar rapi

# Membuat 3 kolom agar tombol berada pas di tengah
col1, col2, col3 = st.columns([1, 1.2, 1])

# MEMBUAT TOMBOL DI DALAM KOLOM TENGAH
with col2:
    tombol_maaf = st.button("Iya, aku maafin 💖", use_container_width=True)
    st.write("") # Spasi antar tombol
    tombol_bete = st.button("Masih bete 😤", use_container_width=True)


# --- MENAMPILKAN PESAN DI LUAR KOLOM AGAR BISA LEBAR ---
# Format string diubah agar tidak terdeteksi sebagai kotak kode oleh Streamlit

if tombol_maaf:
    st.balloons()
    st.toast("Terima kasih sayang... ❤️", icon="💖")
    
    pesan_sukses = (
        "<div style='padding: 30px; background-color: #FCE4EC; border-radius: 15px; color: #5E3A41; margin-top: 25px; border: 1px solid #F8BBD0; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);'>"
        "<h3 style='text-align: center; color: #C07C88; margin-bottom: 20px;'>Aku minta maaf banget cantik.. baca ini ya.. 💌</h3>"
        "<div style='text-align: justify; font-size: 16px; line-height: 1.8; font-family: sans-serif;'>"
        "Aku minta maaf banget ya cantik buat hari ini. Aku ngga tau kenapa ngga bisa mikir panjang buat ngejaga perasaan kamu. "
        "Seharusnya aku bisa mikir kalau hal kaya gitu tuh sesuatu yang janggal dan bukannya di diemin aja, harus nya setelah aku tau konteks dari story kamu "
        "aku langsung unlike, dan langsung bilang ke kamu, bukannya malah diem aja kaya tadi tanpa penjelasan. "
        "Maaf aku betingkah disaat emosi kamu lagi ngga stabil, kamu lagi pusing cape di tambah kamu lagi period."
        "<br><br>"
        "Aku bener-bener minta maaf ya sayang, kamu orang spesial buat aku cantik. Aku mau kamu, aku mau Alea, "
        "Bukan temen yang ada di story kamu, aku mau nya Alea, maafin aku karena aku malah buat mood kamu makin rusak "
        "aku yang kangen banget sama kamu, aku yang buat masalah, jujur dari pagi aku udah semangat banget karena hari ini mau ketemu kamu. "
        "<br><br>"
        "Tapi malah aku yang bikin batal, karena tingkah bodoh dan ngga jelas aku yang bikin kamu jadi males dan ngga mood ketemu aku, "
        "Aku minta maaf banget ya sayang, besok kita ketemu ya, aku mau peluk kamu, mau ndusel di kamu, aku kangen banget sama kamu cantik. "
        "aku sekangen itu sama kamu Alea. "
        "<br><br>"
        "Aku bener-bener minta maaf buat hari ini ya sayang, satu kesalahan bodoh yang seharusnya ngga harus aku lakuin. "
        "Tapi karena otak bodoh aku yang ngegampangin dan anggep remeh, aku sampe lupa sama perasaan kamu, dan bodo amat sama "
        "kelakuan aku tadi, Tapi serius cantik, aku bener bener minta maaf banget, aku ngerasa bersalah banget, aku dari tadi ngga "
        "tenang dan fokus buat ngapa ngapain, di otak aku cuman full mikirin kamu, aku takut kamu makin marah sama aku, bahkan aku takut kamu illfeel ke aku."
        "<br><br>"
        "Dengan segala kekurangan dan kelemahan aku yang bahkan bisa dibilang sangat banyak, tapi aku bener-bener mau berjuang buat kamu. "
        "Walaupun aku bodoh, aneh, dan ngga jelas, setidaknya tekad aku ada karena aku beneran sayang banget sama kamu.. ❤️"
        "</div>"
        "</div>"
    )
    st.markdown(pesan_sukses, unsafe_allow_html=True)

elif tombol_bete:
    st.toast("isokey, aku ngerti tapi jangan lama lama ya cantik, aku kangen 🥺", icon="🌧️")
    
    pesan_error = (
        "<div style='text-align: center; padding: 20px; background-color: #F5EAEB; border-radius: 15px; color: #5E3A41; margin-top: 25px; border: 1px solid #E2A9B4; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);'>"
        "<b>aku kangen banget andrea.. jangan lama lama ya.. </b><br>"
        "Aku kangen banget sama kamu, bener bener sekangen itu.. aku tau sekarang udah susah kamu buat percaya aku lagi "
        "tapi serius cantik, aku bener bener kangen sama kamu, dan aku janji ngga akan bodoh kaya gini lagi, aku akan berusaha "
        "jadi klei yang terbaik buat andrea, aku bener bener minta maaf ya, jangan lama lama buat waktu sendiri nya ya.. aku bener "
        "bener ngga bisa tidur sayang kalo ngga denger suara kamu 😔🫶"
        "</div>"
    )
    st.markdown(pesan_error, unsafe_allow_html=True)
