import streamlit as st
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image # 워드클라우드용 마스크를 생성하기위한 라이브러리 import
from wordcloud import ImageColorGenerator
import os



fontpath = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=fontpath)
fm._rebuild()

def app():
  
  st.write('page5')
  
  
  movie = pd.read_csv('db/4p/movie_info.csv')
  movie = movie.astype({'영화코드':'str'})
  #movie_reviews = pd.read_csv('data/total_reviews.csv')
  movie_reviews = os.path.join('db/4p/CSV_files', "*_review_noh_1.csv")
  #action_review_noh_1.csv,adult_review_noh_1.csv,adventure_review_noh_1.csv,animation_review_noh_1.csv,comedy_review_noh_1.csv,crime_review_noh_1.csv,documentary_review_noh_1.csv,drama_review_noh_1.csv,etc_review_noh_1.csv,family_review_noh_1.csv,fantasy_review_noh_1.csv,fear_review_noh_1.csv,history_review_noh_1.csv,melo_review_noh_1.csv,musical_review_noh_1.csv,mystery_review_noh_1.csv,thriller_review_noh_1.csv,war_review_noh_1.csv,western_review_noh_1.csv
  
  #action_review_noh_1.concat
  st.write(movie_reviews)
