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

  
  st.write('page4 영화추천')

  genre_='fantasy'
  puid= 'adiv****'
  punick= '푸른불'
  puid=puid[0:4]+'****'
  
  

  

  
  def full_data_learning(genre_):

    connect = sqlite3.connect(f'db/4p/{genre_}_review_noh_1.db', isolation_level=None)
    cursor = connect.cursor()
    col = 'item rating user'
    quary_string = f"select * from {genre_}_review_noh_1 "
    cursor.execute(quary_string)
    
    for i in cursor:
      st.write(i)

    '''
    data_folds = DatasetAutoFolds(ratings_file=cursor)
    trainset = data_folds.build_full_trainset()
    algo = SVD(n_epochs=5, n_factors=500, random_state=0)
    algo.fit(trainset)
    return algo
    '''


  algo = full_data_learning(genre_)
'''
  def mvCd_of_unshow(genre_,puid,punick):
    
    
    connect = sqlite3.connect(f'db/4p/{genre_}_review_noh_1.db', isolation_level=None)
    cursor = connect.cursor()
    
    quary_string = f"select * from {genre_}_review_noh_1"
    cursor.execute(quary_string )
    st.write(cursor)
    
    
    data = cursor, table=(['index','code','score','raw_user', 'userCd','user_id', 'user_nick', 'movie', 'genre','review'])
    str_expr = '(user_id == @puid) and (user_nick == @punick)'
    total = data.code.unique()
    query = data.query(str_expr)['code'].unique()
    indexes = [np.where(total==i)[0][0] for i in query]
    #df_q =np.delete(total,indexes)
    return total

  unshow_mvCd_array = mvCd_of_unshow(genre_,puid,punick)
  def prediction(algo,uid, uia):
    pred = [algo.predict(uid=str(uid), iid=str(isbn)) for isbn in uia]
    ests = lambda x : x.est
    pred.sort(key=ests, reverse=True)
    top10_pred = pred[:10]
    isbn_est_list = [(pr.iid, pr.est) for pr in top10_pred]
    return isbn_est_list
  
  
  user_mvrating_est_list = prediction(algo,puid,unshow_mvCd_array)
  user_mvrating_est_list
  
  def get_recomendationmovie(prediction):
    movies = pd.read_table('db/4p/movie_info_1.db', sep=',', encoding='utf-8', engine='python')
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
  user_movie_recomendation_df.sort_index()
    
  st.write(user_movie_recomendation_df)
  
'''    
