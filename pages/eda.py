import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("📈 Exploratory Data Analysis (EDA)")
    
    # Load data
    df = pd.read_csv('data/anime.csv')
    
    # Display a sample of the dataset
    st.write("### Dataset Sample")
    st.dataframe(df.head())
    
    # Visualization
    st.write("### Distribution of Anime Ratings")
    
    # Example plot
    fig, ax = plt.subplots()
    df['rating'].hist(ax=ax, bins=20, color='skyblue')
    ax.set_title('Distribution of Anime Ratings')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')
    
    st.pyplot(fig)
