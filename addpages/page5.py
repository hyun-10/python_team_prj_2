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
    df = pd.read_csv(f'db/4p/{i}_review_noh_1.csv',names=['code','score','raw_user', 'userCd','user_id', 'user_nick', 'movie', 'genre','review'], encoding='utf-8', engine='python')
    movie_reviews = pd.concat([data, df])
  movie_reviews = movie_reviews.astype({'code':'str'})
  movie_reviews['select_genre'] = movie_reviews['genre'].apply(lambda x : x.split(',')[0])
  movie_reviews['select_genre'].value_counts()
  
  #code = 	'20226579' # 리뷰없음
  #code = '19190007' # 리뷰있음/드라마 _ 리뷰45개 _ 시각화x
  #code = '19328008' # 리뷰있음/범죄 _ 리뷰42개  _ 시각화x
  #code = '19560023' # 리뷰있음/전쟁 _ 리뷰4개 _ 시각화x
  code = '19770022' # 리뷰있음/SF _ 리뷰32개  _ 시각화x
  #code = '20119397' # 리뷰있음 / 공연 _ 리뷰356개  _ 시각화o
  #code = '19900057' # 리뷰있음 / 성인물 _ 리뷰5개 _ 시각화x
  #code = '20226162' # 리뷰있음/액션  _ 리뷰25개 _ 시각화x
  #code = '19398001'# 리뷰있음/가족 _ 리뷰390개 _ 시각화o
  #code = '19428012' # 리뷰있음/코미디 _ 리뷰13개 _ 시각화x
  #code = '19528001' # 리뷰있음/뮤지컬 _ 리뷰400개  _ 시각화o
  #code = '19588006' # 리뷰있음/스릴러 _ 리뷰58개  _ 시각화o
  #code = '20224198' # 리뷰있음/멜로 _ 리뷰40개  _ 시각화x
  #code = '19598002' # 리뷰있음/애니메이션 _ 리뷰46개  _ 시각화x
  #code = '20225180' # 리뷰있음/공포 _ 리뷰393개  _ 시각화o
  #code = '20225750' # 리뷰있음/미스터리 _ 리뷰8개  _ 시각화x
  #code = '20197434' # 리뷰있음/사극 _ 리뷰3388개  _ 시각화o
  #code = '19880156' # 리뷰있음/판타지 _ 리뷰258개  _ 시각화o
  #code = '19518011' #리뷰있음 / 어드벤처 _ 리뷰14개  _ 시각화x
  #code = '19808231' # 리뷰있음 / 기타 _ 리뷰29개  _ 시각화x
  #code = '20181795' # 리뷰있음 / 서부극 _ 리뷰6개  _ 시각화x
  
  def get_review(query_code,movie_info,movie_reviews):
    select_movie = movie_info[movie_info['영화코드']==code]
    select_movie_review = pd.merge(select_movie, movie_reviews, left_on='영화코드', right_on='code', how='left')
    movie_ = select_movie_review[['영화코드',	'영화이름',	'제작년도',	'상영시간',	'제작상태',	'제작국가',	'장르',	'감독',	'배우',	'스탭수',	'img_url',	'code',	'movie',	'genre']].iloc[0]
    print(movie_)
    bool_review = select_movie_review['review']!=select_movie_review['review']
    if bool_review[0]:
      print('리뷰가 없습니다.')
      select_movie_review = np.nan # 시각화하지않기 위한 장치
    elif len(select_movie_review['review']) <100:
      print(len(select_movie_review['review']),'개의 리뷰가 있습니다.')
      select_movie_review = np.nan # 시각화하지않기 위한 장치
    else :
      print(len(select_movie_review['review']),'개의 리뷰가 있습니다.')
    return   select_movie_review
  
  mv_reviews = get_review(code,movie,movie_reviews)
  
  
  def refined_review(review):
    #세종사전실행
    okt = Okt()
    #단어리스트만들기
    word_list = []
    word_list = review
    #형태소분리
    sentences_tag = []

    for sentence in word_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
    #명사추출
    noun_list = []
    for sentence in sentences_tag:
        for word, tag in sentence:
            if tag in ["Noun"]:
                noun_list.append(word)
    #두글자 이상인 단어만 추출
    noun_list = [n for n in noun_list if len(n) > 1]
    #단어별로 개수세기
    counts = Counter(noun_list)
    tags = counts.most_common(50)
    # 일반적인 단어빼기
    tags=dict(tags)
    stop_words = ['영화', '감독', '배우', 'ㅋㅋ', 'ㅎㅎ', 'ㅠㅠ', '근데', '진짜']

    for word in stop_words:
      if word in tags.keys():
        del tags[word]
    return tags
  
  st.write(mv_reviews)
  
  
  
  
  
  
  
  
  
  
  
  
  
