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
  #movie_reviews = pd.read_csv('data/total_reviews.csv')
  #movie_reviews (f'db/4p/{action}_review_noh_1.csv")
  #action_review_noh_1.csv,adult_review_noh_1.csv,adventure_review_noh_1.csv,animation_review_noh_1.csv,comedy_review_noh_1.csv,crime_review_noh_1.csv,documentary_review_noh_1.csv,drama_review_noh_1.csv,etc_review_noh_1.csv,family_review_noh_1.csv,fantasy_review_noh_1.csv,fear_review_noh_1.csv,history_review_noh_1.csv,melo_review_noh_1.csv,musical_review_noh_1.csv,mystery_review_noh_1.csv,thriller_review_noh_1.csv,war_review_noh_1.csv,western_review_noh_1.csv
  data= pd.read_csv('db/4p/action_review_noh_1.csv', names=['code','score','raw_user', 'userCd','user_id', 'user_nick', 'movie', 'genre','review'])
  for i in ('adult','adventure','animation','comedy','crime','documentary','drama','etc','family','fantasy','fear','history','melo','musical','mystery','thriller','war','western'):
    df = pd.read_csv(f'db/4p/{i}_review_noh_1.csv')
    movie_reviews = pd.concat([data, df])
  st.write(movie_reviews)
                 
  #f'db/4p/{action}_review_noh_1.csv'
  #action_review_noh_1.concat
  #st.write(movie_reviews)
  
