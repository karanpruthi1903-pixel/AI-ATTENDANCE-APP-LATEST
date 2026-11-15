import streamlit as st

def subject_card(subject):
    st.subheader(subject.get("name", "Subject"))

    if "subject_code" in subject:
        st.write(f"Subject Code: {subject['subject_code']}")