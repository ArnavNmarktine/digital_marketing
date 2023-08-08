import streamlit as st 
import numpy as np
import pandas as pd 
import random
import matplotlib.pyplot as plt
import warnings
# Ignore all warnings (Not recommended in most cases)
warnings.filterwarnings("ignore")

from utils import user_by_date,plot


a={'organic_search':51,'Direct':16,'Referral':14,'Social':10,'Other':5,'paid_search':2,'Affiliates':1,'Display':1 }
st.set_page_config(page_title="Marktine", 
                   page_icon=":M:", 
                   layout="wide")



# Side Bar 

st.sidebar.image("https://marktine.com/wp-content/uploads/2022/01/logo.svg", use_column_width=True)

with st.sidebar:
    st.write("129, Shri Hans Marg, Usha Vihar, Keshav Vihar, Arjun Nagar, Jaipur, Rajasthan 302018")





st.sidebar.header("Please Filter Here:")




try:
    start_date, end_date = st.sidebar.date_input('START DATE  - END DATE :', [])

except:
 st.sidebar.header("Please Select a date ")


st.sidebar.header("Set Channel View distribtuion")


#Main 



try:

    data = user_by_date(start_date,end_date,a)
    st.write(data)
except Exception as e:
    print(e) 
 


st.sidebar.header("Set Channel View distribtuion")


try :
   plt = plot(data)
   st.pyplot(plt)
except Exception as e:
   print(e)
   