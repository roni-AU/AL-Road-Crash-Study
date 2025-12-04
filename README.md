# Alabama Crash Data 2018 – Crash Severity Analysis
*INSY 6500 – Final Project*

## Project Overview
This project analyzes **160,163 crash records** that occurred on **Alabama roads in 2018**, obtained from the CARE crash database. The original dataset includes **235 variables** describing roadway characteristics, environmental conditions, traffic conditions, driver behavior, and various administrative fields.

For this study, we focus on identifying **patterns and contributing factors associated with crash severity**. We examine how roadway, environmental, traffic, distracted-driving, and work-zone conditions relate to the severity of crash outcomes.

## Research Objective
**To investigate the relationship between crash severity and roadway, environmental, and traffic-related factors, and to identify patterns that help explain why some crashes result in more severe outcomes.**

## Dataset Summary
- **Total records:** 160,163 crashes  
- **Year:** 2018  
- **Location:** Alabama public roads  
- **Original variables:** 235  
- **Variables retained for analysis include:**
  - Roadway condition (surface condition, alignment, grade, roadway type)
  - Environmental condition (weather, lighting, atmosphere)
  - Traffic condition (traffic control devices, traffic flow, lane configuration)
  - Distracted driving indicators
  - Crash severity and fatality indicators
- **Variables removed include:**
  - Police response and emergency services fields  
  - Highly detailed location identifiers  
  - Administrative/duplicative fields irrelevant to the analysis  

## Project Workflow
The project is organized into the following notebooks:

1. **Data cleaning**  
   - Load raw CARE crash data  
   - Select relevant columns  
   - Handle missing values and encode variables  
   - Save cleaned dataset as `crash_2018.pkl`

2. **univariate EDA**
   - Summary statistics and distributions  
   - Crash severity frequency analysis  
   - Visual exploration of roadway, environmental, and traffic factors  

3. **Bivariate EDA**
   - Analysis of severity vs other factors 
   - Cross-tabulations and conditional probabilities
   - Visual explorations 

4. **Multivariate Analysis and Transformations**
   - Analysis of correlation matrix 
   - Explore pairwise relationship
  

## Methodology
- Cleaned variables are encoded consistently (categorical normalization, boolean flags where appropriate).
- Intermediate cleaned data is stored with **pickle** to preserve data types and ensure reproducibility.
- Analysis uses descriptive statistics, visualization, and pattern identification methods.
- All code is formatted with **ruff** for styling consistency.
- Notebook outputs are automatically stripped using **nbstripout** to prevent merge conflicts.

## Research Questions
We aim to answer the following questions:
- How does crash severity vary with roadway conditions (surface type, alignment, grade, roadway classification)?
- What environmental conditions (lighting, weather, atmosphere) are associated with higher severity crashes?
- How driver and crash mechanism variables relate to severity?
- Are there meaningful interactions or combinations of factors that consistently correspond to high-severity crashes?

## Collaboration Workflow
This project follows the collaboration workflow recommended in the course:

1. **Always pull before starting work:**
git pull


2. **Before every commit:**
ruff format .
git add .
git commit -m "<message>"
git push


3. **Notebook outputs** are auto-removed via `nbstripout` to avoid merge conflicts.

4. Partners coordinate notebook ownership to avoid simultaneous edits.

## Team Members
- **Partner A:** Data Cleaning & Variable Selection  
- **Partner B:** Exploratory Analysis & Severity Pattern Investigation  
- **Both partners:** Conclusions, interpretation, and documentation  

## Expected Outcomes
- Identification of the most influential roadway, environmental, and traffic conditions associated with severe crashes.  
- Visual and statistical summaries of patterns influencing crash severity.  
- A cleaned, well-documented dataset suitable for further modeling and safety analysis.

