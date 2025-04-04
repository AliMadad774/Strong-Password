import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker Ali Madad", page_icon="🔑", layout="Center")
st.markdown("""
            <style>
            .main {text-align: center;}
            .stTextinput {width: 60% !important; margin: auto; }
            .stButton button:hover {width: 50%; background-color #4CAF50; color: white; font-size: 18px; }
            </style>
            """,unsafe_allow_html=True)
st.title("🔑 Password Strenth Generator")
st.write("Enter your password below to check its security level. 🔍")

def check_password_strength(password):
    score = 0
    feedback =[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ password should be **atleast 8 character long**.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ password should include **both uppercase(A-Z) and lowercase**.")

    if re.search(r"\d", password):
        score+= 1
    else:
        feedback.append("❌ password should include ** at least one number (0-9) **,")
    if re.search("r[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special charecter(!@#$%^&*)**.")

    if score == 4:
        st.success("✅ **Strong password** - your password is Secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate password** - consider improving security by adding more feature")
    else:
        st.error("❌ **week password** - follow the suggestion below to strength it. ")
    if feedback:
        with st.expander("🔎**Improve Your Password** ")
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")
    
    if st.button("check strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ please enter a password first!")








