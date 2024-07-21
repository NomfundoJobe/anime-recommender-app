import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Anime Recommender System", page_icon=":star:", layout="wide")

# Sidebar menu for navigation
selected = st.sidebar.radio("Menu", ["Home", "Meet the Team", "Project Overview", "EDA"])

# Page content based on selection
if selected == "Home":
    st.title("Welcome to the Anime Recommender System!")
    st.image("https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/203/509/datas/original.png", caption="Explore the World of Anime", use_column_width=True)
    st.markdown("""
        Dive into our anime recommender system and discover your next favorite show! 🌟
        Our system provides personalized recommendations based on your preferences, helping you explore the vast world of anime. Whether you're looking for action, romance, or adventure, we've got you covered!
    """)

elif selected == "Meet the Team":
    import pages.team as team
    team.show()

elif selected == "Project Overview":
    import pages.project_overview as project_overview
    project_overview.show()

elif selected == "EDA":
    import pages.eda as eda
    eda.show()
