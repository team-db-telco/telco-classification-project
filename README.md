## Telco Team Project

## Purpose
Why are our customers churning?

Some questions I have include:

1. Are there clear groupings where a customer is more likely to churn? 
2. Are there features that indicate a higher propensity to churn? 
3. Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point?
4. If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

## Deliverables
1. Report (jupyter notebook) answering the question:
    - "Why are our customers churning?"
    - I want to see the analysis you did to answer my questions and lead to your findings. Please clearly call out the **questions** and **answers** you are analyzing. 
    - End of notebook will produce .csv file with the customer_id, probability of churn, and the prediction of churn (1=churn, 0=not_churn).
2. Presentation: [Link] ()
    - Illustrates how your model works
        - Include the features being used
        - Include how likely your model is to give a high probability of churn when churn doesn't occur, to give a low probability of churn when churn occurs, and to accurately predict churn.
3. Multiple .py files with their associated notebooks
    - aqcuire.py
    - prepare.py
    - model.py
4. Github Repository: [Link](https://github.com/team-db-telco/telco-classification-project)
    - Readme (this file)
    - Final Jupyter notebook walking through the pipeline
    - .py files with all functions necessary to reproduce the model

## Pipeline

# Planning
- Hypotheses:
    1. Are there clear groupings in tenure where a customer is more likely to churn? 
    - $H_0$: There are no cohorts who have a higher rate of churn than other cohorts
    - $H_a$: There is a cohort with a higher rate of churn than others
    2. Are there features that indicate a higher propensity to churn? 
    - $H_0$: There are no features who have a higher rate of churn than other features
    - $H_a$: Senior citizens have a higher rate of churn 
    - $H_a$: Month-to-month contracts have a higher rate of churn 
    - $H_a$: Two-year contracts have a higher rate of churn
    - $H_a$: People that pay by electronic check have a higher rate of churn 
    - $H_a$: 
    3. Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point?
    - $H_0$: There is no price threshold for specific services where the likelihood of churn increases
    - $H_a$: Higher price phone services are more likeley to churn
    4. If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?
    - $H_0$: Month-to-month customers and 1-year contract customers are equally likely to churn after the 12th month
    - $H_a$: Month-to-month customers are more likely to churn after the 12th month than 1-year contract customers
    - $H_a$: 1-year contract customers are more likely to churn after the 12th month than month-to-month customers

- New Hypotheses:
    -  
- Failed to reject Hypotheses:
    - 
- Rejected Hypotheses:
    - 

# Acquire Data
- Goal: a prepared dataframe
    - Create a file called acquire.py with all necessary functions to generate this dataframe from SQL

# Data Preparation
- Goal: prepared dataframe using the functions listed below, found in prepare.py 
    - Split data into train/test
        - split_my_data()
    - Handle missing & null values
        - 
    - Handle outliers
        - 
    - Encode variables: gender, churn, churn payment type
        - 
    - Scale data
        - 
    - New features: 
        1. tenure in years
            - 
        2. Single variable representing the information from phone_service and multiple_lines
            - 
        3. Single variable representing info from dependents and partner
            - 
        4. other ways to merge variables, such as streaming_tv & streaming_movies, online_security & online_backup
            - 
- Goal: a jupyter notebook that explores the above issues, documents plans to address them, and uses the functions 
    - 
- Goal: Data Dictionary
    1. 

# Data Exploration
- Goal: Answer key questions
    1. If a group is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts? 
        - (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers))
    2. Are there features that indicate a higher propensity to churn? 
        - like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?
    3. Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?
    4. If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?
    5. Controlling for services (phone_id, internet_service_type_id, online_security_backup, device_protection, tech_support, and contract_type_id), is the mean monthly_charges of those who have churned significantly different from that of those who have not churned? 
        - (Use a t-test to answer this.)
    6. How much of monthly_charges can be explained by internet_service_type? 
        - (hint: correlation test). 
    7. How much of monthly_charges can be explained by internet_service_type + phone service type (0, 1, or multiple lines). 

- Goal: Create visualizations:
    - Explore the interactions of variables 
        - (independent with independent and independent with dependent)
        - The goal is to identify features that are related to churn, identify any data integrity issues, understand 'how the data works'. 
        - (The visualizations done in your analysis for questions 1-5 count towards the requirements below)
    - What can you say about each variable's relationship to churn, based on your initial exploration? 
    - If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
    - Summarize your conclusions, provide clear answers to the specific questions, and summarize any takeaways/action plan from the work above.

# Modeling
- Goal: Feature Selection
    - Remove any variables that seem to provide limited to no additional information
- Goal: Train (fit, transform, evaluate) multiple different models
- Goal: Compare evaluation metrics across all the models, and select the best performing model.
- Goal: Test the final model (transform, evaluate) on your out-of-sample data (the testing data set). 
    - Summarize the performance. 
    - Interpret your results.