import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header('st.write')
st.markdown('---')
st.subheader('sub st.write')

st.write('Hello,*World!* :sunglasses:')

st.write(1234)
df= pd.DataFrame({'col1':[1,2,3,4,5,6,7,8],
                  'index':['a','b','c','d','e','f','g','h']})
st.write(df)

st.write('Below is a DataFrame:',df,'Above is a DataFrame')

df2 =pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)
c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',color='c',tooltip=['a','b','c']
)
st.write(c)

code='''def hello():
        print("Hello,Streamlit!")'''
st.code(code,language='python')