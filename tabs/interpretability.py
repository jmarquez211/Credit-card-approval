import streamlit as st 


title = 'Interpretability'
sidebar_name = 'Interpretability'


def run():
    
    #st.markdown("## Hey")
    st.markdown("""
                ## This section is for the user to interpret the main features to determinate if someone is going to be approved or not
                """)
    st.write(""" 
             The graphs were made with a command of the library SHAP generates a bar plot that visualizes the SHAP (SHapley Additive exPlanations) values for a machine learning model.
             
             The SHAP summary plot is designed to provide insights into the importance of each feature in the dataset with respect to the model's predictions.
             It helps in understanding which features have the most significant impact on the model's output.
             
             Y-axis: The features of the dataset. Each bar represents a single feature.
             X-axis: The mean absolute SHAP value for each feature. This value indicates the average impact of the feature on the model's predictions 
             across all the samples.
             """)
    
    st.image("/home/jmarquez211/Escritorio/creditcard/tabs/images/shapvalues.png",width=550)
    
    st.subheader("Interpreteting the bars")
    st.markdown(""" The length of each bar represents the average magnitude of the SHAP values for that feature.
                Longer bars indicate features that are more important to the model, meaning they have a higher average impact on the predictions.
                Shorter bars indicate features that are less important.""")
    
    
    st.subheader("SHAP values")
    
    st.markdown("""
                    SHAP values quantify the contribution of each feature to the prediction of each sample.
                    A positive SHAP value means that the feature increases the predicted value, while a negative 
                    SHAP value means it decreases the predicted value.
                    In this bar plot, only the magnitude (absolute value) of the SHAP values is considered to show the importance 
                    of each feature, regardless of the direction of the impact.
                """)
    
    st.markdown(""" 
                This plot helps us understand which features are most influential in the model's decision-making process.
                It provides transparency by showing how much each feature contributes to the model's predictions on average.
                
                Features with longer bars are more important and should be prioritized for further analysis or potential data
                collections efforts. Features with very short bars might be candidates for removal, as they have little 
                impact on the model's prediction.
                """)
    
    st.subheader("Beeswarm plot")
    
    st.markdown(""" 
                The SHAP beeswarm plot is designed to show the distribution of SHAP values for each feature across all samples in the dataset.
                It provides a comprehensive view of how each feature affects the model’s predictions, highlighting both the importance and the direction of the impact.
                """)
    st.image("/home/jmarquez211/Escritorio/creditcard/tabs/images/shap1.png",width=800)
    
    st.markdown(""" ### Understanding the SHAP Beeswarm Plot""")
    
    st.markdown(""" 
                The SHAP beeswarm plot is designed to show the distribution of SHAP values for each feature across all samples in the dataset.
                It provides a comprehensive view of how each feature affects the model’s predictions, highlighting both the importance and the direction of the impact.
                
                """)
    
    st.markdown(""" ### Components of the plot""")
    st.markdown("""
                Y-axis: The features of the dataset, ordered by their importance. The most important features are at the top.
                X-axis: The SHAP values. These values indicate the impact of each feature on the model’s output for each sample.
                Dots: Each dot represents a SHAP value for a particular feature in a single sample.
                Color: The color of the dots represents the value of the feature, usually ranging from low (blue) to high (red).
                """)
    
    st.markdown(""" ### Interpreting the dots""")
    st.markdown(""" 
                The position of each dot on the X-axis shows the SHAP value for that feature in a particular sample.
                Dots to the right of the center (positive SHAP values) indicate that the feature increases the predicted value, while dots to the left (negative SHAP values) indicate that the feature decreases the predicted value.
                The spread of the dots along the X-axis gives a sense of the variability in the feature’s impact.
                """)
    
    st.markdown("### Feature impact and interaction")
    
    st.markdown(""" 
                The vertical spread of the dots for each feature indicates the range of its impact on the model's predictions.
                A wide spread means the feature has a significant impact on different samples.
                The color gradient within each feature’s dots shows how the feature value affects its SHAP value.
                
                """)
    
    st.markdown(""" 
                *Overall Feature Importance*: Features at the top of the plot are more important overall. They have a more significant impact on the model’s predictions.
                
                *Direction of Impact*: The horizontal position of the dots shows whether a feature increases or decreases the prediction.
                
                *Feature Value Effects*: The color of the dots helps us understand how the actual feature values relate to their SHAP values. For example, higher values of a feature might lead to higher SHAP values and thus higher predictions.
                """)
    
    st.markdown(""" 
                The SHAP summary plot and the SHAP beeswarm plot both visualize the impact of features on model output, but they serve slightly different purposes. The SHAP summary plot, especially when displayed as a bar plot, 
                provides an overview of the average importance of each feature, ranking them by their contribution to model predictions. This makes it useful for quickly identifying the most influential features. On the other hand,
                the SHAP beeswarm plot offers a more detailed view by showing the distribution of SHAP values for individual predictions. Each point represents a SHAP value for a specific feature and data instance, color-coded by feature value,
                which helps in understanding how different feature values impact predictions. The beeswarm plot is particularly useful for detecting interactions between features and identifying patterns or outliers in the data.
                """)
    
   
    
