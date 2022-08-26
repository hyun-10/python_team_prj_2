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
  
  d1 = pd.read_csv('db/4p/total_reviews_1.csv')
  d2 = pd.read_csv('db/4p/total_reviews_2.csv')
  d3 = pd.read_csv('db/4p/total_reviews_3.csv')
  d4 = pd.read_csv('db/4p/total_reviews_4.csv')
  

  d12 = pd.concat([d1, d2])
  d34 = pd.concat([d3, d4])
  

  movie_reviews = pd.concat([d12,d34])
  
  movie_reviews.drop(['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.2'], axis=1, inplace=True)
  st.write(movie_reviews)
 
 
