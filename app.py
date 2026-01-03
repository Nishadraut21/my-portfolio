import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Nishad Raut | Portfolio",
    page_icon="💻",
    layout="wide",
)

# --- CSS STYLING ---
st.markdown("""
<style>
    /* Clean up the default Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Nishad Atul Raut")
    st.write("📍 Kalyan, India")
    
    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Projects", "Skills", "Contact"],
        icons=["house", "briefcase", "code-slash", "cpu", "envelope"],
        default_index=0,
    )
    
    st.write("---")
    
    # Resume Download Button Logic
    # We use a try-except block so the app doesn't crash if the file is missing
    try:
        with open("assets/resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Nishad_Raut_Resume.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found in 'assets' folder.")

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Hello, I'm Nishad! 👋")
        st.subheader("Python Developer & Gen AI Enthusiast")
        st.write(
            """
            I am a B.Tech Graduate (Computer Technology) passionate about building scalable solutions 
            using **Python, Django, and SQL**. My focus is on mastering Object-Oriented Programming (OOP) 
            and Generative AI technologies to drive innovation.
            """
        )
        st.write("### 🚀 Objective")
        st.info(
            "To work in a professional environment where I can utilize my skills in Python "
            "and AI to fulfill organizational goals while continuously learning."
        )
    with col2:
        # Fun interactive metric
        st.metric(label="Degree Aggregate", value="6.2 CGPA", delta="RTMNU Nagpur University")
        st.metric(label="Coding Focus", value="Python & Gen AI")

# --- EXPERIENCE SECTION (Interactive Timeline) ---
if selected == "Experience":
    st.header("⏳ Professional Journey")
    
    # Data from your resume
    data = [
        dict(
            Role="Web Developer Intern", 
            Company="Webocta Tech Pvt. Ltd", 
            Start="2025-03-01", 
            End="2025-06-30",
            Description="WordPress customization, Elementor, designing and developing web pages."
        ),
        dict(
            Role="Salesforce Intern", 
            Company="Networkz Infosystem Pvt. Ltd", 
            Start="2023-03-01", 
            End="2023-05-31",
            Description="Salesforce CRM prerequisites, Apex programming language basics."
        )
    ]
    
    df = pd.DataFrame(data)
    
    # Create Interactive Gantt Chart using Plotly
    fig = px.timeline(
        df, 
        x_start="Start", 
        x_end="End", 
        y="Company", 
        color="Role",
        hover_data=["Description"],
        title="Internship Timeline"
    )
    fig.update_yaxes(autorange="reversed") # Put recent on top
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("---")
    
    # Detailed View
    st.subheader("Detailed Experience")
    for index, row in df.iterrows():
        with st.expander(f"{row['Role']} @ {row['Company']}"):
            st.write(f"📅 **Duration:** {row['Start']} to {row['End']}")
            st.write(f"💡 **Key Work:** {row['Description']}")

# --- PROJECTS SECTION ---
if selected == "Projects":
    st.header("💻 Featured Projects")
    
    st.subheader("Automatic Question Paper Generator System")
    st.caption("Tech Stack: Spring Boot, Java, MySQL, JavaScript")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write(
            """
            Developed an application to automatically generate question papers based on user-defined 
            requirements and constraints. 
            
            **Key Features:**
            * Used **Ant Colony Optimization (ACO)** for optimal question selection.
            * Designed a user-friendly interface for constraint input.
            * Handled full database schema design and backend integration.
            """
        )
    with col2:
        st.write("#### Algorithm Used")
        # Using LaTeX for the math concept you mentioned
        st.latex(r'''
        P_{ij}(t) = \frac{[\tau_{ij}(t)]^\alpha \cdot [\eta_{ij}]^\beta}{\sum_{k \in \text{allowed}} [\tau_{ik}(t)]^\alpha \cdot [\eta_{ik}]^\beta}
        ''')
        st.caption("Optimization Logic (Conceptual Representation)")

# --- SKILLS SECTION ---
if selected == "Skills":
    st.header("🛠 Technical Proficiency")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Programming & Database")
        st.write("""
        - **Languages:** Python, C#, SQL
        - **Databases:** MySQL, PostgreSQL
        - **Frameworks:** Django
        """)
        
    with col2:
        st.subheader("Web & AI Tools")
        st.write("""
        - **Web:** HTML, CSS, JavaScript, WordPress
        - **AI Tools:** GitHub Copilot, Gemini Pro, GPT, Cursor
        - **Version Control:** Git, GitHub
        """)
        
    st.subheader("Soft Skills")
    st.success("Adaptability | Rapid Skill Acquisition | Strategic Problem Solving | Time Management")

# --- CONTACT SECTION ---
# --- CONTACT SECTION ---
if selected == "Contact":
    st.header("📬 Get In Touch")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Feel free to reach out for collaborations or job opportunities.")
        st.write("📧 **Email:** rautnishad2@gmail.com")
        st.write("📱 **Mobile:** +91 7499698921")
        st.write("🏠 **Address:** Flat No. 1201, Viento C, Khoni Palava, Kalyan")
        
    with col2:
        # Functional Contact Form
        contact_form = """
        <form action="https://formsubmit.co/rautnishad2@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
             <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
             <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
             <button type="submit" style="background-color: #FF4B4B; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)