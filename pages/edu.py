"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### University of Connecticut School of Business
**Master of Science in Business Analytics and Project Management | May 2020** | [**UConn**](https://www.business.uconn.edu/)\n
GPA 4.00/4.00 | Beta Gamma Sigma Honoree 

**Courses ** \n
- Statistics in Business Analytics \n
- Big Data Analytics with Hadoop \n
- Business Decision Modelling \n
- Predictive Analytics \n
- Data Mining and Business Analytics \n
- Introduction to Project Management \n
- Advanced Business Analytics and Project Management \n
- Adaptive Business Intelligence \n
- Project Risk and Cost Management \n
- Project Leadership and Communication \n


### Distance Learning

**University of Michigan | June 2020** | [Credential](https://coursera.org/share/eb4b7f377b485efe57dafbf0ef9e9178)\n
- Applied Text Mining

**Deeplearning.ai | April 2020** | [Credential](https://coursera.org/share/a07ae8b31a11a44f30fe4f77d6d6c0cc)\n
- Structuring Machine Learning Projects

**A Cloud Guru| February 2020** | [Credential](https://verify.acloud.guru/5F4E6B310B93)\n
- AWS certified cloud practitioner 2020

### Manipal Institute of Technology
**Bachelors of Technology in Mechanical Engineering | May 2015** | [**MIT**](https://manipal.edu/mit.html)\n
GPA 8.54/10.00 

**Courses **\n
- Essentials of management\n
- Engineering Economics and Management \n
- Object Oriented Programming \n
- Business Communications \n
- Operational Research

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
