import streamlit as st

def show():
    st.title("👥 Our Team")
    st.markdown(
        """
        <style>
        .team-section {
            background-color: #f4f4f9;
            border-radius: 10px;
            padding: 20px;
        }
        .team-member {
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .team-member h3 {
            color: #0073e6;
        }
        .team-section h2 {
            color: #0073e6;
        }
        .team-section p {
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="team-section">', unsafe_allow_html=True)
    
    st.write(
        """
        ## Welcome to Our Team
        👋 Hello and welcome! Meet the talented team behind the Anime Recommender System. We are dedicated to helping you explore the world of anime with our advanced recommendations. 

        ### Team Members
        """
    )
    
    # Team Member 1
    st.markdown(
        """
        <div class="team-member">
            <h3>Nomfundo Sithole</h3>
            <p>Lead Developer</p>
            <p>Nomfundo is the mastermind behind the development of this project. With a background in software engineering, she ensures that everything runs smoothly.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Team Member 2
    st.markdown(
        """
        <div class="team-member">
            <h3>John Smith</h3>
            <p>Data Scientist</p>
            <p>John analyzes the data to provide insights that drive the project forward. His expertise in data science helps us make data-driven decisions.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
