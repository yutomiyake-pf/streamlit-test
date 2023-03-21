import streamlit as st
import time


st.title('Streamlit入門')

st.write('Iprogress bar')

'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'done'
