"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """## Languages
- R
- Python
- SQL 
- VBA

## Platforms and Libraries
- **SAS** - JMP, Enterprise Miner and Enterprise Guide
- **MS Office** - Excel, Powerpoint, Project, Word
- **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Tensorflow, Keras, Streamlit, Dash, Plotly, Matplotlib, Seaborn, etc.
- **R** - Shiny, Dplyr
- **SQL** - MS SQL, PostgreSQL,HIVE, HANA, Teradata 
- Tableau
- PowerBI
- Qlik View
- JIRA, Confluence

## Analytical Skills
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Web Scraping

## AWS Stack
- EC2
- Lambda
- S3
- RDS - Redshift, Aurora, MS SQL
- Dynamo DB
- Sagemaker
- Lex, Polly
- Cloudfront
- IAM
            

_I am a Random Forest in the World of Overfitting_



""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
