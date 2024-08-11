import streamlit as st 
import shap
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle


title = 'Interpretability'
sidebar_name = 'Interpretability'

def guardar_modelo(modelo, ruta):
    with open(ruta, 'wb') as archivo:
        pickle.dump(modelo, archivo)


def cargar_modelo(ruta):
    with open(ruta, 'rb') as archivo:
        modelo_cargado = pickle.load(archivo)
    return modelo_cargado

def run():
    
    df = pd.read_csv('df_good.csv')
    st.write(df)
    st.write(df.info())
    
    
    target = df['Risky_1']
    feats = df.drop('Risky_1', axis=1)

    X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.2)
    
    # Convertir y_train y y_test en arreglos unidimensionales
    y_train = np.array(y_train).ravel()
    y_test = np.array(y_test).ravel()
    
    params = {'objective': 'binary:logistic', 'max_depth':6, 'eval_metric':'logloss'}

    dtrain = xgb.DMatrix(X_train,label=y_train)

    dtest = xgb.DMatrix(data=X_test,label=y_test)


    bst = xgb.train(params,dtrain,1000)
    
    guardar_modelo(bst, 'modelo_xgboost.pkl')
    modelo_cargado = cargar_modelo('modelo_xgboost.pkl')
    
    explainer = shap.TreeExplainer(modelo_cargado,
                               data = X_train,
                               model_output="probability")

    shap_values = explainer.shap_values(X_test)
    #st.write("Expected value:")
    #st.write(explainer.expected_value)
    
    shap1 = shap.summary_plot(shap_values,X_test,plot_type='bar')
    st.write(shap1)
    
    
    
    explanation = explainer(df)
    st.write(shap.plots.beeswarm(explanation))
    
    st.write(shap.summary_plot(shap_values,X_test))
    
    #shap.initjs()
    st.write("<script src='https://cdn.jsdelivr.net/npm/shap@0.39.0/dist/shap.min.js'></script>", unsafe_allow_html=True)


    st.write(shap.force_plot(explainer.expected_value,shap_values[3,:],X_test.iloc[3,:]))
    
   
    