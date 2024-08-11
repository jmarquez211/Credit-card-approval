import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


title = "Testing the model"
sidebar_name = "Models"


def run():
    
    df = pd.read_csv('df_good.csv')
    numerical_data = df._get_numeric_data()
    num_cols = numerical_data.columns

    scaler = StandardScaler()
    numercial_df = pd.DataFrame(scaler.fit_transform(numerical_data), columns= num_cols, index=df.index)
    df_dummies = pd.get_dummies(data = df[["FLAG_OWN_REALTY","NAME_INCOME_TYPE","NAME_EDUCATION_TYPE",
                                                   "NAME_FAMILY_STATUS","NAME_HOUSING_TYPE","OCCUPATION_TYPE",
                                                   "Risky"]], drop_first = True)

    df_num_features=df.select_dtypes(include=np.number)

    df = pd.concat([df_num_features, df_dummies], axis = 1)
    
    target = df['Risky']
    feats = df.drop('Risky', axis=1)

    X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.2)
    st.write(X_train)
    st.write(X_test)
    
    # 1. Entrenar el modelo
    gbr_model = GradientBoostingRegressor()
    gbr_model.fit(X_train, y_train)
    
    # 2. Evaluar la precisión
    y_pred = gbr_model.predict(X_test)
    r2_gbr = r2_score(y_test)
    st.write("Using the Gradient Boost Regressor")
    #st.write(r2_gbr)
    st.write(y_train.shape)
    st.write(y_test.shape)
    
    
