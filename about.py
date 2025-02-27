import streamlit as st

def about():
    st.markdown(
    """  
    <div class="content-container2">
        <h1 class="aiml-heading"> &nbsp; About Me</h1>
    </div>
    <br>
    <h3 class="custom-lines2">Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
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
        <br>
        <div class="content-container">
            <h1 class="custom-heading3">TECHNICAL SKILLS</h1>
            <h3 class="custom-details"><u>Programming Languages</u>:</h3>
            <h5 class="custom-details">Python | SQL</h5>
            <h3 class="custom-details"><u>Techniques</u>:</h3>
            <h5 class="custom-details">Data Preprocessing | Data Augmentation | Model Development | Testing | Analysis | Optimization | UI Development | Image Processing | Pattern Recognition</h5>
            <h3 class="custom-details"><u>Machine Learning and Deep Learning Libraries and Frameworks</u>:</h3>
            <h5 class="custom-details">NumPy | Pandas | Scikit-learn (sklearn) | Matplotlib | Seaborn | Plotly | OpenCV | TensorFlow | Keras | PyTorch</h5>
            <h3 class="custom-details"><u>Development and Deployment Tools</u>:</h3>
            <h5 class="custom-details">Docker | Git | GitHub | VS Code | Streamlit | GCP | AWS | CI/CD | Tableau</h5>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
    """
    <div class="content-container">
        <h1 class="custom-heading3">EDUCATION</h1>
        <h4 class="custom-details"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering<br> &nbsp; ● 12th - HSE <br> &nbsp; ● 10th - CBSE</h4>
        <h1 class="custom-heading3">NON-TECHNICAL SKILLS</h1>
        <h5 class="custom-details">Problem-Solving | Critical Thinking | Attention to Detail | Communication | Collaboration | Time Management</h5>
        <h1 class="custom-heading3">LANGUAGES</h1>
        <h5 class="custom-details">English | Malayalam | Hindi | Tamil</h5>
    </div>

    """,
    unsafe_allow_html=True,
)

    

    
    