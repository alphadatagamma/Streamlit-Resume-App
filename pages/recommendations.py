"""Recommendations page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Recommendations :memo:")
    st.markdown(
            """### Anantha Krishna Rajpurohit
**Senior Analyst | Boston Consulting Group(BCG) | April 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/anantha-krishna-rajpurohit/)\n
Abhishek joined as a fresher into the team. He brings in a lot of energy into the team and gives his 
100%. He was reliable to finish the job at hand and actively reach out for help from peers and managers. 
Always looked to up-skill on a regular basis and actively looked for new skills in the analytics space. 
Since then he grew over three years at Mu Sigma to be able to move on the bigger responsibilities, 
mentoring juniors, managing modules and delivering high quality results. With his recent addition of MS 
in business analytics, I recommend him for any position that require depth in analytics, 
reliability and project management skills
 

### Abhinav Dasgupta
**Deputy Director | Myntra Jabong | April 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/abhinav-dasgupta-a0670422/)  \n
Abhishek was part of the team working with a leading manufacturing giant which I was leading. 
Abhishek brought a great sense of maturity and work ethic coupled with excellent analytical skills 
to the team and ensured we constantly created a good experience for the client stakeholders. 
We solved some of the most complex problems for the business and he was pivotal in making it happen. 
In addition, he has a continuous zeal to learn and improve himself, which was also reflected in his 
decision to pursue masters in the area of analytics. I really enjoyed working with Abhishek 
during his time at Mu Sigma and think he will be a top asset to any team that he will be part of.

### Tara Chamberlain
**Senior Operations Manager| AT&T | February 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/tara-chamberlain-832b991a/)  \n
Abhishek was a member of my Capstone team at UCONN and proved to be an invaluable asset. He was not 
only adept at all data cleaning, modeling, and visualization methods that our team utilized, but
 also took the lead in our research. He ended up uncovering key information that no one, not even our 
 professor or sponsors, was aware of. The team that I run at my current company doesn't 
     have any openings, but it we did, I would be happy to have him join our organization.




""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()

