import streamlit as st
from surprise import SVD
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise.dataset import DatasetAutoFolds
from surprise import Reader
import pandas as pd
import numpy as np
import sqlite3

def app():
  #genre_='fantasy'
  genre_ = st.selectbox('장르를 선택하세요',('action','adult','adventure','animation','comedy','crime','documentary','drama','etc','family','fantasy','fear','history','melo','musical','mystery','thriller','war','western'))
  genre_ = genre_

  puid = st.text_input('adiv****', key=1)
                    

  punick = st.text_input('푸른불',key=2)
  if punick:
    puid=puid[0:4]+'****'

    def full_data_learning(genre_):
      col = 'item rating user'
      reader = Reader(line_format=col, sep=',', rating_scale=(0,10))
 
      count = 0
      while True :
          try :
              data_folds = DatasetAutoFolds(ratings_file=f'db/4p/{genre_}_review_noh_{str(count)}.csv', reader=reader)
              trainset = data_folds.build_full_trainset()
              algo = SVD(n_epochs=5, n_factors=500, random_state=0)
              algo.fit(trainset)
              break
          except :
              count += 1
      return algo

    algo = full_data_learning(genre_)
  
    def mvCd_of_unshow(genre_,puid,punick):
      data = pd.read_csv(f'db/4p/{genre_}_review_noh_1.csv', names=['code','score','raw_user', 'userCd','user_id', 'user_nick', 'movie', 'genre','review'])
      str_expr = '(user_id == @puid) and (user_nick == @punick)'
      total = data.code.unique()
      query = data.query(str_expr)['code'].unique()
      indexes = [np.where(total==i)[0][0] for i in query]
      df_q =np.delete(total,indexes)
      return df_q
  
    unshow_mvCd_array = mvCd_of_unshow(genre_,puid,punick)
  
    def prediction(algo,uid, uia):
      pred = [algo.predict(uid=str(uid), iid=str(isbn)) for isbn in uia]
      ests = lambda x : x.est
      pred.sort(key=ests, reverse=True)
      top10_pred = pred[:10]
      isbn_est_list = [(pr.iid, pr.est) for pr in top10_pred]
      return isbn_est_list
  
    user_mvrating_est_list = prediction(algo,puid,unshow_mvCd_array)
  
    def get_recomendationmovie(prediction):
      movies = pd.read_table('db/4p/movie_info.csv', sep=',', encoding='utf-8', engine='python')
      mvCd_list = []
      for i in prediction :
        mvCd_list.append(i[0])
      str_expr='영화코드 in @mvCd_list'
      df_q = movies.query(str_expr)
    #추천순위로 정렬하기
      df_q['rank']=0
      rank=1
      for i in prediction:      
        index = df_q.index[df_q['영화코드'] == i[0]]
        df_q.loc[index,'rank']=rank
        rank=rank+1
      return df_q
  
    user_movie_recomendation_df = get_recomendationmovie(user_mvrating_est_list)

    user_movie_recomendation_df = user_movie_recomendation_df.set_index('rank')
    st.dataframe(user_movie_recomendation_df.sort_index())
    index_1 = user_movie_recomendation_df.loc[[1],:]
    index_1_movieNm = index_1.iloc[0]['영화이름']
    index_1_gene = index_1.iloc[0]['장르']
    index_1_directors = index_1.iloc[0]['감독']
    index_1_actors = index_1.iloc[0]['배우']
    index_1_img_url = index_1.iloc[0]['img_url']
    
    index_2 = user_movie_recomendation_df.loc[[2],:]
    index_2_movieNm = index_2.iloc[0]['영화이름']
    index_2_gene = index_2.iloc[0]['장르']
    index_2_directors = index_2.iloc[0]['감독']
    index_2_actors = index_2.iloc[0]['배우']
    index_2_img_url = index_2.iloc[0]['img_url']
    
    index_3 = user_movie_recomendation_df.loc[[3],:]
    index_3_movieNm = index_3.iloc[0]['영화이름']
    index_3_gene = index_3.iloc[0]['장르']
    index_3_directors = index_3.iloc[0]['감독']
    index_3_actors = index_3.iloc[0]['배우']
    index_3_img_url = index_3.iloc[0]['img_url']
    
    index_4 = user_movie_recomendation_df.loc[[4],:]
    index_4_movieNm = index_4.iloc[0]['영화이름']
    index_4_gene = index_4.iloc[0]['장르']
    index_4_directors = index_4.iloc[0]['감독']
    index_4_actors = index_4.iloc[0]['배우']
    index_4_img_url = index_4.iloc[0]['img_url']
    
    index_5 = user_movie_recomendation_df.loc[[5],:]
    index_5_movieNm = index_5.iloc[0]['영화이름']
    index_5_gene = index_5.iloc[0]['장르']
    index_5_directors = index_5.iloc[0]['감독']
    index_5_actors = index_5.iloc[0]['배우']
    index_5_img_url = index_5.iloc[0]['img_url']
    
    index_6 = user_movie_recomendation_df.loc[[6],:]
    index_6_movieNm = index_6.iloc[0]['영화이름']
    index_6_gene = index_6.iloc[0]['장르']
    index_6_directors = index_6.iloc[0]['감독']
    index_6_actors = index_6.iloc[0]['배우']
    index_6_img_url = index_6.iloc[0]['img_url']
    
    index_7 = user_movie_recomendation_df.loc[[7],:]
    index_7_movieNm = index_7.iloc[0]['영화이름']
    index_7_gene = index_7.iloc[0]['장르']
    index_7_directors = index_7.iloc[0]['감독']
    index_7_actors = index_7.iloc[0]['배우']
    index_7_img_url = index_7.iloc[0]['img_url']
    
    index_8 = user_movie_recomendation_df.loc[[8],:]
    index_8_movieNm = index_8.iloc[0]['영화이름']
    index_8_gene = index_8.iloc[0]['장르']
    index_8_directors = index_8.iloc[0]['감독']
    index_8_actors = index_8.iloc[0]['배우']
    index_8_img_url = index_8.iloc[0]['img_url']
    
    index_9 = user_movie_recomendation_df.loc[[9],:]
    index_9_movieNm = index_9.iloc[0]['영화이름']
    index_9_gene = index_9.iloc[0]['장르']
    index_9_directors = index_9.iloc[0]['감독']
    index_9_actors = index_9.iloc[0]['배우']
    index_9_img_url = index_9.iloc[0]['img_url']
    
    index_10 = user_movie_recomendation_df.loc[[10],:]
    index_10_movieNm = index_10.iloc[0]['영화이름']
    index_10_gene = index_10.iloc[0]['장르']
    index_10_directors = index_10.iloc[0]['감독']
    index_10_actors = index_10.iloc[0]['배우']
    index_10_img_url = index_10.iloc[0]['img_url']
    
    
    st.write(index_10)
    #st.image(index_1[0]['img_url'])
    
    st.image(index_10.iloc[0]['img_url'])
    st.write(index_10_movieNm)
    st.write(index_10_gene)
    st.write(index_10_directors)
    st.write(index_10_actors)
    
    
    col1, col2, col3, col4, col5= st.columns(5)

    col_list=[col1,col2,col3,col4,col5]
    for i in range(1,6):
        with col_list[i]:
        

        st.image(index_i.iloc[0]['img_url'])
        st.write(index_i_movieNm)
        st.write(index_i_gene)
        st.write(index_i_directors)
        st.write(index_i_actors)
    
