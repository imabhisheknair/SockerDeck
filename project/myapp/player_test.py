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
    data_path =  os.path.join(settings.BASE_DIR, 'data/output.csv')
    players = pd.read_csv(data_path)
    #players.head()
    # players.drop(['ID'], axis=1, inplace=True)
    players.drop(['overall'], axis=1, inplace=True)



    # Model to find the best regression model
    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path)
    model_data.drop(['overall'], axis=1, inplace=True)
    model_data.drop('Unnamed: 0',axis=1, inplace=True)
    # model_data.drop(['player_positions'], axis=1, inplace=True)


    target_name = 'value_eur'
    #scaler = sk.preprocessing
    robust_scaler = pre.RobustScaler()
    X = model_data[['passing', 'dribbling', 'movement_reactions', 'power_shot_power', 
    'mentality_composure', 'attacking_short_passing', 'skill_long_passing', 
    'shooting', 'goalkeeping_diving', 'mentality_vision']]
    print(list(X.columns))
    print(list(model_data.columns))


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
    gbr = GradientBoostingRegressor()

    gbr.fit(X_train, y_train)
    models.loc['train_mse','MLR'] = mean_squared_error(y_pred=gbr.predict(X_train), y_true=y_train)
    models.loc['test_mse','MLR'] = mean_squared_error(y_pred=gbr.predict(X_test), y_true=y_test)


    head_set=['passing', 'dribbling', 'movement_reactions', 'power_shot_power', 
    'mentality_composure', 'attacking_short_passing', 'skill_long_passing', 
    'shooting', 'goalkeeping_diving', 'mentality_vision'] #head
    #input_set=[32,170,72,94,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        print(i)
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    # print(gbr.predict(new_data))
    estimate =  gbr.predict(new_data)[0]
    estimate = gbr.predict([[67, 72, 69, 75, 65, 70, 73, 78, 7, 67]])
    restimate = estimate / 1000000
    return restimate
    print('Done')

def player_prediction2(training_file,input_set):
    from sklearn.ensemble import GradientBoostingRegressor

    # importing data
    data_path= training_file#'data.csv'
    players = pd.read_csv(data_path)

    #players.head()
    # players.drop(['ID'], axis=1, inplace=True)
    players.drop(['value_eur'], axis=1, inplace=True)

    # Model to find the best regression model
    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path)
    print(list(model_data.columns))

    model_data.head()
    # model_data.drop(['ID'], axis=1, inplace=True)
    # model_data.drop(['value_eur'], axis=1, inplace=True)
    # model_data.drop(['player_positions'], axis=1, inplace=True)
    #print(model_data['player_positions'].unique())
    #model_data = pd.concat([model_data, pd.get_dummies(model_data['player_positions'], prefix='cut', drop_first=True)],axis=1)
    #model_data.drop(['player_positions'], axis=1, inplace=True)
    #model_data.head()
    #cols = list(model_data)
    #print(cols)
    #model_data.plot.scatter(x='carat', y='price', s=1);
   
    target_name = 'overall'
    model_data.drop('Unnamed: 0',axis=1, inplace=True)

    #scaler = sk.preprocessing
    robust_scaler = pre.RobustScaler()
    # X = model_data.drop('overall', axis=1)
    X = model_data[['passing', 'dribbling', 'movement_reactions', 'power_shot_power', 
    'mentality_composure', 'attacking_short_passing', 'skill_long_passing', 
    'shooting', 'goalkeeping_diving', 'mentality_vision']]
    y = model_data.overall
    print(list(X.columns))

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

    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    # models.loc['train_mse','MLR'] = mean_squared_error(y_pred=gbr.predict(X_train), y_true=y_train)
    # models.loc['test_mse','MLR'] = mean_squared_error(y_pred=gbr.predict(X_test), y_true=y_test)
    head_set=['passing', 'dribbling', 'movement_reactions', 'power_shot_power', 
    'mentality_composure', 'attacking_short_passing', 'skill_long_passing', 
    'shooting', 'goalkeeping_diving', 'mentality_vision'] #head
    #input_set=[32,170,72,94,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        print(i)
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    # print(gbr.predict(new_data))
    # return linear_regression.predict(new_data)[0]
    result = linear_regression.predict([[67, 72, 69, 75, 65, 70, 73, 78, 7, 67]])
    print("overall:", result)
    return result
    print('Done')



#input_set=[32,170,72,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
#tr_file='../data/data.csv'
#result = player_prediction2(training_file=tr_file,input_set=input_set)
#print(result)
#95500000
#78792000.
#75766000
