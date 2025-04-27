import pandas as pd
import streamlit as st
import plotly.express as px

# file='diabetes.csv'
# data=pd.read_csv(file)
# print(data.head(5))
# print(data.tail(5))



st.set_page_config(page_title="Diabetes Dashboard", layout="wide")

st.title("Diabetes Visualization Dashboard")

data = pd.read_csv('diabetes.csv')

st.subheader("Diabetes Statistics:")

tab1,tab2,tab3=st.tabs(["Glucose","BMI","Age"])


with tab1:
    st.subheader("Glucose Analysis")

    col1,col2=st.columns(2)

    with col1:
        glucose_data = data["Glucose"]
        glucose_data = glucose_data.mean()
        glucose_data=round(glucose_data,2)
        col1.metric("Average Glucose", glucose_data)

    with col2:
        fig_glucose=px.histogram(data,x='Glucose',nbins=40,color_discrete_sequence=["#f5e680"])
        fig_glucose.update_layout(title="Glucose Level Distribution",xaxis_title="Glucose",yaxis_title="Count")
        st.plotly_chart(fig_glucose)

with tab2:
    st.subheader("BMI Analysis")

    col1,col2=st.columns(2)

    with col1:
        bmi_data=data["BMI"]
        bmi_data=bmi_data.mean()
        bmi_data=round(bmi_data,2)
        col1.metric("Average BMI",bmi_data)
    with col2:
        fig_glucose=px.histogram(data,x='BMI',nbins=40,color_discrete_sequence=["#7beef5"])
        fig_glucose.update_layout(title="BMI Level Distribution",xaxis_title="BMI",yaxis_title="Count")
        st.plotly_chart(fig_glucose)


with tab3:
    st.subheader("Age Analysis")
    col1, col2 = st.columns(2)

    with col1:
        age_data=data["Age"]
        age_data = age_data.mean()
        age_data = round(age_data, 2)
        col1.metric("Age ",age_data)
    with col2:
        fig_glucose = px.histogram(data, x='Age', nbins=40, color_discrete_sequence=["skyblue"])
        fig_glucose.update_layout(title="Age Level Distribution", xaxis_title="Age", yaxis_title="Count")
        st.plotly_chart(fig_glucose)

#hw : complete the age tab
# col1, col2, col3 = st.columns(3)
#
# glucose_data = data["Glucose"]
# glucose_data = glucose_data.mean()
#
# col1.metric("Average Glucose", glucose_data)
#
#
# mean_bmi = data["BMI"].mean()
# col2.metric("Average BMI",mean_bmi)

