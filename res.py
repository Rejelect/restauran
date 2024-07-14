import streamlit as st
import pandas as pd

df = pd.read_csv('restaurant_data.csv')

st.title('Restaurant Dashboard')

st.header('Restaurant Data')
st.write(df)

st.sidebar.header('Filters')

location = st.sidebar.multiselect(
    'Select Location',
    options=df['Location'].unique(),
    default=df['Location'].unique()
)

cuisine = st.sidebar.multiselect(
    'Select Cuisine',
    options=df['Cuisine'].unique(),
    default=df['Cuisine'].unique()
)

filtered_df = df[(df['Location'].isin(location)) & (df['Cuisine'].isin(cuisine))]

st.header('Filtered Data')
st.write(filtered_df)

st.header('Statistics')

avg_rating = filtered_df['Rating'].mean()
st.write(f'Average Rating: {avg_rating:.2f}')

total_revenue = filtered_df['Revenue'].sum()
st.write(f'Total Revenue: ${total_revenue:,.2f}')

st.subheader('Seating Capacity Distribution')
st.bar_chart(filtered_df['Seating Capacity'])

st.subheader('Average Meal Price Distribution')
st.bar_chart(filtered_df['Average Meal Price'])

st.subheader('Ambience Score Distribution')
st.bar_chart(filtered_df['Ambience Score'])

st.subheader('Service Quality Score Distribution')
st.bar_chart(filtered_df['Service Quality Score'])
