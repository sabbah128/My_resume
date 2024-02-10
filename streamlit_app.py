import streamlit as st
from PIL import Image


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.write('# **Hossein KianAra, M.Sc.**')
st.write('#### ***Data Scientis*** ')

image = Image.open('Myprofile.jpg')
st.image(image, width=150)



st.markdown('### :blue[*SUMMARY*]', unsafe_allow_html=True)
st.info('''
- Data scientist with expertise in machine learning and deep learning.
- Possessing a master's degree in computer science and a bachelor's degree in statistics.
- Experience in data analysis and visualization with Power BI and Python.
- More than 12 years of experience in the banking industry. 
- Excellent grade in organizational assessment for 4 years. 
- Eager and motivated about leveraging data to make informed business decisions.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3c6e6e;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/hossein-kian-ara/" target="_blank">Hossein KianAra</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work experience</a>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


st.markdown(''' ### :blue[*EDUCATION*]''')
txt('**Master of degree in Computer Science.**, *Shahed, Tehran University*, IRAN', '2021-2023')
st.markdown('''
- GPA: `3.63`
- Research thesis entitled `Machine learning diagnosis of active juvenile idiopathic arthritis on blood pool [99MTc] Tc-MDP scintigraphy images`.
- Collaborated on the development of two articles with the Children's Nuclear Medicine Development Center at Dr. Gharib Hospital in Tehran.
- Graduated with First Class Honors.
''')
txt('**Bachelors of Science.** (Statistics), *Azad University of Arak*, IRAN','2005-2009')
st.markdown('''
- GPA: `3.1`
- Research thesis entitled `KAPPA coefficient in medical research`.
''')

st.markdown('''### :blue[*WORK EXPERIENCE*]''')
txt('**Banking Digital Transformation** (Part-Time), Tehran, IRAN', 'Feb/2022-current')
st.markdown('''
- Participation in the "Digital Transformation of Maskan Bank" initiative, which aims to incorporate AI and data science to evaluate customers.
            (The project has a statistical population of over 9 million people.)
- Achieved a 15% increase in online transactions and digital banking usage through the implementation of new digital channels and features.
''')
txt('**Customer Credit Analyst** (Full-Time), Arak, IRAN', 'Jan/2017-current')
st.markdown('''
- Reduced risk through analyzing financial data and credit reports for accurate credit assessments.
- Redesigned and implemented a customer validation algorithm, resulting in a twofold increase in validation speed.
- Developed a clustering algorithm in Python to identify influential customers in branch credit using a dataset of over 9,000 data points.
''')
txt('**Senior Banking Affairs Officer** (Full-Time), Arak, IRAN', 'Nov/2013-Jan/2017')
st.markdown('''
- Directed a team of seven individuals to reduce customer claims, resulting in a 30% reduction in loan delinquencies.
- Collaborated with underwriters and loan officers to close 40+ loans per month.
- Trained and mentored 10+ junior colleagues, resulting in improved team performance and productivity.
''')
txt('**Junior Banking Affairs Officer** (Full-Time), Arak, IRAN', 'Oct/2011-Nov/2013')
st.markdown('''
- Planned, executed, and optimized digital marketing campaigns, resulting in a 15% increase in customer engagement with online banking services.
- Implemented customer forecasting models, resulting in a 10% improvement in demand forecast accuracy.
- Oversaw the processing of more than 3,000 transactions on a monthly basis.
''')


st.markdown('''### :blue[*ACHIEVEMENTS*]''')
st.markdown('''
- Ranked first in the master's program at the Faculty of Computer Sciences.
- Secured first place in the youth category programming competition in Markazi province and ranked fourth nationally in Iran.
- Published two publications in partnership with the Dr. Gharib Hospital's Children's Nuclear Medicine Development Centre in Tehran.
''')

st.markdown('''### :blue[*SKILLS*]''')
txt3('Programming', '`Python`')
txt3('Data Preparation/Analysis', '`SQL`, `Excel`, `Pandas`, `Numpy`')
txt3('Data Visualization', '`Power BI`,`Matplotlib`, `Seaborn`, `Bokeh`')
txt3('Sql & noSql db', '`SQL-Server`, `Neo4j`')
txt3('Machine Learning', '`Scikit-learn`, `Pycaret`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`Streamlit`')

st.markdown('''### :blue[*SOCIAL MEDIA*]''')
txt2('Email:', 'sabbah128@gmail.com')
txt2('LinkedIn:', 'https://www.linkedin.com/in/hossein-kian-ara/')
txt2('GitHub:', 'https://github.com/sabbah128/')
txt2('Telegram:', '@sabbah128')


st.markdown(''' **RELEVANT COURSES** ''')
st.markdown('''
- Advance Algorithms,
- Advance AI,
- Data Mining (concept and techniques),
- Introduction to Machine Learning,
- Computing Data Mining,
- Data Visualization,
- Big Data.
''')




