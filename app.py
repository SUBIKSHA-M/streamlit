import pandas as pd
import streamlit as st
import numpy as np
st.title("Collections Dashboard")
with st.form(key='columns_in_form'):
  st.write("DPD wise collections - May")
  cols = st.beta_columns(5)
  a=cols[0].selectbox(f'Select the state', ["None","Tamil Nadu"], key=0)
  b=cols[1].selectbox(f'Select the period', ["None","Post-Covid","Pre-Covid"], key=1)
  c=cols[2].selectbox(f'Select the allocation', ["None","Inhouse","Agency"], key=2)
  d=cols[3].selectbox(f'Select the product',["None","IC","CL"], key=3)
  e=cols[4].selectbox(f'Select the week',["Week 1","Week 2","Week 3","Week 4"], key=4)
  submitted1 = st.form_submit_button('Submit')
if submitted1 :
	st.write(a,b,c,d,e)
	st.write("Its working")
