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
    # Section: Resume / CV
    st.header("CV")
    resume_file_path = "anandapadmanabhan_cv.pdf"
    # Embed PDF Viewer
    st.markdown(
        f"""
        <iframe src="{resume_file_path}" width="700" height="500" style="border: none;"></iframe>
        """,
        unsafe_allow_html=True,
    )

    # Read the resume file
    with open(resume_file_path, "rb") as file:
        resume_data = file.read()

    # Download Button
    st.download_button(
        label="Download Resume",
        data=resume_data,
        file_name="Resume.pdf",
        mime="application/pdf",
    )