# import streamlit as st

# def about():
#     st.markdown(
#     """  
#     <h1 class="custom-heading">About Me</h1>
#     <div>
#         <h3 class="custom-lines2"><br>Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
#         <br>
#         <h1 class="custom-heading2">EDUCATION</h1>
#         <h3 class="custom-lines3"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#     # Section: Resume / CV
#     st.header("CV")
#     resume_file_path = "ANANDAPADMANABHAN_CV.pdf"
#     # Embed PDF Viewer
#     st.markdown(
#         f"""
#         <iframe src="{resume_file_path}" width="700" height="500" style="border: none;"></iframe>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Read the resume file
#     with open(resume_file_path, "rb") as file:
#         resume_data = file.read()

#     # Download Button
#     st.download_button(
#         label="Download Resume",
#         data=resume_data,
#         file_name="Resume.pdf",
#         mime="application/pdf",
#     )

# # Add custom styling
# st.markdown(
#     """
#     <style>
#     iframe {
#         border-radius: 10px;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


import streamlit as st

def about():
    st.markdown(
        """  
        <h1 class="custom-heading">About Me</h1>
        <div>
            <h3 class="custom-lines2"><br>Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
            <br>
            <h1 class="custom-heading2">EDUCATION</h1>
            <h3 class="custom-lines3"> &nbsp; ● BTech in Information Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section: Resume / CV
    st.header("CV")

    # Path to resume file
    resume_file_path = "ANANDAPADMANABHAN_CV.pdf"

    # Embed PDF Viewer (using st.components.v1.html for better iframe handling)
    st.components.v1.html(
        f"""
        <iframe src="{resume_file_path}" width="700" height="500" style="border: none;"></iframe>
        """,
        height=520,
    )

    # Read the resume file
    try:
        with open(resume_file_path, "rb") as file:
            resume_data = file.read()

        # Add Download Button
        st.download_button(
            label="Download Resume",
            data=resume_data,
            file_name="ANANDAPADMANABHAN_CV.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.error("Resume file not found. Please ensure the file is in the correct location.")