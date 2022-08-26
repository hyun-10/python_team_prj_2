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
  d5 = pd.read_csv('db/4p/total_reviews_5.csv')
  d6 = pd.read_csv('db/4p/total_reviews_6.csv')
  d7 = pd.read_csv('db/4p/total_reviews_7.csv')
  d8 = pd.read_csv('db/4p/total_reviews_8.csv')
  d9 = pd.read_csv('db/4p/total_reviews_9.csv')
  d10 = pd.read_csv('db/4p/total_reviews_10.csv')
  d12 = pd.concat(map(pd.read_csv, [d1, d2]), ignore_index=True)
  st.writd(d12)
 
  

  
  
  
