import streamlit as st
import webbrowser as wb
st.title("Install database Sistem Pendukung Keputusan Metode AHP")
st.markdown('''Silahkan lengkapi isian berikut untuk membuat database baru untuk aplikasi SPK Metode AHP''')
hostname = st.text_input('Ketik nama host ',value='localhost')
username = st.text_input('Ketik nama user databasenya ',value='root')
passwordnya = st.text_input('Ketik passwordnya',value='',type='password')
namadb = st.text_input('Ketik nama databasenya ', value='ahp')
if st.button('Instal Databasenya'):
 st.write('Proses instalasi dilaksanakan... tunggu sebentar !')
 import mysql.connector
 mydb = mysql.connector.connect( host=hostname,user=username,password=passwordnya) 
 mycursor=mydb.cursor()
 mycursor.execute("select schema_name from information_schema.schemata where schema_name='"+namadb+"';")
 myresult=mycursor.fetchall()
 if myresult:
  st.write('Database sudah ada ! Apakah akan dihapus ?')
  if st.button('Ya'):
   mycursor.execute("drop database "+namadb)
   mydb.commit()
  if st.button('Tidak'):
   st.write('Database '+namadb+' tidak jadi dibuat !')
   exit() 
 mycursor.execute("select schema_name from information_schema.schemata where schema_name='"+namadb+"';")
 myresult=mycursor.fetchall()
 if not myresult:
  mycursor.execute("create database "+namadb)
  st.write('Database '+namadb+' berhasil dibuat !')
