import streamlit as st
st.sidebar.markdown("### Hitung Luas Segi Empat")
st.sidebar.markdown("Berikut ini adalah pemrograman sederhana dengan python yang dapat anda coba.  Program ini untuk menghitung luas segi empat.")
st.title("Hitung Luas Segi Empat")
st.markdown('''
st.title("Hitung Luas Segi Empat")\n
panjang=st.number_input('Inputkan nilai panjang (0-50)', 0.0, 50.0,0.0,1.0)\n
lebar=st.number_input('Inputkan nilai lebar (0-50)', 0.0, 50.0,0.0,1.0)\n
luas=panjang*lebar\n
st.write("Luas segi empat = ",luas," satuan.")\n
''')
panjang=st.number_input('Inputkan nilai panjang (0-50)', 0.0, 50.0,0.0,1.0)
lebar=st.number_input('Inputkan nilai lebar (0-50)', 0.0, 50.0,0.0,1.0)
luas=panjang*lebar
##st.subheader(f'Luas segi empat = {luas:,d} satuan.')
st.write('Luas segi empat = ',luas,' satuan.')
