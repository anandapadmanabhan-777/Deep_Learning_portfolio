import streamlit as st

def about():
    st.markdown(
    """  
    <h1 class="custom-heading">About Me</h1>
    <div>
        <h3 class="custom-lines2"><br>Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
        <br>
        <h1 class="custom-heading2">EDUCATION</h1>
        <h3 class="custom-lines3"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
    </div>
    """,
    unsafe_allow_html=True,
)
    cv_file_path = "ANANDAPADMANABHAN_CV.pdf"
    # Read the resume file
    with open(cv_file_path, "rb") as file:
        cv_data = file.read()

    # # Inject CSS for global styling
    # st.markdown(
    #     """
    #     <style>
    #     /* Style for all download buttons */
        
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # Download Button
    st.download_button(
        label="Download CV",
        data=cv_data,
        file_name="ANANDAPADMANABHAN_CV.pdf",
        mime="application/pdf",
    )
    