import requests
# pip install streamlit-lottie
import streamlit as st
# from streamlit_lottie import st_lottie

st.set_page_config(page_title='Asia cup Analysis',layout='wide')
# st.title("Asia Cup Data")
# st.text(" ") 
st.image("/home/tejas/Downloads/Asia_cup.jpg")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    
    return r.json()

# 
lottie_coding=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_1fXD2hXInk.json")
# with st.container():
# #     right_column=st.columns(2)
# #     with right_column:
st_lottie(lottie_coding, height=300, key='coding')
    
# # st.markdown("""---""")

# st.beta_columns
import streamlit as st 
import pandas as pd  
import numpy as np
import pickle  #to load a saved modelimport base64  #to open .gif files in streamlit app


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv('/home/tejas/Downloads/asiacup.csv')
col1=['Opponent','Format','Selection','Avg Bat Strike Rate','Highest Score','Wicket Taken','Given Extras','Highest Individual wicket','Run Rate','Extras']
df1=df.drop(col1,axis=1)
Df=df1.head(10)
# with st.sidebar:
#     st.table(Df)
df2=df1.dropna()
df2.head(10)
# option = st.selectbox(
#     'How would you like to see?',
#     (' Number of times Team won the toss.', 'Number of times Team won the result.', 'Number of matches done on different ground.',"Top 5 player of Match."," Number of times the Team get all out."))
st.markdown("# CHOOSE THE OPTION")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Number of times Team won the toss.", "Number of times Team won the result.", "Number of matches done on different ground.","Top 5 player of Match."," Number of times the Team get all out."])

with tab1:
    st.markdown("Q1.} Number of times Team won the toss.")
    df3=df2[df2['Toss']=='Win']
    df3.head(10)
    df4=df3['Team'].value_counts()
    df4
    chart = df4.plot.bar(y='Team', figsize=(10, 5),xlabel='Teams',ylabel='Toss_winning')
    st.line_chart(df4)

with tab2:
    st.markdown("Q2.}Number of times Team won the result.")
    df5=df2[df2['Result']=='Win']
    df5.head(10)
    df6=df5['Team'].value_counts()
    df6
    st.bar_chart(df6)
    
with tab3:
    st.markdown("Q3.}Number of matches done on different ground")
    df7=df1['Ground'].value_counts()
    df7
    st.bar_chart(df7)
    
with tab4:
    st.markdown("Q4.}Top 5 player of Match")
    df8=df1['Player Of The Match'].value_counts()
    df9=df8.head(5)
    df9
    st.bar_chart(df9)
    
with tab5:
    st.markdown("Q5.} Number of times the Team get all out.")
    df10=df1[df1['Wicket Lost']==10.0]
    df11=df10['Team'].value_counts()
    df11
    st.line_chart(df11)
    
st.markdown("""---""")
    
# st.radio('Which is your favourite Team?',['India','Sri Lanka','Pakisthan','Bangladesh','Afghanistan','Hong Kong','UAE'])
# st.markdown("""---""")
st.markdown("# #Number of times a Team won and Loss the Match.")

df12=df[['Team','Result']]
# df12
df13=df12[['Team', 'Result']].value_counts().reset_index(name='count')
df14=df13.sort_values(by=['Result'])
# df14
df15=df14.drop([13,16,12,15,14])
# df15
st.bar_chart(df15,x='Team',y='count',height=500)

st.markdown("""---""")

st.markdown("# #Run scored by different Teams in different Year")

df16=df[['Team','Run Scored','Year']]
# df16
df17=df16.sort_values(by=['Team'])
# df17
df18=df17.drop([56,57])
df18
df19=df18[df18['Team']=='Afghanistan']
df20=df19.mean()
# df20
# st.markdown("""---""")

df21=df18[df18['Team']=='Bangladesh']
df22=df21.mean()
# df22
# st.markdown("""---""")
df23=df18[df18['Team']=='Hong Kong']
df24=df23.mean()
# df24
# st.markdown("""---""")
df25=df18[df18['Team']=='India']
df26=df25.mean()
# df26
df27=df18[df18['Team']=='Pakistan']
df28=df27.mean()
# df28
# st.markdown("""---""")
df29=df18[df18['Team']=='Sri Lanka']
df30=df29.mean()
# df30
# # st.line_chart(df19, y='Run Scored',x='Year')
# df20=df18[df18['Team']=='Sri Lanka']
# # st.line_chart(df19, y='Run Scored',x='Year')
# df21=df18[df18['Team']=='Pakisthan']
# # st.line_chart(df19, y='Run Scored',x='Year')

# # st.line_chart(df19, y='Run Scored',x='Year')
st.markdown("""---""")
st.markdown("# #Average run scored by the Team in Asia Cup")

data=[['Afghanistan',187.42],['Bangladesh',185.06],['Hong Kong',135.75],['India',213.68],['Pakistan',217.55],['Sri Lanka',212.55]]
df31 = pd.DataFrame(data, columns=['Team', 'Average_score'])
df31
# st.bar_chart(df31, y='Average_score',x='Team')
st.markdown("""---""")

import streamlit as st
import extra_streamlit_components as stx
st.markdown("# #Details of match of team India differentiated by runs.")

# chosen_id1= stx.tab_bar(Team=[
#     stx.TabBarItemData(id="Tab1", title='India'),
#     stx.TabBarItemData(id="Tab2", title="Sri Lanka"),


chosen_id= stx.tab_bar(data=[
    stx.TabBarItemData(id="tab1", title="Below 100", description="Match Details of Team India getting less than 100 runs"),
#     st.text(""),
    stx.TabBarItemData(id="tab2", title="100-200", description="Match Details of Team India getting runs between 100 and 200"),
#     st.text(""),
    stx.TabBarItemData(id="tab3", title="200-300", description="Match Details of Team India getting runs between 200 and 300"),
#     st.text(""),
    stx.TabBarItemData(id="tab4", title="Above 300", description=" Match Details of Team India getting more than 300 runs")])


placeholder = st.container() 

if chosen_id == "tab1":
    placeholder.markdown(f"## Welcome to `{chosen_id}`")
    placeholder.info(f"Since we are in {chosen_id}, So details of matches of team India when they scored below 100 is:")
    df32=df[df['Team']=='India']
    df33=df32[df32['Run Scored']<100.0000]
#     with st.sidebar:
    st.table(df33)
    
    
#     placeholder.image("https://placekitten.com/g/400/200",caption=f"Meowhy from {chosen_id}")
#     placeholder.slider("A slider",0,10,5,1)
#     placeholder.checkbox("A checkbox",True)
#     placeholder.button("A button")

elif chosen_id == "tab2":
    placeholder.markdown(f"## Welcome to `{chosen_id}`")
    placeholder.info(f"Since we are in {chosen_id} , So details of matches of team India when then scored between 100 and 200 is:")
    df34=df[df['Team']=='India']
    df35=df34[(df34['Run Scored']>100.0000)&(df34['Run Scored']<200.0000)]
#     with st.sidebar:
    st.table(df35)

elif chosen_id == "tab3":
    placeholder.markdown(f"## Welcome to `{chosen_id}`")
    placeholder.info(f"Since we are in {chosen_id}, So details of matches of team India when they scored between 200 and 300 is:")
    df36=df[df['Team']=='India']
    df37=df36[(df36['Run Scored']>200.0000)&(df36['Run Scored']<300.0000)]
#     with st.sidebar:/
    st.table(df37)
         
elif chosen_id == "tab4":
    placeholder.markdown(f"## Welcome to `{chosen_id}`")
    placeholder.info(f"Since we are in {chosen_id}, So details of matches of team India when they scored above 300 is:")
    df38=df[df['Team']=='India']
    df39=df38[df38['Run Scored']>300.0000]
#     with st.sidebar:
    st.table(df39)
        
# import streamlit as st
# from streamlit_javascript import st_javascript

# url = st_javascript("await fetch('').then(r => window.parent.location.href)")

# st.write(url)        
# st.markdown("""
# **** 
# ### Don't forget to `pip install extra_streamlit_components`
# # """)
# df23=[['df19','df20']]
# df23
# df23 = pd.DataFrame(columns=['df19','df20'])
# st.line_chart(df23)

# columns=['df19','df20']
# result = df16.loc[df16['India'] == 1, 'Run Scored'].sum()
# result

# st.selectbox('Which is your favourite Team',['India','Sri Lanka','Pakisthan','Bangladesh','Afghniastan','Hong Kong','UAE'])    
# # st.write('You selected:', option)
# st.markdown("""---""")
# st.markdown("Q1.} Number of times Team won the toss.")
# df3=df2[df2['Toss']=='Win']
# df3.head(10)
# df4=df3['Team'].value_counts()
# df4
# chart = df4.plot.bar(y='Team', figsize=(10, 5),xlabel='Teams',ylabel='Toss_winning')
# st.line_chart(df4)
# st.markdown("""---""")
# st.markdown("Q2.}Number of times Team won the result.")
# df5=df2[df2['Result']=='Win']
# df5.head(10)
# df6=df5['Team'].value_counts()
# df6
# st.bar_chart(df6)
# st.markdown("""---""")
# st.markdown("Q3.}Number of matches done on different ground")
# df7=df1['Ground'].value_counts()
# df7
# st.bar_chart(df7)
# st.markdown("""---""")
# st.markdown("Q4.}Top 5 player of Match")
# df8=df1['Player Of The Match'].value_counts()
# # df8
# df9=df8.head(5)
# df9
# st.bar_chart(df9)
# st.markdown("""---""")
# st.markdown("Q5.} Number of times the Team get all out.")
# df10=df1[df1['Wicket Lost']==10.0]
# # df10
# df11=df10['Team'].value_counts()
# df11
# st.line_chart(df11)
