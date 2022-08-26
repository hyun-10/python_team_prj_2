import streamlit as st
import pandas as pd

import numpy as np

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image # 워드클라우드용 마스크를 생성하기위한 라이브러리 import
from wordcloud import ImageColorGenerator
import os





def app():
  
  st.write('page5')
  
  
  movie = pd.read_csv('db/4p/movie_info.csv')
  movie = movie.astype({'영화코드':'str'})
 
  da_1= pd.read_csv('db/4p/action_review_noh_1.csv')
  da_2= pd.read_csv('db/4p/adult_review_noh_1.csv')
  da_3= pd.read_csv('db/4p/adventure_review_noh_1.csv')
  da_4= pd.read_csv('db/4p/animation_review_noh_1.csv')
  da_5= pd.read_csv('db/4p/comedy_review_noh_1.csv')
  da_6= pd.read_csv('db/4p/crime_review_noh_1.csv')
  da_7= pd.read_csv('db/4p/documentary_review_noh_1.csv')
  da_8= pd.read_csv('db/4p/drama_review_noh_1.csv')
  da_9= pd.read_csv('db/4p/etc_review_noh_1.csv')
  da_10= pd.read_csv('db/4p/family_review_noh_1.csv')
  da_11= pd.read_csv('db/4p/fantasy_review_noh_1.csv')
  da_12= pd.read_csv('db/4p/fear_review_noh_1.csv')
  da_13= pd.read_csv('db/4p/history_review_noh_1.csv')
  da_14= pd.read_csv('db/4p/melo_review_noh_1.csv')
  da_15= pd.read_csv('db/4p/musical_review_noh_1.csv')
  da_16= pd.read_csv('db/4p/mystery_review_noh_1.csv')
  da_17= pd.read_csv('db/4p/thriller_review_noh_1.csv')
  da_18= pd.read_csv('db/4p/war_review_noh_1.csv')

  
  #for i in ('adult','adventure','animation','comedy','crime','documentary','drama','etc','family','fantasy','fear','history','melo','musical','mystery','thriller','war','western'):
    #df = pd.read_csv(f'db/4p/{i}_review_noh_1.csv', encoding='utf-8', engine='python')
  movie_reviews = pd.concat([da_1,da_2,da_3,da_4,da_5,da_6,da_7,da_8,da_9,da_10,da_11,da_12,da_13,da_14,da_15,da_16,da_17,da_18])
  st.write(movie_reviews)
 
  

  
  
  
