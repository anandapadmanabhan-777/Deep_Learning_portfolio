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
    <style>
        /* Custom styles for the ordered list and list items */
        ol.custom-details {
            padding-left: 20px; /* Add some padding to the left */
        }
        
        ol.custom-details li {
            font-family: 'Atma', cursive !important;
            font-size: 18px !important;
            color: #000;
            margin-bottom: 5px;
        }
    </style>
    
    <h1 class="custom-heading2">TECHNICAL SKILLS</h1>
    
    <h3 class="custom-details">● Programming Languages:</h3>
    <ol class="custom-details">
        <li>Python</li>
        <li>SQL</li>
    </ol>
    
    <h3 class="custom-details">● Techniques:</h3>
    <ol class="custom-details">
        <li>Data Preprocessing</li>
        <li>Data Augmentation</li>
        <li>Model Development</li>
        <li>Testing</li>
        <li>Analysis</li>
        <li>Optimization</li>
        <li>UI Development</li>
        <li>Image Processing</li>
        <li>Pattern Recognition</li>
    </ol>
    
    <h3 class="custom-details">● Machine Learning and Deep Learning Libraries and Frameworks:</h3>
    <ol class="custom-details">
        <li>NumPy</li>
        <li>Pandas</li>
        <li>Scikit-learn (sklearn)</li>
        <li>Matplotlib</li>
        <li>Seaborn</li>
        <li>Plotly</li>
        <li>OpenCV</li>
        <li>TensorFlow</li>
        <li>Keras</li>
        <li>PyTorch</li>
    </ol>
    
    <h3 class="custom-details">● Development and Deployment Tools:</h3>
    <ol class="custom-details">
        <li>Docker</li>
        <li>Git</li>
        <li>GitHub</li>
        <li>VS Code</li>
        <li>Streamlit</li>
        <li>GCP</li>
        <li>AWS</li>
        <li>CI/CD</li>
        <li>Tableau</li>
    </ol>
    """,
    unsafe_allow_html=True,
)


    # st.markdown(
    #     """
    #     <h1 class="custom-heading2">TECHNICAL SKILLS</h1>
    #     <h3 class="custom-details">● Programming Languages: <br> &nbsp; &nbsp; Python | SQL</h3>
    #     <h3 class="custom-details">● Techniques: <br> &nbsp; &nbsp; Data Preprocessing | Data Augmentation | Model Development | Testing | Analysis | Optimization | UI Development | Image Processing | Pattern Recognition</h3>
    #     <h3 class="custom-details">● Machine Learning and Deep Learning Libraries and Frameworks: <br> &nbsp; &nbsp; NumPy | Pandas | Scikit-learn (sklearn) | Matplotlib | Seaborn | Plotly | OpenCV | TensorFlow | Keras | PyTorch</h3>
    #     <h3 class="custom-details">● Development and Deployment Tools: <br> &nbsp; &nbsp; Docker | Git | GitHub | VS Code | Streamlit | GCP | AWS | CI/CD | Tableau</h3>
    #     <ol class="custom-details">
    #     <li class="custom-details">Python</li>
    #     <li>SQL</li>
    # </ol>
    #     """,
    #     unsafe_allow_html=True,
    # )

    st.markdown(
    """
    <h1 class="custom-heading2">EDUCATION</h1>
    <h3 class="custom-lines3"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
    
    """,
    unsafe_allow_html=True,
)

    

    
    