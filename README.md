# Alabama Crash Data 2018 – Crash Severity Analysis
*INSY 6500 – Final Project*

## Authors
- **Partner A:** Md Roknuzzaman, Graduate Research Assistant, Auburn University, Auburn AL-36849. Email: mzr0177@auburn.edu 
- **Partner B:** Kwaku Emmanuel Tufuor, Graduate Research Assistant, Auburn University, Auburn AL-36849. Email: kwt0013@auburn.edu


## Project Overview
This project analyzes **160,163 crash records** that occurred on **Alabama roads in 2018**, obtained from the CARE crash database. The original dataset includes **235 variables** describing roadway characteristics, environmental conditions, traffic conditions, driver behavior, and various administrative fields.

For this study, we focus on identifying **patterns and contributing factors associated with crash severity**. We examine how roadway, environmental, traffic, and distracted driving relate to the severity of crash outcomes.

## Research Objective
**To investigate the relationship between crash severity and roadway, environmental, and traffic-related factors, and to identify patterns that help explain why some crashes result in more severe outcomes.**

## Dataset Summary
- **Total records:** 160,163 crashes  
- **Year:** 2018  
- **Location:** Alabama public roads  
- **Original variables:** 235  
- **Variables retained for analysis include:**
  - 4 Spatial and time factors (Location, Area type, roadway type, Timestamp) 
  - 5 Roadway conditions (AADT, Speed Limit, alignment and grade, lane count, lane separation)
  - 2 Environmental condition (lighting, visibility)
  - 4 Vehicle factors (Number of vehicles, Vehicle type, crash manner, impact speed)
  - 3 Driver demographic information (Gender, License Status, Age)
  - 1 Distracted driving indicator (BAC level)
  - 3 Crash severity and fatality indicators (Number Killed, Number Serious Injuries, Number Non-fatal Injuries)
- **Variables removed include:**
  - Police response and emergency services fields  
  - Highly detailed location and personal information identifiers  
  - Administrative/duplicative fields irrelevant to the analysis  

## Project Workflow
The project is organized into the following notebooks:

**Task - 1: Selection of Relevant Columns** led by Md Roknuzzaman and Kwaku Emmanuel Tufuor  
   - Study existing literature to identify potential factors   
   - Select relevant columns 
   - Save relevant columns as `Raw_Data.csv`
     
**Task - 2: Data Quality and Cleaning**  led by Md Roknuzzaman
   - Load raw CARE crash data   
   - Handle missing values and encode variables  
   - Save cleaned dataset as `crash_2018_cleaned.pkl`

**Task - 3: Univariate EDA** led by Kwaku Emmanuel Tufuor
   - Summary statistics and distributions  
   - Crash severity frequency analysis  
   - Visual exploration of roadway, environmental, and traffic factors  

**Task - 4: Bivariate EDA** led by Md Roknuzzaman
   - Analysis of severity vs other factors 
   - Cross-tabulations and conditional probabilities
   - Visual explorations 

**Task - 5: Multivariate Analysis and Transformations** led by Md Roknuzzaman and Kwaku Emmanuel Tufuor
   - Analysis of correlation matrix 
   - Explore pairwise relationship

**Task - 6: Conclusion, Interpretation and Presentation** led by Md Roknuzzaman and Kwaku Emmanuel Tufuor
   - Make concluding remarks 
   - Prepare Streamlit dashboard for presentation  

## Methodology
- Cleaned variables are encoded consistently (categorical normalization, boolean flags where appropriate).
- Intermediate cleaned data is stored with **pickle** to preserve data types and ensure reproducibility.
- Analysis uses descriptive statistics, visualization, and pattern identification methods.
- All code is formatted with **ruff** for styling consistency.
- Notebook outputs are automatically stripped using **nbstripout** to prevent merge conflicts.

## Research Questions
We aim to answer the following questions:
- How does crash severity vary with roadway conditions?
- What environmental conditions are associated with higher severity crashes?
- How do driver and crash mechanism variables relate to severity?
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


## Expected Outcomes
- Identification of the most influential roadway, environmental, and traffic conditions associated with severe crashes.  
- Visual and statistical summaries of patterns influencing crash severity.  
- A cleaned, well-documented dataset suitable for further modeling and safety analysis.

