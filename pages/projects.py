"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects - :male-construction-worker: ")
    st.markdown(
            """### Graduate Consultant, LIMRA | Aug 2019 – Dec 2019
            
**Life insurance Policy Lapse Study [AWS Sagemaker, S3, Python, MS Project]**
- Performed exploratory data analysis on 9.6 million records of aggregated data about “premium persistency” and analyzed the frequency and causes of lapses using Tableau
- Built XGBoost classification model with 83% precision, 76% recall using AWS Sagemaker to predict customer churn 

            
### Decision Scientist, Mu Sigma Inc.| July 2015 - Dec 2020
**Web Application for a Major US Retailer [SQL- Teradata, HANA, HIVE, Agile-JIRA]**
- Managed agile teams working on development of a web-based Business Intelligence dashboard to rate ~51k vendors based on key performance indicators like OTIF and In-stock Metrics
- Led a team of five analysts to develop SQL queries, calculation views and stored procedures to extract data for front-end visualizations

**Sales and revenue reporting for a US Technology giant [Excel, VBA, SSIS-ETL]**
- Developed multiple Power BI and Excel dashboards explaining sales and revenues across different business units.
- Performed Extract Transform Load of data files from several Data Sources to feed the DataCube backend for the reports
- Created data quality dashboard using VBA and excel to accurately identify data discrepancy issues between reports reducing the time for manual verification by 90%

**Predicting potential product complaints [Regex, NLP, Random Forest]**
- Processed customer complaints data using regex and NLP to identify common topics and establish a cause effect relationship with quality control tests’ data from a refrigerator assembly line
- Created a scalable tool on SAS Visual Analytics to speed up identifying issues during production, leading to 25% improvement in parts availability during assembly


### Academic Projects [(GitHub)](https://github.com/alphadatagamma)

**The Cricket Project [BeautifulSoup, Regex, AWS Sagemaker, S3, Redshift, Tableau]**
- Used BeautifulSoup and Regex to scrape cricket data for 10 countries and ~6000 players using AWS Sagemaker and EC2 
- Created a data warehouse in AWS Redshift, and a tableau dashboard to visualize key trends

**Advance House Price Prediction in Python [Kaggle Top 2%, Stacked Regression]**
- Created a custom stacked regression model to predict sale price for 1500 houses and achieved a low RMSE of 0.11 for the final model and a top 2% rank on the leaderboard

**IBM Attrition Analysis and Prediction [Python, Tableau, Decision Trees]**
- Performed exploratory data analysis and external research to identify the mix of drivers affecting employee attrition rates  
- Created a classification model using Decision trees and Gradient Boosting to identify employees that are likely to leave, so that the company can have a strategy for employee engagement

            

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
