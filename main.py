import streamlit as st
st.set_page_config(
    page_title="Informasi Sederhana",
    page_icon="🌊",
)

# CSS untuk judul
st.title("Selamat Datang !")
st.markdown("<style>h1 {text-align: center; color: #000000;}</style>", unsafe_allow_html=True)

# Container untuk gambar-gambar
image_container = st.container()

# Tampilkan gambar-gambar dengan judul dan layout horizontal
with image_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn0-production-images-kly.akamaized.net/wWs9Ishiqa4ya0JGsDow36FMbNk=/0x0/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3662769/original/033930000_1639360949-logo-motor-honda-c0af44.jpg", use_column_width=True)
        st.write("<div style='text-align: center;'>Honda</div>", unsafe_allow_html=True)
    with col2:
        st.image("https://cdn.pertamax7.com/wp-content/uploads/2021/10/Kawasaki-River-Mark-Background-Putih.jpg", use_column_width=True)
        st.write("<div style='text-align: center;'>Kawasaki</div>", unsafe_allow_html=True)
    with col3:
        st.image("https://vectrostudio.com/wp-content/uploads/2019/11/Yamaha-Logo_vectrostudio.jpg", use_column_width=True)
        st.write("<div style='text-align: center;'>Yamaha</div>", unsafe_allow_html=True)

# CSS untuk gambar
st.markdown("<style>img {margin: 10px;}</style>", unsafe_allow_html=True)

