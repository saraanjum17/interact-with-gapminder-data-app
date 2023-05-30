import streamlit as st
import pandas as pd
import plotly.express as px

#Titles the Streamlit app
#Changes settings so the plot will take up more space
st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

#Imports all the gapminder data as a dataframe
df = pd.read_csv("Data/gapminder_tidy.csv")

#Defines lists of all the continents and metrics possible
continents_list = list(df['continent'].unique())
metrics_list = list(df['metric'].unique())

#Defines metric labels for nicer display names
metric_labels = {metrics_list[0]:"GDP per Capita", metrics_list[1]:"Average Life Expectancy", metrics_list[2]:"Population"}

#Defines a format function to format the metric options in the sidebar
def format_func(raw_metric):
    return metric_labels[raw_metric]

#Creates a sidebar in which to put the dropdown boxes
with st.sidebar:
    #Adds a subheader
    st.subheader("Configure the Plot")
    
    #Defines the desired continent and metric
    #format_func needs the options argument
    #It iterates through every item in the options list and puts it through the format function
    continent = st.selectbox(label = "Choose a continent", options = continents_list)
    metric = st.selectbox(label = "Choose a metric", options = metrics_list, format_func = format_func)

#Defines the query according to the inputs, allowing for a flexible inquiry
query = f"continent == '{continent}' & metric == '{metric}'"

#Creates a sub-dataframe with GDP per capita data from the continent of Oceania
df_gdp_o = df.query(query)

#Plots the figure, displays it
title = f"{metric_labels[metric]} for Countries in {continent}"
fig = px.line(df_gdp_o, x = "year", y = "value", color = "country", title = title, labels = {"year":"Year","value": f"{metric_labels[metric]}"})
st.plotly_chart(fig, use_container_width = True)

#Includes the markdown text to explain the graphic
st.markdown(f"This plot shows the {metric_labels[metric]} for countries in {continent}.")

#Displays the dataframe if desired
show_data = False
if show_data:
    st.dataframe(df_gdp_o)