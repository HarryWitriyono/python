import streamlit as st
st.sidebar.markdown("### My first Awesome App")
st.sidebar.markdown("Berikut ini adalah pemrograman sederhana dengan python yang dapat anda coba.  Program ini untuk menghitung luas segi empat.")
st.title("Hitung Luas Segi Empat")
st.markdown('''
print("Hitung Luas Segi Empat")
panjang=float(input("Input nilai panjangnya : "))
lebar=float(input("Input nilai lebarnya : "))
luas=panjang*lebar
print("Luas segitiga = ",luas," satuan")
''')
panjang=st.number_input('Inputkan nilai panjang (0-50)', 0, 50)
lebar=st.number_input('Inputkan nilai lebar (0-50)', 0, 50,0.5)
luas=panjang*lebar
##st.subheader(f'Luas segi empat = {luas:,d} satuan.')
st.write('Luas segi empat = ',luas,' satuan.')
