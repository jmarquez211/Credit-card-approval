import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_curve, auc, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

title = "Testing the model"
sidebar_name = "Models"

def plot_roc(model, X_test, y_test):
    # Obtener las probabilidades de predicción para la clase positiva
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)
    else:
        y_prob = model.decision_function(X_test)
        
    if y_prob.ndim > 1:  # Verificar si hay más de una dimensión
        fpr0, tpr0, _ = roc_curve(y_test, y_prob[:, 0], pos_label=0)
        fpr1, tpr1, _ = roc_curve(y_test, y_prob[:, 1], pos_label=1)
    else:
        fpr0, tpr0, _ = roc_curve(y_test, y_prob, pos_label=0)
        fpr1, tpr1, _ = roc_curve(y_test, 1 - y_prob, pos_label=1)
    
    roc_auc0 = auc(fpr0, tpr0)
    roc_auc1 = auc(fpr1, tpr1)
    
   
    
    # Plotear la curva ROC
    plt.figure(figsize=(8, 6))
    plt.plot(fpr0, tpr0, color='blue', label=f'ROC curve for Risky=0 (AUC = {roc_auc0:.2f})')
    plt.plot(fpr1, tpr1, color='red', label=f'ROC curve for Risky=1 (AUC = {roc_auc1:.2f})')
    plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
    


def plot_confusion_matrix_table(model, X_test, y_test):
    predictions = model.predict(X_test)
    cm = confusion_matrix(y_test, predictions)
    cm_df = pd.DataFrame(cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])
    st.write("Confusion Matrix, table form:")
    st.table(cm_df.style.set_properties(**{'font-size': '16pt', 'border-collapse': 'collapse'}))






def run():
    
    df = pd.read_csv('df_good.csv')
    df.rename(columns={"Risky_1":"Risky"}, inplace=True)
    

    target = df['Risky']
    feats = df.drop('Risky', axis=1)

    X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.2, random_state=42)
    
    model_name = st.selectbox("Choose Model", ['Logistic Regression', 'Support Vector Machine', 'Decision Tree Classifier', 'Random Forest Classifier',
                                               'Gaussian Naive Bayes', 'Ada boost', 'Gradient Boosting Classifier'],key='model_selectbox')

    model = None
    
    # Crear los modelos según la selección del usuario
    if model_name == 'Logistic Regression':
        model = LogisticRegression()
    elif model_name == 'Support Vector Machine':
        model = SVC()
    elif model_name == 'Decision Tree Classifier':
        model = DecisionTreeClassifier()
    elif model_name == 'Random Forest Classifier':
        model = RandomForestClassifier()
    elif model_name == 'Gaussian Naive Bayes':
        model = GaussianNB()
    elif model_name == 'Ada boost':
        model = AdaBoostClassifier()
    elif model_name == 'Gradient Boosting Classifier':
        model = GradientBoostingClassifier()

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Preddiciones
    predictions = model.predict(X_test)

    # Métricas de evaluación
    metric = st.radio("Choose Metric", ('Accuracy', 'Recall', 'F1 Score'),key='metric_radio')

    if metric == 'Accuracy':
        value = accuracy_score(y_test, predictions)
    elif metric == 'Recall':
        value = recall_score(y_test, predictions)
    elif metric == 'F1 Score':
        value = f1_score(y_test, predictions)

    st.write(f"Using the {model_name}, {metric} is: {value}")
    
    
    plot_roc(model, X_test, y_test)
    
    # Mostrar la matriz de confusión
    plot_confusion_matrix_table(model, X_test, y_test)
    

run()
    
