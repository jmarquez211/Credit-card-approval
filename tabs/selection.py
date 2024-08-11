import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler

sidebar_name = "Selection"

def run():
    st.markdown("Select your features and predict if you're acceptable for the credit")
    
    
    # Load datasets 
    df_application = pd.read_csv('main/tabs/application_record.csv')
    df_credit = pd.read_csv('credit_record.csv')
    
    # Process data
    starter_month = pd.DataFrame(df_credit.groupby(['ID'])['MONTHS_BALANCE'].agg(min))
    starter_month = starter_month.rename(columns={'MONTHS_BALANCE':'Account day'})
    df_application = pd.merge(df_application, starter_month, how='left', on='ID')

    df_credit['dep_value'] = np.where(df_credit['STATUS'].isin(['2', '3', '4', '5']), 'Yes', None)

    cpunt = df_credit.groupby('ID').count()
    cpunt['dep_value'] = np.where(cpunt['dep_value'] > 0, 'Yes', 'No')
    cpunt = cpunt[['dep_value']]

    df_application = pd.merge(df_application, cpunt, how='inner', on='ID')
    df_application['Risky'] = np.where(df_application['dep_value'] == 'Yes', 1, 0)
    df_application.drop(['dep_value', 'ID'], axis=1, inplace=True)
    
    df_application['OCCUPATION_TYPE'].fillna(df_application['OCCUPATION_TYPE'].mode()[0], inplace=True)
    
    df_application['DAYS_EMPLOYED'] = df_application['DAYS_EMPLOYED'].abs() / 365
    df_application['DAYS_BIRTH'] = df_application['DAYS_BIRTH'].abs() / 365
    
    df = pd.read_csv('df_good.csv')
    df.rename(columns={"Risky_1": "Risky"}, inplace=True)
    
    target = df['Risky']
    feats = df.drop('Risky', axis=1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=1/3, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Initialize the model
    model = GradientBoostingClassifier()

    st.write("---")
    st.markdown("Select your features:")

    # Sliders for selecting the values
    gender = st.slider('Your gender (0: Female, 1: Male)', 0, 1, key='gender_slider')
    children = st.slider('How many children do you have?', 0, 19, step=1, key='children_slider')
    income = int(st.text_input("Put down your income in $", 0, key='income_input'))
    age = st.slider('Your age', 20, 69, key='age_slider')
    work = st.slider('Select your years of experience', 0, 43, step=1, key='work_slider')
    car = st.slider('Do you have a car? (0: No, 1: Yes)', 0, 1, key='car_slider')
    realty = st.slider('Do you have a house or realty? (0: No, 1: Yes)', 0, 1, key='realty_slider')
    
    # Selección de variable categórica y su valor
    categorical_variables = ['NAME_EDUCATION_TYPE', 'NAME_INCOME_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'OCCUPATION_TYPE']
    selected_variable = st.selectbox('Select a categorical variable:', categorical_variables, key="categorical_variable_select")
    unique_values = df_application[selected_variable].unique()
    selected_value = st.selectbox(f'Select a value for {selected_variable}:', unique_values, key="selected_value_select")
    
    # Map the selected value to a numeric value
    value_mapping = {value: index for index, value in enumerate(unique_values)}
    numeric_value = value_mapping[selected_value]

    # Predict button
    if st.button("Predict", key='predict_button'):
        input_data = pd.DataFrame({
            'gender': [gender],
            'children': [children],
            'AMT_INCOME_TOTAL': [income],
            'DAYS_BIRTH': [age],
            'DAYS_EMPLOYED': [work],
            'FLAG_OWN_CAR': [car],
            'FLAG_OWN_REALTY': [realty],
            selected_variable: [numeric_value]
        })
        
        # Ensure input_data has all required features
        missing_cols = set(feats.columns) - set(input_data.columns)
        for col in missing_cols:
            input_data[col] = 0
        
        input_data = input_data[feats.columns]  # Reorder columns to match training data
        
        # Normalize input data
        input_data = scaler.transform(input_data)
        
        # Fit the model on the training data
        model.fit(X_train, y_train)
        
        # Predict the classification
        classification = model.predict(input_data)[0]
        
        # Display the result based on the prediction
        if classification == 1:
            st.write("# It is safe to grant the credit. Congratulations!")
            st.balloons()
        else:
            st.write("## Our apologies, it is not safe to grant the credit.")
        
        st.write('---')

run()


