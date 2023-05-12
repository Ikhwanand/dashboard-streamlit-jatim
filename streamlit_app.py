import streamlit as st
import pandas as pd  
import numpy as np  
import plost 


# Page setting
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Dashboard Penyakit Hipertensi dan Diabetes Melitus pada Provinsi Jawa Timur 2018-2022')

st.sidebar.header('Dashboard')

st.sidebar.subheader('Timer Data Parameter')
year_data = st.sidebar.selectbox('Select year data', ('Tahun 2018', 'Tahun 2019', 'Tahun 2020', 'Tahun 2021', 'Tahun 2022'))

st.sidebar.subheader('Bar Chart Parameter')
data_theta = st.sidebar.selectbox('Select data', ('jumlah_penyakit_hipertensi', 'jumlah_penyakit_diabetes_mellitius'))

st.sidebar.markdown(''' 
                    Created with ❤️ by Ikhwananda copyright Data Professor
                    ''')

# Data 
data = pd.read_csv('Jumlah Penyakit Tidak Menular Clean.csv')

penyakit_hipertensi_sum = data['jumlah_penyakit_hipertensi'].sum()
penyakit_diabetes_sum = data['jumlah_penyakit_diabetes_mellitius'].sum()

penyakit_hipertensi_mean = data['jumlah_penyakit_hipertensi'].mean()
penyakit_diabetes_mean = data['jumlah_penyakit_diabetes_mellitius'].mean()

penyakit_hipertensi_min = data['jumlah_penyakit_hipertensi'].min()  
penyakit_diabetes_min = data['jumlah_penyakit_diabetes_mellitius'].min() 

penyakit_hipertensi_max = data['jumlah_penyakit_hipertensi'].max()
penyakit_diabetes_max = data['jumlah_penyakit_diabetes_mellitius'].max()


# Row A
st.markdown('## Penyakit Hipertensi')
st.markdown('##')
st.subheader('Total penyakit Hipertensi dari 2018 - 2022')
cola1, cola2, cola3, cola4 = st.columns(4)

cola1.metric("Total", f"{round(penyakit_hipertensi_sum):,}")
cola2.metric("Rata-rata", f"{round(penyakit_hipertensi_mean):,}")
cola3.metric("Minimal", f"{round(penyakit_hipertensi_min):,}")
cola4.metric("Maksimal", f"{round(penyakit_hipertensi_max):,}")


# Row B
st.markdown('## Penyakit Diabetes Melitus')
st.markdown('##')
st.subheader('Total penyakit Diabetes Melitus dari 2018 - 2022')
colb1, colb2, colb3, colb4 = st.columns(4)

colb1.metric("Total", f"{round(penyakit_diabetes_sum):,}")
colb2.metric("Rata-rata", f"{round(penyakit_diabetes_mean):,}")
colb3.metric("Minimal", f"{round(penyakit_diabetes_min):,}")
colb4.metric("Maksimal", f"{round(penyakit_diabetes_max):,}")

c1, c2 = st.columns((7,3))
if year_data == 'Tahun 2018':
    tahun_2018 = data.query('periode_update == "Tahun 2018"')
    data_2018 = tahun_2018[['kabupaten_kota', data_theta]]
    with c1:
        st.markdown('### Bar Chart')
        plost.bar_chart(
            data=data_2018,
            bar='kabupaten_kota',
            value=data_theta,
            direction = 'horizontal',
            color='kabupaten_kota',
            
            
        )
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=data_2018,
            theta=data_theta,
            color='kabupaten_kota',
            legend='bottom',
            use_container_width=True,
        )
elif year_data == 'Tahun 2019':
    tahun_2019 = data.query('periode_update == "Tahun 2019"')
    data_2019 = tahun_2019[['kabupaten_kota', data_theta]]
    with c1:
        st.markdown('### Bar Chart')
        plost.bar_chart(
            data=data_2019,
            bar='kabupaten_kota',
            value=data_theta,
            direction='horizontal',
            color='kabupaten_kota',
            
            
        )
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=data_2019,
            theta=data_theta,
            color='kabupaten_kota',
            legend='bottom',
            use_container_width=True,
        )

elif year_data == 'Tahun 2020':
    tahun_2020 = data.query('periode_update == "Tahun 2020"')
    data_2020 = tahun_2020[['kabupaten_kota', data_theta]]
    with c1:
        st.markdown('### Bar Chart')
        plost.bar_chart(
            data=data_2020,
            bar='kabupaten_kota',
            value=data_theta,
            direction='horizontal',
            color='kabupaten_kota',
            
            
        )
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=data_2020,
            theta=data_theta,
            color='kabupaten_kota',
            legend='bottom',
            use_container_width=True,
        )

elif year_data == 'Tahun 2021':
    tahun_2021 = data.query('periode_update == "Tahun 2021"')
    data_2021 = tahun_2021[['kabupaten_kota', data_theta]]
    with c1:
        st.markdown('### Bar Chart')
        plost.bar_chart(
            data=data_2021,
            bar='kabupaten_kota',
            value=data_theta,
            direction='horizontal',
            color='kabupaten_kota',
            
            
        )
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=data_2021,
            theta=data_theta,
            color='kabupaten_kota',
            legend='bottom',
            use_container_width=True,
        )
        
elif year_data == 'Tahun 2022':
    tahun_2022 = data.query('periode_update == "Tahun 2022"')
    data_2022 = tahun_2022[['kabupaten_kota', data_theta]]
    with c1:
        st.markdown('### Bar Chart')
        plost.bar_chart(
            data=data_2022,
            bar='kabupaten_kota',
            value=data_theta,
            direction='horizontal',
            color='kabupaten_kota',
            
            
        )
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=data_2022,
            theta=data_theta,
            color='kabupaten_kota',
            legend='bottom',
            use_container_width=True,
        )
