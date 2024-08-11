import streamlit as st
import pandas as pd


title = "Approval risk"
sidebar_name = "Context"

def run():
    st.title("Could I get a credit card?")
    
    
    
    st.markdown(""" 
                
                Have you ever wondered what one can need to get a credit card?
                
                Are there many prerequisites? 
                
                How can I know if I could been approved to obtain that credit? 
                
                Do I need a lot of saved money?
                
                
                Shall I need to be married? 
                
                """)
    
    
    st.image("images/credit_card_approved.png")
    
    st.markdown("## The main goal of this project")
    
    st.markdown("""
                Throughout the sections the user will be able to navigate and select different kind of plots,
                features, models of machine learning in order to determinate if with some specific characteristics someone
                can be selected to obtain the credit card.
                
        Here are the principal features you can select if you want
        to know if the credit will be approved or not.
    """)

    # Cargar datos
    df_application = pd.read_csv('application_record.csv')
    
    st.write(df_application.head())
    
    
    st.markdown("""
                
                ### Project Introduction

                Welcome to our Credit Approval Prediction System. This project is designed to help individuals and financial institutions assess the likelihood of credit approval based on a variety of personal and financial factors. Using advanced machine learning techniques, we analyze extensive datasets to provide an informed prediction about an applicant's creditworthiness.

                #### What This Project Does

                1. **Data Integration**:
                - We combine data from multiple sources, including application records and credit history, to build a comprehensive profile of each applicant.

                2. **Feature Analysis**:
                - Key variables such as income, employment status, age, and asset ownership are considered to determine their impact on credit approval.

                3. **Model Training and Evaluation**:
                - Two robust machine learning models, the Gradient Boosting Classifier and AdaBoost Classifier, are trained and evaluated to ensure accurate predictions.

                4. **User Interaction**:
                - Through an intuitive Streamlit interface, users can input their details and receive immediate feedback on their credit approval status.
                - Features like sliders and drop-down menus make it easy for users to enter relevant information and understand the outcome.

                #### How to Use This App

                - **Step 1**: Select your features using the sliders and drop-down menus provided. These features include your income, age, years of work experience, and ownership of assets like cars and realty.
                - **Step 2**: Choose the machine learning model you prefer: Gradient Boosting Classifier or AdaBoost Classifier.
                - **Step 3**: Click on the "Show Results" button to get an instant prediction of your credit approval status.

                This project aims to demystify the credit approval process and provide users with a transparent and accessible way to understand their credit profiles. While the system offers valuable insights, it's important to remember that these predictions are based on statistical models and should be considered as one of many tools in assessing creditworthiness.

                We hope this tool helps you gain a better understanding of how credit decisions are made and what factors are most influential. Thank you for using our Credit Approval Prediction System!
                    """)
