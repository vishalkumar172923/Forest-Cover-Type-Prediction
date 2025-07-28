import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import pickle
from PIL import Image

# Loads model
rfc=pickle.load(open("rfc.pkl",'rb'))

st.title("Forest Cover Type Prediction") 

img=Image.open('0_Forest_Cover_image.png')
st.image(img, caption='Forest Cover', use_container_width=True)




user_input=st.text_input("Enter All the Forest Cover Types")   


if(user_input):
    user_input=user_input.split(',') 
    features=np.array([user_input], dtype=np.float64) 
    prediction=rfc.predict(features).reshape(1,-1)
    prediction=int(prediction[0])
    

    img_dict={
        1 : {"name" : "Spruce/Fir" ,        "image" : "1_SpruceFir.jpg"},
        2 : {"name" : "Lodgepole Pine" ,    "image" : "2_ Lodgepole_Pine.jpg"},
        3 : {"name" : "Lodgepole Pine" ,    "image" : "3_Ponderosa_Pine.jpg"},
        4 : {"name" : "Cottonwood/Willow" , "image" : "4_ Cottonwood_Willow.jpg"},
        5 : {"name" : "Aspen" ,             "image" : "5_Aspen.jpg"},
        6 : {"name" : "Douglas-fir" ,       "image" : "6_ Douglas_fir.jpg"},
        7 : {"name" : "Krummholz" ,         "image" : "7_ Krummholz.jpg"}
    }


    cover_type_info= img_dict.get(prediction)

    if cover_type_info is not None:
        forest_name=cover_type_info['name']
        forest_image=cover_type_info['image']


        col1,col2= st.columns([2,3])
        with col1:
            st.write("The Predicted Cover Type is")
            st.write(f"<h1 style=' font-size:50px, font-weight:bold '>{forest_name}</h1>",unsafe_allow_html=True)

        with col2:
            final_image= Image.open(forest_image)
            st.image(final_image, caption='Forest Cover', use_container_width=True)
    