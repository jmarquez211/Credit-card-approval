import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
#from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import numpy as np


title = "Approval risk"
sidebar_name ="Context"

def run():
    
    st.markdown('Prediction of credit approval')
    #st.image('/home/jmarquez211/Projects/Python/Tutoriales/Gradient Boosting/creditcard/tabs')
    
    st.markdown(
    """
    Here are the principal features you can select if you want
    to know if the credit will be approved or not.
    """
    )
    
    #df = pd.read_csv('df_good.csv')
    df_application = pd.read_csv('application_record.csv')
    df_credit = pd.read_csv('credit_record.csv')
    starter_month=pd.DataFrame(df_credit.groupby(['ID'])['MONTHS_BALANCE'].agg(min))
    starter_month=starter_month.rename(columns={'MONTHS_BALANCE':'Account day'})
    df_application=pd.merge(df_application,starter_month,how='left',on='ID')

    df_credit['dep_value'] = None
    df_credit['dep_value'][df_credit['STATUS'] =='2']='Yes'
    df_credit['dep_value'][df_credit['STATUS'] =='3']='Yes'
    df_credit['dep_value'][df_credit['STATUS'] =='4']='Yes'
    df_credit['dep_value'][df_credit['STATUS'] =='5']='Yes'

    cpunt=df_credit.groupby('ID').count()
    cpunt['dep_value'][cpunt['dep_value'] > 0]='Yes'
    cpunt['dep_value'][cpunt['dep_value'] == 0]='No'
    cpunt = cpunt[['dep_value']]

    df_application = pd.merge(df_application,cpunt,how='inner',on='ID')
    df_application['Risky']=df_application['dep_value']
    df_application.loc[df_application['Risky']=='Yes','Risky']=1
    df_application.loc[df_application['Risky']=='No','Risky']=0
    df_application.drop('dep_value',axis=1,inplace=True)
    df_application.drop('ID',axis=1,inplace=True)
    df_application['OCCUPATION_TYPE'].fillna(df_application['OCCUPATION_TYPE'].mode()[0], inplace=True)
    
    st.write(df_application.head())
    
    
    df = pd.read_csv('df_good.csv')

    df_dummies = pd.get_dummies(data = df[["FLAG_OWN_REALTY","NAME_INCOME_TYPE","NAME_EDUCATION_TYPE",
                                                   "NAME_FAMILY_STATUS","NAME_HOUSING_TYPE","OCCUPATION_TYPE",
                                                   "Risky"]], drop_first = True)

    df_num_features=df.select_dtypes(include=np.number)

    df = pd.concat([df_num_features, df_dummies], axis = 1)
    
    target = df['Risky']
    feats = df.drop('Risky', axis=1)
    
    

    X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.2)
    #st.write(y_train)
    #st.write(y_test)
    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)
    gradient_boosting_model = GradientBoostingRegressor(random_state=42)
    gradient_boosting_model.fit(X_train, y_train)
    #st.write(y_test.shape)
    gb_predictions = gradient_boosting_model.predict(X_test)
    
    
    
    alpha_model = ['Gradient Boosting Regressor','Random Forest Regressor']
    
    def use_model(model_name):
        if model_name == "Gradient Boosting Regressor":
            #alpha = st.selecbox("Select the model:",alpha_model)
            return 
        elif model_name == "Random Forest Regressor":
            alpha = st.selecbox("Select the model:",alpha_model)
    
    # Function to obtain the metric selected by the user
    def get_scoring_metric(model_name):
        if model_name in ["GBR", "Random Forest Regressor"]:
            
            return st.radio("Select scoring metric", ["score", "mean_squared_error"])
            
    
    model_name = st.selectbox("Selec the model for predictions",["Gradient Boost","Random Forest"])
    model = use_model(model_name)
    
    if model_name in ["Gradient Boosting Regressor", "Random Forest Regressor"]:
        # showing the metrics for each model
        scoring_metric = get_scoring_metric(model_name)
        
        if scoring_metric:
            
            st.write("Selected scoring metric:", scoring_metric)
    
    if st.button("Show results"):
        st.write("Results: ")
        
        model.fit(X_train,y_train)
        predictions = model.predict(X_test)
        
        if scoring_metric:
            if scoring_metric == "score" or scoring_metric == "mean_squared_error":
                score = model.score(X_test, y_test)
                st.write("Score:", score)
                
                # this is a dataframe, to show it better
                df_pred = pd.DataFrame({"Predictions": predictions})
        
                # a little changes for representation
                df_pred = df_pred.rename(columns={"Predictions": "Risky"})
                st.write('The predictions for every car are:')
                st.write(df_pred)
                
            elif scoring_metric == "r2_score":
                r2 = r2_score(y_test, predictions)
                st.write("R2 Score:", r2)
    
    st.markdown('---')