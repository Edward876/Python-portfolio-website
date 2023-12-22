from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image
import requests
import os

def ac_lottie(url):
    get = requests.get(url)
    if get.status_code != 200:
        return None
    return get.json()
st.set_page_config(page_title="Supratim Saha", page_icon=Image.open(os.path.abspath("./image/logo4.png")), layout="wide")
anim = ac_lottie("https://lottie.host/497a3d8f-7c78-460e-a18f-5008232c3097/0Lct3QeUvi.json")

############## CSS ##############
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("styles.css")
############## Header ##############

with st.container():
    st.header("Hey! I'm Supratim Saha :wave:")
    st.title("A backend Dev, Student at  Bennett University")
    st.markdown("""I am a student of Bennett University, pursuing my B.Tech in Computer Science and Engineering. 
              I like technology, and trying my best to be a good developer. :computer:""")
    st.write("---")
    
with st.container():
    st.subheader("🤔 Who am I? ")
    right_column, left_column = st.columns(2)
    with right_column:
        st.write("##")
        st.write("""My name is Supratim Saha. I am also known as Shinichi and Shilly Joestar. 
                 I'm a first year student of B.TECH computer science and engineering in Bennett University, situated in Greater Noida, India. 
                 I want to be a back-end developer. I have skills in Javascript (Node.js), Python, C lang.
                 Next I'm thinking to learn java. Thanks for visiting my website.""")
    with left_column:
        st_lottie(anim, height=300, key="animation")
st.write("----")


with st.container():
     st.subheader("🚀 Some of my Projects")
     st.write("##")
     col1, col2 = st.columns(2)
     with col1:
         st.subheader("📝 FreeEduFetch ")
         st.write("""
  - **Purpose** : FreeEduFetch is an API that provides information about free courses from Udemy.
  - **Implementation** : The API is implemented in Python and hosted on Render.
  - **API Endpoints** : It supports multiple data formats and has different endpoints for each format. 
    These include JSON, XML, YAML, TXT, and CSV.
  - **Usage Examples**: The project’s README provides examples of how to fetch data from the API using various programming languages, 
    including Python, Node.js, Java, Go, and TypeScript""")
         st.write("##")
         st.link_button("View in Github", "https://github.com/Edward876/FreeEduFetch")

     with col2:
         st.write("##")
         st.write("##")
         st.image(Image.open(os.path.abspath("./image/p1.jpg")))
         
         st.write("##")           

with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.write("##")
        st.write("##")
        st.image(Image.open(os.path.abspath("./image/p2.jpg")))
        
    with col4:
        st.subheader("🧮 Python Calculator")
        st.write("""
                 A python calculator app with a good user interface.
                 Made it using Tkinter.
                 """)
        st.write("##")
        st.link_button("View in Github", "https://github.com/Edward876/Python-Calculator")
st.write("----")
with st.container():
    st.header("💬 Get in touch")
    st.write("##")
    st.write("- **My social media handels:**")
    a,b = st.columns(2)
    with a:
        c,d = st.columns([0.2,0.4], gap="small")
        with c:
             st_lottie(ac_lottie("https://lottie.host/4efb242c-8957-4b81-9e36-5ea882a675d6/2marCB6EGH.json"), height=30)
            
             st_lottie(ac_lottie("https://lottie.host/863bf059-e741-4072-a9f3-7db260df0939/Sc2h48HkEU.json"), height=30)
            
             st_lottie(ac_lottie("https://lottie.host/093659b0-73cf-45bc-8d55-fec88beb7909/DD1l3HXSML.json"), height=30)
        with d:
            st.markdown("[Kudo._.Shinichi](https://www.instagram.com/_kudo._.shinichi_/)")
           
            st.markdown("[Edward876](https://github.com/Edward876)")
           
            st.markdown("[Supratim Saha](https://www.linkedin.com/in/supratim-saha-548399233/)")
st.write("---")
with st.container():
    contain = """
<form action="https://formsubmit.co/b1a2b3u4a5@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name"  required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form> 

"""
    right,left = st.columns(2)
    with right:

        st.markdown(contain, unsafe_allow_html=True)
    with left:
        st.empty()
    
