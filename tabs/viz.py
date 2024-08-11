import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

'''
This file is created for the visualization
'''

sidebar_name = "Data visualization"

def run():
    st.markdown("""
                In this section we will be creating the visualization of the data.
                
                """)
    
    df = pd.read_csv('application_record.csv')

    
    df1 = pd.read_csv('df_good.csv')
    
    st.subheader("""
                 
                 Now, let's see different type of graphs. Choose one: """)
    
    # Pregunta al usuario qué gráfico desea ver
    selected_chart = st.selectbox("Select a chart", ["Bar plot gender", "Bar plot realty", "Bar plot number of children",
                                                     "Comparative number of children","Bar plot family status", "Pie chart family status",
                                                     "Risky people account", "Housing state","Types of jobs",
                                                     "Annual amount and risk","Box plot of income",
                                                     ])

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
        
        
    elif selected_chart == "Bar plot realty":
        # Gráfico 2: Distribución de la propiedad de vivienda
        realty_counts = df['FLAG_OWN_REALTY'].value_counts()
        color_realty = ['green', 'red']
        
        fig_realty = go.Figure(data=[
            go.Bar(x=realty_counts.index, y=realty_counts.values, marker_color=color_realty)
        ])
        
        # Personalizar el diseño y las etiquetas del gráfico
        fig_realty.update_layout(
            title='Distribution of Owns Realty',
            xaxis=dict(title='Owns Realty', tickangle=45),
            yaxis=dict(title='Count'),
            showlegend=False
        )
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_realty)
        st.write("This chart displays the distribution of owns realty.")
        
    elif selected_chart == "Bar plot number of children":
        # Filtrar los datos para mostrar solo hasta 10 hijos
        df_filtered = df[df['CNT_CHILDREN'] <= 10]
        children_counts = df_filtered['CNT_CHILDREN'].value_counts().sort_index()
        color_children = px.colors.qualitative.Plotly
        
        fig_children = go.Figure(data=[
            go.Bar(x=children_counts.index, y=children_counts.values, marker_color=color_children[:len(children_counts)])
        ])
        
        # Personalizar el diseño y las etiquetas del gráfico
        fig_children.update_layout(
            title='Distribution of Number of Children',
            xaxis=dict(title='Number of Children (up to 10)', tickangle=45),
            yaxis=dict(title='Count'),
            showlegend=False
        )
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_children)
        st.write("This chart displays the distribution of the number of children per household (up to 10 children).")
    
    elif selected_chart == "Comparative number of children":
        df_few_children = df[df['CNT_CHILDREN'] <= 3]
        df_many_children = df[df['CNT_CHILDREN'] > 3]

        few_children_counts = df_few_children['CNT_CHILDREN'].value_counts().sort_index()
        many_children_counts = df_many_children['CNT_CHILDREN'].value_counts().sort_index()
        
        fig_comparative = make_subplots(rows=1, cols=2, subplot_titles=('Less than or equal to 3 children', 'More than 3 children'))

        # Añadir el primer subplot: menos de 4 hijos
        fig_comparative.add_trace(
            go.Bar(x=few_children_counts.index, y=few_children_counts.values, marker_color='blue'),
            row=1, col=1
        )

        # Añadir el segundo subplot: más de 3 hijos
        fig_comparative.add_trace(
            go.Bar(x=many_children_counts.index, y=many_children_counts.values, marker_color='red'),
            row=1, col=2
        )

        # Personalizar el diseño y las etiquetas del gráfico
        fig_comparative.update_layout(
            title_text='Comparative Number of Children',
            xaxis=dict(title='Number of Children', tickangle=0),
            yaxis=dict(title='Count'),
            showlegend=False
        )
    
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_comparative)
        st.write("This chart compares the distribution of the number of children per household.")
    
    

        
    elif selected_chart == "Pie chart family status":
        # Calcular el conteo de estados civiles
        family_status_counts = df['NAME_FAMILY_STATUS'].value_counts()

        # Configurar los colores para cada segmento del gráfico
        colors = px.colors.qualitative.Plotly

        # Crear el gráfico circular (pie chart) con Plotly
        fig_pie = go.Figure(data=[
            go.Pie(labels=family_status_counts.index, values=family_status_counts.values, 
                textinfo='label+percent', marker=dict(colors=colors))
        ])

        # Personalizar el diseño y las etiquetas del gráfico
        fig_pie.update_layout(
            title='Family Status of Individuals',
            showlegend=False,
            width=750,
            height=550,
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_pie)
        st.write("This chart displays the distribution of family status.")
    
    elif selected_chart == "Risky people account":
        colors_risky = px.colors.qualitative.Plotly
    
        # Calcular conteo de personas con riesgo
        risky_counts = df1['Risky_1'].value_counts()

        # Crear gráfico de barras con Plotly
        fig_risky = go.Figure(data=[
            go.Bar(x=risky_counts.index, y=risky_counts.values, marker_color=colors_risky)
        ])

        # Personalizar el diseño y las etiquetas del gráfico
        fig_risky.update_layout(
            title='Number of People with Risk',
            xaxis=dict(title='Risky Status', tickangle=45),
            yaxis=dict(title='Count'),
            showlegend=False
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_risky)
        st.write("This chart displays the number of people considered risky for being approved for a credit card")
        
    elif selected_chart == "Housing state":
        # Gráfico 1: Gráfico de barras del tipo de vivienda
        housing_counts = df['NAME_HOUSING_TYPE'].value_counts()

        fig_housing = go.Figure(data=[
            go.Bar(x=housing_counts.index, y=housing_counts.values, marker_color=px.colors.qualitative.Plotly)
        ])

        # Personalizar el diseño y las etiquetas del gráfico
        fig_housing.update_layout(
            title='Distribution of Housing Status',
            xaxis=dict(title='Housing Status', tickangle=45),
            yaxis=dict(title='Count'),
            showlegend=False
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_housing)
        st.write("This chart displays the distribution of housing status.")
        
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
        
        

    elif selected_chart == "Annual amount and risk":

        # Crear el gráfico de caja con Plotly
        fig_risk = go.Figure()

        # Añadir los box plots para cada categoría de riesgo
        fig_risk.add_trace(go.Box(x=df1['Risky_1'][df1['Risky_1'] == 0],
                                y=df1['AMT_INCOME_TOTAL'][df1['Risky_1'] == 0],
                                name='No risky'))
        fig_risk.add_trace(go.Box(x=df1['Risky_1'][df1['Risky_1'] == 1],
                                y=df1['AMT_INCOME_TOTAL'][df1['Risky_1'] == 1],
                                name='Risky'))

        # Personalizar el diseño y las etiquetas del gráfico
        fig_risk.update_layout(
            title='Distribution of annual income per risk',
            xaxis=dict(title='Risky of approving the loan', tickvals=[0, 1], ticktext=['Not risky', 'Risky']),
            yaxis=dict(title='Total annual income'),
            showlegend=True,
            width=700,  # Ajustar el ancho del gráfico
            height=500,  # Ajustar la altura del gráfico
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_risk)
        st.write("This chart displays the distribution of annual income by loan risk.")
    
    elif selected_chart == "Boxplot of income":
        
        mean = df1['AMT_INCOME_TOTAL'].mean()
        std_dev = df1['AMT_INCOME_TOTAL'].std()

        # Definir los límites
        lower_limit = mean - 3 * std_dev
        upper_limit = mean + 3 * std_dev

        # Eliminar los outliers
        df_income= df1[(df1['AMT_INCOME_TOTAL'] >= lower_limit) & (df1['AMT_INCOME_TOTAL'] <= upper_limit)]


        # Crear el gráfico de caja con Plotly
        fig_box_income = go.Figure()

        # Añadir el box plot
        fig_box_income.add_trace(go.Box(
            y=df_income['AMT_INCOME_TOTAL'],
            name='Income',
        ))

        # Personalizar el diseño y las etiquetas del gráfico
        fig_box_income.update_layout(
            title='Income Distribution',
            yaxis=dict(title='Income'),
            showlegend=False,
            width=700,  # Ajustar el ancho del gráfico
            height=500  # Ajustar la altura del gráfico
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_box_income)
        st.write("This chart displays the distribution of income.")
        st.write(f"Mean income: {mean}")
        st.write(f"Standard deviation of income: {std_dev}")
        st.write(f"Lower limit: {lower_limit}")
        st.write(f"Upper limit: {upper_limit}")

# Ejecutar la aplicación de Streamlit
if __name__ == "__main__":
    run()   
