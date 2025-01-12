import streamlit as st

def about():
    st.markdown(
    """  
    <h1 class="custom-heading">About Me</h1>
    <h3 class="custom-lines2"><br>Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
    """,
    unsafe_allow_html=True,
)   
    st.divider()
    cv_file_path = "ANANDAPADMANABHAN_CV.pdf"
    # Read the resume file
    with open(cv_file_path, "rb") as file:
        cv_data = file.read()
    # Download Button
    st.download_button(
        label="Download CV",
        data=cv_data,
        file_name="ANANDAPADMANABHAN_CV.pdf",
        mime="application/pdf",
    )
    
    st.markdown(
        """
        <h1 class="custom-heading2">TECHNICAL SKILLS</h1>
        <h3 class="custom-details"><u>Programming Languages:</u></h3>
        <h3 class="custom-details">Python | SQL</h3>
        <h3 class="custom-details"><u>Techniques:</u></h3>
        <h3 class="custom-details">Data Preprocessing | Data Augmentation | Model Development | Testing | Analysis | Optimization | UI Development | Image Processing | Pattern Recognition</h3>
        <h3 class="custom-details"><u>Machine Learning and Deep Learning Libraries and Frameworks:</u></h3>
        <h3 class="custom-details">NumPy | Pandas | Scikit-learn (sklearn) | Matplotlib | Seaborn | Plotly | OpenCV | TensorFlow | Keras | PyTorch</h3>
        <h3 class="custom-details"><u>Development and Deployment Tools:</u></h3>
        <h3 class="custom-details">Docker | Git | GitHub | VS Code | Streamlit | GCP | AWS | CI/CD | Tableau</h3>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
    """
    <div class="content-container">
        <h1 class="custom-heading2">EDUCATION</h1>
        <h3 class="custom-lines3"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

    

    
    