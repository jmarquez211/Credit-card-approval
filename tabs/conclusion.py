import streamlit as st 


sidebar_name = "Conclusion"

def run():
    
    
    st.title("The main goal")
    st.markdown("""
                This project aimed to develop a reliable credit approval prediction system using machine 
                learning models. By analyzing an extensive dataset of application records and credit history, 
                we strived to determine whether an applicant is likely to be approved for credit based on various 
                factors. Our models, Gradient Boosting Classifier and AdaBoost Classifier, were employed to enhance 
                the accuracy of these predictions.
                """)
    
    
    st.markdown("""
                
                ### Project Conclusion

                This project aimed to develop a reliable credit approval prediction system using machine learning models. By analyzing an extensive dataset of application records and credit history, we strived to determine whether an applicant is likely to be approved for credit based on various factors. Our models, Gradient Boosting Classifier and AdaBoost Classifier, were employed to enhance the accuracy of these predictions.

                #### Key Insights

                1. **Data Preparation**:
                - We integrated data from application records and credit history, creating a comprehensive dataset that includes personal and financial information.
                - Handling missing values, especially for variables like `OCCUPATION_TYPE`, was crucial to maintain data integrity and model performance.
                - We converted the `DAYS_EMPLOYED` and `DAYS_BIRTH` variables to more interpretable formats (years), making the dataset more intuitive.

                2. **Feature Selection**:
                - Our model utilized various features, including `AMT_INCOME_TOTAL`, `DAYS_BIRTH`, `DAYS_EMPLOYED`, `FLAG_OWN_CAR`, and `FLAG_OWN_REALTY`.
                - Categorical variables like `NAME_EDUCATION_TYPE`, `NAME_INCOME_TYPE`, and `OCCUPATION_TYPE` were also considered, as they provide insights into the applicant's background and stability.

                3. **Model Training and Evaluation**:
                - We split our data into training and testing sets to evaluate the performance of the models effectively.
                - The Gradient Boosting Classifier and AdaBoost Classifier were chosen for their robustness and ability to handle various types of data.
                - Evaluation metrics such as Mean Squared Error (MSE) and R2 Score were used to assess the models' accuracy.

                4. **User Interface**:
                - A Streamlit-based application was developed to allow users to input their details and get a prediction on their credit approval status.
                - Features like sliders and drop-downs made it easy for users to enter information such as income, age, years of experience, and ownership of assets like cars and realty.

                #### Conclusion

                While the models predict credit approval with reasonable accuracy, it's important to understand that no model is perfect. Certain variables, such as income and employment status, undeniably play significant roles in determining creditworthiness. However, they are not the sole determinants. The context of each applicant's situation, such as their spending habits, existing debts, and overall financial stability, must also be considered.

                The project highlights the importance of combining various data points to make informed predictions. For potential applicants, it's a reminder that while models can provide a probabilistic outcome, human judgment and a holistic view of their financial health are essential. Financial institutions should use these models as supplementary tools rather than definitive decision-makers.

                In the future, the system could be improved by incorporating more diverse data sources, like transaction histories and social factors, to enhance prediction accuracy. Additionally, providing explanations for each prediction can help applicants understand their credit profiles better and take steps to improve their creditworthiness.

                This project underscores the potential of machine learning in finance while emphasizing the need for responsible and context-aware application of technology in credit risk assessment.
                    """)
