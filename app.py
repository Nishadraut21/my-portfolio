import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Nishad Raut | Portfolio",
    page_icon="💻",
    layout="wide",
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/5a919e31-5026-47b2-8419-756180352b27/6L8B3hBwR1.json") # Coding animation
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json") # Contact animation
lottie_ai = load_lottieurl("https://lottie.host/955e81b6-7649-43c9-9403-120005d5193d/L0L8Z3xXy8.json") # AI Brain


st.markdown("""
<style>
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Styling the sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6; 
    }
    
    /* Custom Card Style for Experience */
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Hover effect for buttons */
    div.stButton > button:hover {
        background-color: #ff4b4b;
        color: white;
        border-color: #ff4b4b;
        transform: scale(1.02);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
 
    try:
        img = Image.open("assets/profile-pic.png")
        st.image(img, width=150)
    except:
        st.write("📷") 

    st.title("Nishad Atul Raut")
    st.write("📍 Kalyan, India")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Projects", "Skills", "Contact"],
        icons=["house", "briefcase", "code-slash", "cpu", "envelope"],
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )
    
    st.write("---")
    
    try:
        with open("assets/resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Nishad_Raut_Resume.pdf",
            mime="application/pdf",
        )
    except:
        st.warning("⚠️ Resume file missing")


if selected == "Home":
    col1, col2 = st.columns([1.5, 1]) 
    
    with col1:
        st.title("Hello, I'm Nishad! 👋")
        st.markdown("<h3 style='color: #ff4b4b;'>Python Developer & Gen AI Enthusiast</h3>", unsafe_allow_html=True)
        st.write(
            """
            I am a B.Tech Graduate (Computer Technology) passionate about building scalable solutions 
            using **Python, Django, and SQL**. My focus is on mastering Object-Oriented Programming (OOP) 
            and **Generative AI** technologies to drive innovation.
            """
        )
        st.info("🚀 **Objective:** To leverage AI & Python to solve real-world problems.")
        
       
        st.markdown("""
        <a href="https://linkedin.com" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/Nishadraut21" target="_blank">GitHub</a> | 
        <a href="mailto:rautnishad2@gmail.com">Email</a>
        """, unsafe_allow_html=True)

    with col2:
        st_lottie(lottie_coding, height=300, key="coding")


if selected == "Experience":
    st.header("⏳ Professional Journey")
    
    data = [
        dict(Role="Web Developer Intern", Company="Webocta Tech Pvt. Ltd", Start="2025-03-01", End="2025-06-30", Description="WordPress customization, Elementor, designing and developing web pages."),
        dict(Role="Salesforce Intern", Company="Networkz Infosystem Pvt. Ltd", Start="2023-03-01", End="2023-05-31", Description="Salesforce CRM prerequisites, Apex programming language basics.")
    ]
    df = pd.DataFrame(data)
    
   
    fig = px.timeline(df, x_start="Start", x_end="End", y="Company", color="Role", hover_data=["Description"], title="Internship Timeline")
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(xaxis_title="Date", height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("### 📌 Detailed Roles")
    for index, row in df.iterrows():
        with st.expander(f"{row['Role']} @ {row['Company']}", expanded=True):
            st.write(f"📅 **{row['Start']} - {row['End']}**")
            st.write(f"💡 {row['Description']}")


if selected == "Projects":
    st.header("💻 Featured Projects")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Automatic Question Paper Generator")
        st.caption("Tech: Spring Boot, Java, MySQL")
        st.write("Developed an intelligent system to generate exam papers using **Ant Colony Optimization (ACO)**.")
        st.markdown("**Key Features:**")
        st.markdown("- 🧠 **Smart Selection:** Uses ACO to select unique questions.")
        st.markdown("- ⚡ **Automation:** Reduces manual effort by 90%.")
        st.markdown("- 🗄️ **Database:** Optimized MySQL schema.")
    
    with col2:
        # Math concept visualization
        st.markdown("#### The Algo Logic (ACO)")
        st.latex(r'''P_{ij}(t) = \frac{[\tau_{ij}(t)]^\alpha \cdot [\eta_{ij}]^\beta}{\sum [\tau_{ik}(t)]^\alpha \cdot [\eta_{ik}]^\beta}''')
        st_lottie(lottie_ai, height=200, key="ai")


if selected == "Skills":
    st.header("🛠 Technical Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🐍 Python Core")
        st.progress(90)
        st.write("Django, Pandas, Scripting")
        
    with col2:
        st.markdown("### 🤖 Gen AI")
        st.progress(75)
        st.write("Gemini Pro, GPT, Cursor")
        
    with col3:
        st.markdown("### 🗄️ Data")
        st.progress(85)
        st.write("SQL, MySQL, PostgreSQL")
        
    st.write("---")
    st.write("Also proficient in: **Git, HTML/CSS, WordPress, C#**")


if selected == "Contact":
    st.header("📬 Get In Touch")
    
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.write("### Let's Connect!")
        st.write("I am currently looking for opportunities in **Python Development** and **AI**.")
        st.write("📧 rautnishad2@gmail.com")
        st.write("📱 +91 7499698921")
        st_lottie(lottie_contact, height=200)

    with right_col:
        contact_form = """
        <form action="https://formsubmit.co/rautnishad2@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
             <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
             <textarea name="message" placeholder="Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; height: 150px;"></textarea>
             <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
