import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('metadata_sample.csv')

# Title and description
st.title('Publication Data Explorer')
st.write('Explore publication data by year and source. Use the widgets below to filter and visualize the dataset.')

# Interactive widgets
years = pd.to_datetime(df['publish_time']).dt.year.unique()
selected_year = st.slider('Select Year', int(min(years)), int(max(years)), int(min(years)))
sources = df['source_x'].unique()
selected_source = st.selectbox('Select Source', sources)

# Filter data
filtered_df = df[(pd.to_datetime(df['publish_time']).dt.year == selected_year) & (df['source_x'] == selected_source)]

# Show sample of data
st.subheader('Sample of Filtered Data')
st.dataframe(filtered_df.head())

# Visualization: Bar chart of source frequencies
st.subheader('Source Frequency (All Data)')
fig1, ax1 = plt.subplots()
df['source_x'].value_counts().plot(kind='bar', ax=ax1)
ax1.set_xlabel('Source')
ax1.set_ylabel('Count')
st.pyplot(fig1)

# Visualization: Line graph of publications per year
st.subheader('Publications Per Year (All Data)')
df['year'] = pd.to_datetime(df['publish_time']).dt.year
year_counts = df['year'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
ax2.plot(year_counts.index, year_counts.values, marker='o')
ax2.set_xlabel('Year')
ax2.set_ylabel('Count')
ax2.set_title('Number of Publications Per Year')
st.pyplot(fig2)
