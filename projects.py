
import streamlit as st
import fashion_page as fa
import mnist_page as mn
import fraud_detect_page as fr
import churn_page as ch
import temperature_page as te
import cifar_page as ci
import description as dr

def projects():
    # Initialize session state for navigation
    if "selected_project" not in st.session_state:
        st.session_state.selected_project = "None"
        

    # Main Projects Page
    if st.session_state.selected_project == "None":
        
        st.markdown(
            """
            <div class="content-container2">
                <h1 class="aiml-heading"> &nbsp; AI/ML Projects</h1>
            </div>
            <br>
            """,
            unsafe_allow_html=True,
            )
        
        #st.divider()
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            if st.button("Customer Churn Prediction"):
                st.session_state.selected_project = "Customer Churn"
                st.rerun()
        with col2:
            if st.button("Credit Card Fraud Detection"):
                st.session_state.selected_project = "Credit Card Fraud"
                st.rerun()
        with col3:
            if st.button("MNIST Digit Recognizer"):
                st.session_state.selected_project = "MNIST"
                st.rerun()
        with col4:
            if st.button("Fashion-MNIST"):
                st.session_state.selected_project = "Fashion-MNIST"
                st.rerun()
        with col5:
            if st.button("Temperature Prediction"):
                st.session_state.selected_project = "Temperature"
                st.rerun()
        with col6:
            if st.button("CIFAR-10 Classifier"):
                st.session_state.selected_project = "CIFAR-10"
                st.rerun()
        st.divider()
        dr.description()



    # Render Specific Project Page
    elif st.session_state.selected_project == "Customer Churn":
        ch.churn_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "Credit Card Fraud":
        fr.fraud_detect_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "MNIST":
        mn.mnist_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "Fashion-MNIST":
        fa.fashion_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()
    elif st.session_state.selected_project == "Temperature":
        te.temperature_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "CIFAR-10":
        ci.cifar_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()
            
