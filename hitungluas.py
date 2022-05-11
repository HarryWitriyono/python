import streamlit as st
st.sidebar.markdown("### My first Awesome App")
st.sidebar.markdown("Welcome to my first awesome app. This app is built using Streamlit and uses data source from redfin housing market data. I hope you enjoy!")
st.title("Hitung Luas Segi Empat")
st.markdown('''
print("Hitung Luas Segi Empat")
panjang=float(input("Input nilai panjangnya : "))
lebar=float(input("Input nilai lebarnya : "))
luas=panjang*lebar
print("Luas segitiga = ",luas," satuan")
''')
