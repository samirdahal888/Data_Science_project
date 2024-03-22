import streamlit as st
import pandas as pd
import pickle
css='''
<style>
.st-emotion-cache-uf99v8 {
    display: flex;
    flex-direction: column;
    width: 100%;
    overflow: auto;
    -webkit-box-align: center;
    align-items: center;
    background-color: #506855;
}
</style>
'''



st.markdown(css, unsafe_allow_html=True)


st.markdown(' # **PredictPeak**')

no_of_bed=st.sidebar.slider("Choose number of bedrooms:",1,99,10)
no_of_bath=st.sidebar.slider("Choose number of bathrooms:",1,198,10)
house_size=st.sidebar.slider("house size in sqfit:",487,156244,2000)
state=st.sidebar.selectbox("select the state",('California','Colorado','Connecticut','Delaware','District of Columbia','Georgia','Maine','Maryland','Massachusetts','New Hampshire', 'New Jersey','New York','Ohio','Pennsylvania','Puerto Rico', 'Rhode Island','Vermont','Virgin Islands','Virginia', 'West Virginia', 'Wyoming'))


def user_input():
   
    data={
        'no_of_bed':no_of_bed,
        'no_of_bath':no_of_bath,
        'house_size':house_size,
        'state':state


    }
    features=pd.DataFrame(data,index=[0])

    return features

data=user_input()
st.write(data)


state_corr_value={'California': 0,
 'Colorado': 1,
 'Connecticut': 2,
 'Delaware': 3,
 'District of Columbia': 4,
 'Georgia': 5,
 'Maine': 6,
 'Maryland': 7,
 'Massachusetts': 8,
 'New Hampshire': 9,
 'New Jersey': 10,
 'New York': 11,
 'Ohio': 12,
 'Pennsylvania': 13,
 'Puerto Rico': 14,
 'Rhode Island': 15,
 'Vermont': 16,
 'Virgin Islands': 17,
 'Virginia': 18,
 'West Virginia': 19,
 'Wyoming': 20}

def get_value():
    for keys, values in state_corr_value.items():
        if state == keys:
            print(int(values))
            return keys,values


key,value = get_value()
st.write()
st.write("## State and its labeled value:",key,value)


with open('pickel_model','rb') as f:
   model= pickle.load(f)



st.write("# predicted price according to your input in $")
   
st.write(model.predict([[no_of_bed,no_of_bath,house_size,value]]))

data = pd.DataFrame({
        'latitude' : [40.7128, 34.0522, 41.8781, 29.7604, 39.9526],
         'longitude' : [-74.0060, -118.2437, -87.6298, -95.3698, -75.1652]
})
st.write(" ## USA MAP")
st.map(data)