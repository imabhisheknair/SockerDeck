# Importing useful libraries
import warnings
warnings.filterwarnings('ignore')
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import sklearn.preprocessing as pre
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso

from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,GradientBoostingRegressor,AdaBoostRegressor 
from sklearn.neural_network import MLPRegressor
#import seaborn as sns
import collections
import os
from django.conf import settings


def player_prediction(training_file,input_set):
    # importing data
    data_path =  os.path.join(settings.BASE_DIR, 'data/data.csv')
    players = pd.read_csv(data_path)
    #players.head()
    players.drop(['ID'], axis=1, inplace=True)
    players.drop(['overall'], axis=1, inplace=True)



    # Model to find the best regression model
    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path)
    model_data.head()
    model_data.drop(['ID'], axis=1, inplace=True)
    model_data.drop(['overall'], axis=1, inplace=True)
    model_data.drop(['player_positions'], axis=1, inplace=True)

    #print(model_data['player_positions'].unique())
    #model_data = pd.concat([model_data, pd.get_dummies(model_data['player_positions'], prefix='cut', drop_first=True)],axis=1)
    #model_data.drop(['player_positions'], axis=1, inplace=True)
    #model_data.head()
    #cols = list(model_data)
    #print(cols)
    #model_data.plot.scatter(x='carat', y='price', s=1);

    target_name = 'value_eur'
    #scaler = sk.preprocessing
    robust_scaler = pre.RobustScaler()
    X = model_data.drop('value_eur', axis=1)
    X = robust_scaler.fit_transform(X)
    y = model_data[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123) #20% test
    models = pd.DataFrame(index=['train_mse', 'test_mse'], columns=['NULL', 'MLR', 'Ridge','KNN', 'LASSO'])

    #Null Model
    y_pred_null = y_train.mean()
    models.loc['train_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_train.size),
                                                    y_true=y_train)
    models.loc['test_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_test.size),
                                                   y_true=y_test)

    #Linear Regression
    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    models.loc['train_mse','MLR'] = mean_squared_error(y_pred=linear_regression.predict(X_train), y_true=y_train)
    models.loc['test_mse','MLR'] = mean_squared_error(y_pred=linear_regression.predict(X_test), y_true=y_test)

    #Ridge Regreesion
    # ridge_regression = Ridge()
    # ridge_regression.fit(X_train, y_train)
    # models.loc['train_mse','Ridge'] = mean_squared_error(y_pred=ridge_regression.predict(X_train), y_true=y_train)
    # models.loc['test_mse','Ridge'] = mean_squared_error(y_pred=ridge_regression.predict(X_test), y_true=y_test)


    #KNeighborsRegressor
    # knn = KNeighborsRegressor(n_neighbors=10, weights='distance', metric='euclidean', n_jobs=-1) # k neighbours n =10
    # knn.fit(X_train, y_train)
    # models.loc['train_mse','KNN'] = mean_squared_error(y_pred=knn.predict(X_train), y_true=y_train)
    # models.loc['test_mse','KNN'] = mean_squared_error(y_pred=knn.predict(X_test), y_true=y_test)

    # Lasso Regression
    # lasso = Lasso(alpha=0.1)
    # lasso.fit(X_train, y_train)
    # models.loc['train_mse','LASSO'] = mean_squared_error(y_pred=lasso.predict(X_train), y_true=y_train)
    # models.loc['test_mse','LASSO'] = mean_squared_error(y_pred=lasso.predict(X_test), y_true=y_test)

    # Random Forest Regressor
    # clf_rf = RandomForestRegressor()
    # clf_rf.fit(X_train, y_train)
    # models.loc['train_mse','RF'] = mean_squared_error(y_pred=clf_rf.predict(X_train), y_true=y_train)
    # models.loc['test_mse','RF'] = mean_squared_error(y_pred=clf_rf.predict(X_test), y_true=y_test)
    #diamonds.head()

    # rf_final = RandomForestRegressor(n_estimators =100, n_jobs=-1)
    # rf_final.fit(X, y)


    head_set=['age','height_cm','weight_kg','weak_foot','skill_moves','attacking_crossing',
          'attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling',
          'skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration',
          'movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power',
          'power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions',
          'mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking',
          'defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking',
          'goalkeeping_positioning','goalkeeping_reflexes'] #head
    #input_set=[32,170,72,94,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        print(i)
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    # print(linear_regression.predict(new_data))
    estimate =  linear_regression.predict(new_data)[0]
    restimate = estimate / 1000000
    return restimate
    print('Done')

def player_prediction2(training_file,input_set):
    # importing data
    data_path= training_file#'data.csv'
    players = pd.read_csv(data_path)
    #players.head()
    players.drop(['ID'], axis=1, inplace=True)
    players.drop(['value_eur'], axis=1, inplace=True)






    # Model to find the best regression model
    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path)
    model_data.head()
    model_data.drop(['ID'], axis=1, inplace=True)
    model_data.drop(['value_eur'], axis=1, inplace=True)
    model_data.drop(['player_positions'], axis=1, inplace=True)

    #print(model_data['player_positions'].unique())
    #model_data = pd.concat([model_data, pd.get_dummies(model_data['player_positions'], prefix='cut', drop_first=True)],axis=1)
    #model_data.drop(['player_positions'], axis=1, inplace=True)
    #model_data.head()
    #cols = list(model_data)
    #print(cols)
    #model_data.plot.scatter(x='carat', y='price', s=1);

    target_name = 'overall'
    #scaler = sk.preprocessing
    robust_scaler = pre.RobustScaler()
    X = model_data.drop('overall', axis=1)
    X = robust_scaler.fit_transform(X)
    y = model_data[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    models = pd.DataFrame(index=['train_mse', 'test_mse'], columns=['NULL', 'MLR', 'Ridge','KNN', 'LASSO'])

    #Null Model
    y_pred_null = y_train.mean()
    models.loc['train_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_train.size),
                                                    y_true=y_train)
    models.loc['test_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_test.size),
                                                   y_true=y_test)

    #Linear Regression
    # linear_regression = LinearRegression()
    # linear_regression.fit(X_train, y_train)
    # models.loc['train_mse','MLR'] = mean_squared_error(y_pred=linear_regression.predict(X_train), y_true=y_train)
    # models.loc['test_mse','MLR'] = mean_squared_error(y_pred=linear_regression.predict(X_test), y_true=y_test)

    #Ridge Regression
    ridge_regression = Ridge()
    ridge_regression.fit(X_train, y_train)
    models.loc['train_mse','Ridge'] = mean_squared_error(y_pred=ridge_regression.predict(X_train), y_true=y_train)
    models.loc['test_mse','Ridge'] = mean_squared_error(y_pred=ridge_regression.predict(X_test), y_true=y_test)


    # KNeighborsRegressor
    # knn = KNeighborsRegressor(n_neighbors=10, weights='distance', metric='euclidean', n_jobs=-1)
    # knn.fit(X_train, y_train)
    # models.loc['train_mse','KNN'] = mean_squared_error(y_pred=knn.predict(X_train), y_true=y_train)
    # models.loc['test_mse','KNN'] = mean_squared_error(y_pred=knn.predict(X_test), y_true=y_test)

    # Lasso Regression/
    # lasso = Lasso(alpha=0.1)
    # lasso.fit(X_train, y_train)
    # models.loc['train_mse','LASSO'] = mean_squared_error(y_pred=lasso.predict(X_train), y_true=y_train)
    # models.loc['test_mse','LASSO'] = mean_squared_error(y_pred=lasso.predict(X_test), y_true=y_test)

    # Random Forest Regressor
    # clf_rf = RandomForestRegressor()
    # clf_rf.fit(X_train, y_train)
    # models.loc['train_mse','RF'] = mean_squared_error(y_pred=clf_rf.predict(X_train), y_true=y_train)
    # models.loc['test_mse','RF'] = mean_squared_error(y_pred=clf_rf.predict(X_test), y_true=y_test)
    # #diamonds.head()

    # rf_final = RandomForestRegressor(n_estimators =100, n_jobs=-1)
    # rf_final.fit(X, y)


    head_set=['age','height_cm','weight_kg','weak_foot','skill_moves','attacking_crossing',
          'attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling',
          'skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration',
          'movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power',
          'power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions',
          'mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking',
          'defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking',
          'goalkeeping_positioning','goalkeeping_reflexes']
    #input_set=[32,170,72,94,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        print(i)
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    # print(linear_regression.predict(new_data))
    return ridge_regression.predict(new_data)[0]
    print('Done')


#input_set=[32,170,72,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
#tr_file='../data/data.csv'
#result = player_prediction2(training_file=tr_file,input_set=input_set)
#print(result)
#95500000
#78792000.
#75766000
