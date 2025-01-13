import streamlit as st

def home():
    st.markdown(
    """
    <div class="content-container2">
        <h1 class="custom-heading"> &nbsp; Welcome to My AI & ML Project Portfolio..!!</h1>
    </div>
    <br>
    <h1 class= "name-heading">Hello, I'm<br> Anandapadmanabhan..!!</h1>
    <br>
    <br>
    <h3 class="custom-lines">Python Developer | Aspiring AI/ML Engineer | Full Stack Python Developer &nbsp; 💻🧠
    """,
    unsafe_allow_html=True,    
)
    st.divider()
    st.markdown(
    """
    
    <div class="social-icons" style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
        <div>
            <a href="https://www.linkedin.com/in/anandapadmanabhan-s-43959522a/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" alt="LinkedIn Profile" width="50">
            </a>
            <p>LinkedIn</p>
        </div>
        <div>
            <a href="mailto:anandapadmanabhan777@gmail.com">
                <img src="https://cdn-icons-png.flaticon.com/512/552/552486.png" alt="Email Me" width="50">
            </a>
            <p>Email</p>
        </div>
        <div>
            <a href="https://github.com/anandapadmanabhan-777" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub Profile" width="50">
            </a>
            <p>GitHub</p>
        </div>
    </div>
    <br>
    
    """,
    unsafe_allow_html=True,    
)
    # Navigation button
    if st.button("Explore AI/ML Projects"):
        st.session_state.menu_selection = "AI/ML Projects"
        st.rerun()