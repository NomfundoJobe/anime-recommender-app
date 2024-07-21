import streamlit as st

def show():
    st.title("📊 Project Overview")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .overview-section {
            background-color: #e8f4f8;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .overview-section h2 {
            color: #0073e6;
        }
        .overview-section p {
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="overview-section">', unsafe_allow_html=True)
    
    st.write(
        """
        ## Project Goals
        Our goal is to develop an advanced recommender system for anime using both content-based and collaborative filtering approaches. 

        ## Features
        - **Content-Based Filtering**: Recommends anime based on the user's previous interactions and preferences.
        - **Collaborative Filtering**: Suggests anime based on the preferences of similar users.
        - **Interactive Visualization**: Provides insights through interactive data visualizations.

        ## Technologies Used
        - Python
        - Streamlit
        - Pandas
        - Scikit-learn
        """
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
