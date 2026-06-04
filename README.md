cat > README.md << 'EOF'
# OpportunityOS

OpportunityOS is an AI Chief of Staff for senior Product Manager job search execution.

It helps a PM evaluate AI product roles by analyzing job descriptions, scoring role fit, recommending the strongest product story to lead with, drafting hiring manager outreach, and creating an interview prep plan.

## Problem

Senior PM job searches are high-context and fragmented. A single candidate may be targeting internal AI roles, AI platform roles, AI agent roles, and core product AI roles — each requiring different positioning, stories, and preparation.

Most job trackers store information, but they do not help candidates make decisions.

## Solution

OpportunityOS turns a job description into an AI-powered role strategy.

The app helps answer:

- Is this role worth prioritizing?
- Which product story should I lead with?
- What risks should I preempt?
- What should I say to the hiring manager?
- What should I prepare for the interview?
- What is the next best action?

## Key Features

- Job description analysis
- Role fit scoring
- AI role categorization
- Product story matching
- Hiring manager outreach generation
- Interview prep planning
- Next-best-action recommendation
- Personalized candidate story library

## AI Product Principles

OpportunityOS is designed around enterprise AI product principles:

- Human-in-the-loop decision support
- Explainable recommendations
- Workflow-first design
- Personalized context
- Structured decision-making
- Workflow-first AI UX

## Tech Stack

- Python
- Streamlit
- OpenAI API
- dotenv

## Demo Flow

1. Enter company name
2. Enter role title
3. Paste job description
4. Click Analyze Role
5. Review fit score, recommended story, outreach, interview prep, and next best action

## Why I Built This

I built OpportunityOS to explore how AI agents can support complex professional workflows. The goal was not to build a generic chatbot, but to design a workflow-oriented AI product that helps with prioritization, positioning, and decision support.

This mirrors how I think enterprise AI products should work: AI should be embedded into real workflows, provide clear reasoning, preserve user control, and improve outcomes over time.
EOF
