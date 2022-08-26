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
 
  data= pd.read_csv('db/4p/action_review_noh_1.csv', names=['code','score','raw_user', 'userCd','user_id', 'user_nick', 'movie', 'genre','review'])
  
  for i in ('adult','adventure','animation','comedy','crime','documentary','drama','etc','family','fantasy','fear','history','melo','musical','mystery','thriller','war','western'):
    df = pd.read_csv(f'db/4p/{i}_review_noh_1.csv', encoding='utf-8', engine='python')
    movie_reviews = pd.concat([data, df])
  movie_reviews = movie_reviews.astype({'code':'str'})
  st.write(movie_reviews['genre'])

  
  
  
