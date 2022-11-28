import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
#from  PIL import ImageChops
import pandas as pd
import io 

#st.set_page_config(page_title="Sharone's Streamlit App Gallery", page_icon="", layout="wide")

# sysmenu = '''
# <style>
# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# '''
#st.markdown(sysmenu,unsafe_allow_html=True)

#Add a logo (optional) in the sidebar
logo = Image.open(r'D:\punya della\KULIAH\SMT 3\SIA\projek\PROJEK SEMENTARA\logo.png')
profile = Image.open(r'D:\punya della\KULIAH\SMT 3\SIA\projek\PROJEK SEMENTARA\ig2.jpg')

with st.sidebar:
    choose = option_menu("KOSANKU", ["Home", "Pilihan Kos", "Pembayaran"],
                         icons=['house', 'geo-alt-fill', 'book'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#0E1117"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#FF7F00"},
    }
    )

logo = Image.open(r'D:\punya della\KULIAH\SMT 3\SIA\projek\PROJEK SEMENTARA\logo.png')
profile = Image.open(r'D:\punya della\KULIAH\SMT 3\SIA\projek\PROJEK SEMENTARA\ig2.jpg')
if choose == "Home":
#Add the cover image for the cover page. Used a little trick to center the image
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">KOSANKU</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        
        st.image(logo, width=130 )
    st.write("KOSANKU adalah sebuah situs yang membantu anda mencari dan menemukan kos-kosan di sekitaran Universitas Negeri Semarang. Dengan kelebihan fitur-fitur pada situs ini, diharapkan mampu membantu anda semua dalam mencari kos-kosan. Cari Kos?? KOSANKU aja!!!  untuk informasi lebih lanjut silakan kunjungi instagram kami di @kosanku_official, see u peeps!!!!")    
    st.image(profile, width=700 )

elif choose == "Pilihan Kos":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Temukan Kos Pilihanmu!</p>', unsafe_allow_html=True)
        
    with col2:  
        st.image(logo,  width=150)     

    st.subheader("WISMA MAWAR")
    st.caption("KODE: 001")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("Depan.jpg")
        st.caption("Tampak depan")
    with col2:
        st.image("Ruang.jpg")
        st.caption("Ruang tengah")
    with col3:
        st.image("tv.jpg")
        st.caption("Ruang tv")
    with col4:
        st.image("dapur.jpg")
        st.caption("Dapur")

    st.caption("""
KOS PUTRI WISMA MAWAR - Bangunan baru, bersih, fasilitas oke

Fasilitas pribadi :

    1. Kamar ukuran 3x3m
    
    2. Full furnished (springbed, lemari pakaian, meja belajar, kipas angin)

Fasilitas bersama:

    1. Kamar mandi luar 

    2. Kulkas dan dapur bersama

    3. Ruang tamu

    4. Rak sepatu dan rak helm

    5. Mesin Cuci dan Ruang Jemur

    6. Parkiran motor (AKSES 24 JAM)

HARGA :

    KM LUAR 500rb/bulan (wajib ditempati sendiri)

    MINIMAL SEWA 3 BULAN

Harga sudah termasuk iuran air dan wifi. (iuran listrik, sampah, dan keamanan terpisah, kurang lebih 60rb perbulan)

""")

    st.subheader("KOS MAMAMIA")
    st.caption("Kode : 002")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("garasi2.jpg")
        st.caption("Garasi")
    with col2:
        st.image("kamar2.jpg")
        st.caption("Kamar Tidur")
    with col3:
        st.image("dapur2.jpg")
        st.caption("Dapur")
    with col4:
        st.image("lorong2.jpg")
        st.caption("Teras")

    st.caption("""
KOS PUTRI MAMAMIA - Bangunan baru, bersih

Fasilitas pribadi :

    1. Kamar ukuran 3x3m
    
    2. Full furnished (springbed, gantungan baju, meja belajar, kipas angin)

    3. Kamar mandi dalam

Fasilitas bersama:

    1. Akses masuk 24 jam

    2. Dapur bersama

    3. Ruang tamu

    4. Rak sepatu 

    5. Mesin Cuci dan Ruang Jemur

    6. Parkiran motor

HARGA :

    KM DALAM 600rb/bulan (wajib ditempati sendiri)

    MINIMAL SEWA 3 BULAN

Harga BELUM termasuk iuran air, wifi, iuran listrik, sampah, dan keamanan. (ada biaya tambahan kurang lebih 75rb perbulan)

""")

    st.subheader("KOS BULAN")
    st.caption("Kode : 003")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("depan3.jpg")
        st.caption("Tampak depan")
    with col2:
        st.image("kamar3.jpg")
        st.caption("Kamar Tidur")
    with col3:
        st.image("dapur3.jpg")
        st.caption("Dapur")
    with col4:
        st.image("ruangtamu3.jpg")
        st.caption("Ruang Tamu")

    st.caption("""
KOS PUTRI BULAN - Bangunan baru, bersih, fasilitas oke

Fasilitas pribadi :

    1. Kamar ukuran 3x4m
    
    2. Full furnished (springbed, lemari pakaian, meja belajar, kipas angin)

    3. Kamar mandi dalam 

Fasilitas bersama:

    1. Ruang Tamu luas

    2. Dapur bersama

    3. Akses 24 jam

    4. Mesin Cuci dan Ruang Jemur


HARGA :

    KM LUAR 725rb/bulan (berdua + 250rb)

    *bila ingin berdua harap menghubungi pemilik kos langsung

    MINIMAL SEWA 3 BULAN

Harga sudah termasuk iuran air, wifi, dan listrik 

""")

    st.subheader("GRIYA MERDEKA")
    st.caption("Kode : 004")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("depan4.jpg")
        st.caption("Tampak depan")
    with col2:
        st.image("kamar4.jpg")
        st.caption("Kamar Tidur")
    with col3:
        st.image("dapur4.jpg")
        st.caption("Dapur")
    with col4:
        st.image("garasi4.jpg")
        st.caption("Garasi")

    st.caption("""
KOS PUTRI GRIYA MERDEKA - Strategis, bersih, fasilitas oke

Fasilitas pribadi :

    1. Kamar ukuran 3x3m
    
    2. Full furnished (springbed, lemari pakaian, meja belajar, kipas angin)

    3. Kamar mandi dalam 

Fasilitas bersama:

    1. Ruang Tamu luas

    2. Dapur bersama

    3. Akses 24 jam

    4. Ruang Jemur

    5. Kulkas bersama 

HARGA :

    KM DALAM 500rb/bulan (khusus sendiri)

    MINIMAL SEWA 3 BULAN

Harga belum termasuk iuran air, wifi, dan listrik 
   """)

    st.subheader("WISMA KELINCI")
    st.caption("Kode : 005")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("depan5.jpg")
        st.caption("Tampak depan")
    with col2:
        st.image("dapur5.jpg")
        st.caption("Dapur")
    with col3:
        st.image("garasi5.jpg")
        st.caption("Garasi")
    with col4:
        st.image("tamu5.jpg")
        st.caption("Ruang Tamu")


    st.caption("""
KOS PUTRI WISMA KELINCI - Strategis, bersih, fasilitas oke

Fasilitas pribadi :

    1. Kamar ukuran 4x4m
    
    2. Full furnished (springbed, lemari pakaian, meja belajar, AC)

    3. Kamar mandi dalam 

    4. Jemuran Handuk

    5. TV

Fasilitas bersama:

    1. Ruang Tamu luas

    2. Dapur bersama

    3. Akses 24 jam

    4. Ruang Jemur dan mesin cuci

    5. Kulkas bersama 

HARGA :

    KM DALAM 800rb/bulan (berdua + 250rb)

    *bila ingin berdua harap menghubungi pemilik kos langsung

    MINIMAL SEWA 3 BULAN

Harga belum termasuk iuran air, wifi, dan listrik 
   """)

Nama =st.text_input("Nama Penyewa : ")
Nomor =st.text_input("No Telepon : ")
Kode =st.text_input("Kode Kos : ")
Durasi =st.number_input("Durasi Penyewaan : ", 3)

Barang = []
Harga = []
while Kode :
    if Kode=="001":
        Barang.append("WISMA MAWAR")
        Harga = int(600000)
        break
    elif Kode=="002":
        Barang.append("KOS MAMAMIA")
        Harga = int(650000)
        break
    elif Kode=="003":
        Barang.append("KOS BULAN")
        Harga = int(500000)
        break
    elif Kode=="004":
        Barang.append("GRIYA MERDEKA")
        Harga = int(500000)
        break
    elif Kode=="005":
        Barang.append("WISMA KELINCI")
        Harga = int(800000)
        break
    else :
        Kode=st.text_input("Kode salah, Masukan Ulang Kode Barang : ")


Jumlah_bayar = int(Harga*Durasi)

def garis():
    st.write("-------------------------------------------------------------------")
garis()

st.write("KOSANKU")
st.write("Nama Penyewa :", Nama)
st.write("No Telepon :", Nomor)
st.write("Kode Barang :", Kode)
st.write("Durasi :",Durasi)

garis()
st.write("Pembayaran KOSANKU")
st.write("Jumlah Pembayaran : Rp", round(Jumlah_bayar))





