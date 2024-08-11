import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

'''
This file is created for the visualization
'''

sidebar_name = "Data visualization"

def run():
    st.markdown("""
                In this section we will be creating the visualization of the data.
                
                """)
    
    df = pd.read_csv('application_record.csv')
    
    st.subheader("""
                 
                 Now, let's different type of graphs: """)
    
    
        

    # Pregunta al usuario qué gráfico desea ver
    selected_chart = st.selectbox("Select a chart", ["Bar plot gender", "Bar plot realty", "Bar plot number of children",
                                                     "Comparative number of childre","Bar plot family status", "Pie chart family status",
                                                     "Risky people account", "Housing state","Types of jobs",
                                                     "Annual amount and risk","Boxplot of income","Boxplot of working years",
                                                     "Boxplot of family members"])

    # Prepara el espacio para mostrar la gráfica
    fig, ax = plt.subplots()

    # Muestra el gráfico correspondiente según la selección del usuario
    if selected_chart == "Bar plot gender":
        gender_counts = df['CODE_GENDER'].value_counts()
        color_gen = ['blue','yellow']
        
        fig_gen  = go.Figure(data=[
        go.Bar(x=gender_counts.index, y=gender_counts.values,marker_color=color_gen)])
        
        # Personalizar el diseño y las etiquetas del gráfico
        fig_gen.update_layout(
            title='Distribution of Jobs',
            xaxis=dict(title='Professions', tickangle=45),
            yaxis=dict(title='Count'),
            showlegend=False)
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_gen)
        st.write("Look at the the number of people by gender")
        """
          # Gráfico 1: Distribución de género
        ax.bar(df['CODE_GENDER'].value_counts().index, df['CODE_GENDER'].value_counts().values)
        ax.set_xlabel('Gender')
        ax.set_ylabel('Number of people')
        ax.set_title('Distribution of Gender')
        st.write("This chart displays the distribution of the number of children per household.")
        """
        
        
       
     
        
    elif selected_chart == "Bar plot realty":
        # Gráfico 2: Distribución de la propiedad de vivienda
        ax.bar(df['FLAG_OWN_REALTY'].value_counts().index, df['FLAG_OWN_REALTY'].value_counts().values)
        ax.set_xlabel('Owns Realty')
        ax.set_ylabel('Number of people')
        ax.set_title('Distribution of Owns Realty')
        st.write("This chart displays the distribution of the number of children per household.")
        
    elif selected_chart == "Bar plot number of children":
        # Gráfico 3: Distribución del número de hijos
        ax.bar(df['CNT_CHILDREN'].value_counts().index, df['CNT_CHILDREN'].value_counts().values)
        ax.set_xlabel('Number of children')
        ax.set_ylabel('Number of people')
        ax.set_title('Distribution of Number of Children')
        st.write("This chart displays the distribution of the number of children per household.")
    
    elif selected_chart == "Comparative number of children":
        df_few_children = df[df['CNT_CHILDREN'] <= 3]
        df_many_children = df[df['CNT_CHILDREN'] > 3]

        # Crear una figura con dos subplots
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))

        # Graficar el primer subplot: menos de 4 hijos
        axs[0].bar(df_few_children['CNT_CHILDREN'].value_counts().index, df_few_children['CNT_CHILDREN'].value_counts().values)
        axs[0].set_title('Menos de 3 hijos')
        axs[0].set_xlabel('Número de hijos')
        axs[0].set_ylabel('Número de personas')

        # Graficar el segundo subplot: más de 3 hijos
        axs[1].bar(df_many_children['CNT_CHILDREN'].value_counts().index, df_many_children['CNT_CHILDREN'].value_counts().values)
        axs[1].set_title('Más de 3 hijos')
        axs[1].set_xlabel('Número de hijos')
        axs[1].set_ylabel('Número de personas')
    
    elif selected_chart == "Bar plot family status":
        # Gráfico 1: Gráfico de barras del estado civil
        family_status_counts = df['NAME_FAMILY_STATUS'].value_counts()
        colors_status_fam = plt.cm.tab10.colors[:len(family_status_counts)]
        ax.bar(family_status_counts.index, family_status_counts.values, color=colors_status_fam)
        ax.set_xlabel('Family Status')
        ax.set_ylabel('Count')
        ax.set_title('Distribution of Family Status')
        # Rotar etiquetas del eje x para mayor legibilidad
        #ax.tick_params(axis='x', rotation=45, alignment='right')
        ax.set_xticklabels(family_status_counts.index, rotation=45, ha='right')

        # Muestra la gráfica en Streamlit
        st.write("This chart displays the distribution of family status.")
        #st.pyplot(fig)
        
        
        
    elif selected_chart == "Pie chart family status":
        #family_status_counts = None
        #family_status_counts = df['NAME_FAMILY_STATUS'].value_counts()
        colors = plt.cm.tab10.colors
        explode = [0.1] * len(df['NAME_FAMILY_STATUS'].value_counts())
        plt.pie(df['NAME_FAMILY_STATUS'].value_counts(), labels=df['NAME_FAMILY_STATUS'].value_counts().index, 
                autopct='%1.1f%%', colors=colors, explode=explode)
        plt.title('Family Status of Individuals')
        plt.axis('equal')
        # Muestra la gráfica en Streamlit
        st.write("This chart displays the distribution of family status.")
    
    elif selected_chart == "Risky people account":
        colors_risky= plt.cm.tab10.colors[:len(df.iloc[:,-1])]

        risky_counts = df.iloc[:,-1].value_counts()

        plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico si es necesario
        plt.bar(risky_counts.index, risky_counts.values, color=colors_risky)
        plt.xticks(rotation=45, ha='right')

        plt.xlabel('Risky status')
        plt.ylabel('Count')
        plt.title('Number of people who has risk')
    
    elif selected_chart == "Housing state":
        # Gráfico 1: Gráfico de barras del estado civil
        housing_counts = df['NAME_HOUSING_TYPE'].value_counts()
        colors_housing = plt.cm.tab10.colors[:len(housing_counts)]
        ax.bar(housing_counts.index, housing_counts.values, color=colors_housing)
        ax.set_xlabel('Housing Status')
        ax.set_ylabel('Count')
        ax.set_title('Distribution of Housing Status')
        # Rotar etiquetas del eje x para mayor legibilidad
        #ax.tick_params(axis='x', rotation=45, alignment='right')
        ax.set_xticklabels(housing_counts.index, rotation=45, ha='right')

        # Muestra la gráfica en Streamlit
        st.write("This chart displays the distribution of family status.")
        
    elif selected_chart == "Types of jobs":
        jobs_counts = df['OCCUPATION_TYPE'].value_counts()
        # Crear el gráfico de barras con Plotly
        
        # Definir una paleta de colores personalizada
        colors_jobs = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 
               'rgb(148, 103, 189)', 'rgb(140, 86, 75)', 'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
               'rgb(188, 189, 34)', 'rgb(23, 190, 207)']
        
        fig = go.Figure(data=[
        go.Bar(x=jobs_counts.index, y=jobs_counts.values, marker_color=colors_jobs)
    ])
    
         # Personalizar el diseño y las etiquetas del gráfico
        fig.update_layout(
        title='Distribution of Jobs',
        xaxis=dict(title='Professions', tickangle=45),
        yaxis=dict(title='Count'),
        showlegend=False
    )
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)
        st.write("Look at the the most common type of jobs")
        
        
        """
        jobs_counts = df['OCCUPATION_TYPE'].value_counts()
        colors_jobs = plt.cm.tab10.colors[:len(jobs_counts)]
        ax.bar(jobs_counts.index, jobs_counts.values, color=colors_jobs)
        ax.set_xlabel('Professions')
        ax.set_ylabel('Count')
        ax.set_title('Distribution of jobs')
        # Rotar etiquetas del eje x para mayor legibilidad
        #ax.tick_params(axis='x', rotation=45, alignment='right')
        ax.set_xticklabels(jobs_counts.index, rotation=45, ha='right')
        st.write("Look at the the most common type of jobs") 
        
        """
        
    elif selected_chart == "Annual amount and risk":
        # Gráfico de caja del ingreso total anual por riesgo de préstamo
        plt.figure(figsize=(10, 7))
        
        # Crear listas para los datos 'No arriesgado' y 'Arriesgado'
        no_arriesgado = df[df.iloc[:, -1] == 0]['AMT_INCOME_TOTAL']
        arriesgado = df[df.iloc[:, -1] == 1]['AMT_INCOME_TOTAL']
        
        # Crear el gráfico de caja usando matplotlib
        plt.boxplot([no_arriesgado, arriesgado], labels=['No arriesgado', 'Arriesgado'])
        
        plt.xlabel('Riesgo de Préstamo')
        plt.ylabel('Ingreso Total Anual')
        plt.title('Distribución de Ingreso Total Anual por Riesgo de Préstamo')
        
        st.write("Look at the the most common type of jobs")
        st.pyplot(plt)

    
    elif selected_chart == "Boxplot of family members":
        figbox1 = px.box(df,x=df['NAME_FAMILY_STATUS'],y=df['CNT_FAM_MEMBERS'],
                         title='bola')
        
        #figbox = px.box(df,x=df['Make_Type'],y='Ewltp (g/km)',
             #       color=df['Make_Type'],title='Distribution of emissions according to the brand')
        st.write(figbox1)
        
        

    
    # Rotar etiquetas del eje x para mayor legibilidad
    #ax.tick_params(axis='x', rotation=45)

    # Muestra la gráfica en Streamlit
    st.pyplot(fig)
