import streamlit as st
from stories import STORIES
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="OpportunityOS",
    page_icon="💼",
    layout="wide"
)

st.title("OpportunityOS")
st.subheader("AI Chief of Staff for Senior PM Job Search")

st.sidebar.title("OpportunityOS")
st.sidebar.write("AI agent for senior PM job search execution.")

st.sidebar.markdown("### Best for")
st.sidebar.write("- Internal AI roles")
st.sidebar.write("- Enterprise AI PM roles")
st.sidebar.write("- AI Agents roles")
st.sidebar.write("- AI Platform roles")
st.sidebar.write("- AI Quality / Evals roles")

st.sidebar.markdown("### Candidate stories")
for story in STORIES.keys():
    st.sidebar.write(f"- {story}")

tab1, tab2, tab3 = st.tabs([
    "Analyze Role",
    "My Stories",
    "How to Use"
])

with tab1:
    company_name = st.text_input(
        "Company name",
        placeholder="Example: MongoDB, Glean, ServiceNow, Anthropic"
    )

    role_title = st.text_input(
        "Role title",
        placeholder="Example: Staff Product Manager, Internal AI"
    )

    job_description = st.text_area(
        "Paste job description here",
        height=300,
        placeholder="Paste the full job description..."
    )

    if st.button("Analyze Role"):
        if not job_description.strip():
            st.warning("Please paste a job description first.")
        else:
            with st.spinner("Analyzing role fit..."):
                story_library = "\n\n".join(
                    [f"{name}: {details}" for name, details in STORIES.items()]
                )

                prompt = f"""
You are OpportunityOS, an AI Chief of Staff for a senior Product Manager running a Silicon Valley AI PM job search.

Candidate profile:
- Senior Product Manager with enterprise AI, cybersecurity, and workflow automation experience
- Built AI-driven TRR automation for technical resource routing
- Used Vertex AI for AI-assisted recommendation workflows
- Improved recommendation acceptance from 28% to 65%
- Achieved around 95% recommendation coverage
- Built human-in-the-loop systems for high-stakes decision-making
- Worked on AI-powered DOR workflows in Salesforce
- Built AI evaluation loops, adoption metrics, and governance-aware product workflows
- Has experience with internal enterprise users and some external/customer-facing AI through AI Policy Optimizer

Candidate story library:
{story_library}

Scoring rubric:
- 90-100: Excellent fit. Strongly apply and seek referral.
- 80-89: Strong fit. Apply with tailored positioning.
- 70-79: Good fit. Apply if company is high priority.
- 60-69: Possible fit but needs heavy repositioning.
- Below 60: Low priority.

Score the job based on:
1. AI product relevance
2. Enterprise/internal workflow relevance
3. Core product relevance
4. Match to candidate's strongest stories
5. Seniority fit
6. Hiring manager believability
7. Risk that the role sees candidate as too internal/GTM-focused

Company:
{company_name}

Role title:
{role_title}

Job description:
{job_description}

Return in this format:

# Fit Score
Give score and short explanation.

# Role Category
Choose one:
- Internal AI
- Enterprise AI Platform
- Core AI Product
- AI Agents
- AI Quality/Evals
- AI Safety
- Weak Fit

# Why This Role Fits
Use bullets.

# Risks / Gaps
Be honest.

# Best Story To Lead With
Choose the best story from the candidate story library and explain why.

# 60-Second Pitch
Write a polished but conversational pitch.

# Hiring Manager Outreach
Write a concise LinkedIn message.

# Interview Prep Plan
List the top 5 areas to prepare.

# Next Best Action
Give one concrete action to take today.
"""

                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert AI product career advisor."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.4
                )

                result = response.choices[0].message.content

                st.markdown("## Role Analysis")
                st.markdown(result)

with tab2:
    st.markdown("## My Product Stories")

    for name, details in STORIES.items():
        st.markdown(f"### {name}")
        st.write(details)

with tab3:
    st.markdown("## How to Use OpportunityOS")
    st.write("1. Paste a job description.")
    st.write("2. Add the company and role title.")
    st.write("3. Click Analyze Role.")
    st.write("4. Review fit score, story match, outreach, and prep plan.")
    st.write("5. Use the output to prioritize your job search.")