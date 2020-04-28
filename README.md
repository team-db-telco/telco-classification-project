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
        - split_my_data(df, percentage)
    - Handle missing & null values
        - handle_nulls(df)
    - Handle outliers
        - Decided outliers were not an issue in this dataset
    - Encode variables: gender, churn, churn payment type
        - boolean_labeler(df, col)
        - more_than_two_labels(df, col)
        - payment_type(df)
    - Scale data
        - uniform_scaler(train, valid, test)
    - New features: 
        1. tenure in years
            - months_to_years(df, col)
        2. Single variable representing the information from phone_service and multiple_lines
            - extra_lines(df)
        3. Single variable representing info from dependents and partner
            - family_support(df)
        4. other ways to merge variables, such as streaming_tv & streaming_movies, online_security & online_backup
            - has_internet(df)
            - internet_services(df)
- Goal: a jupyter notebook that explores the above issues, documents plans to address them, and uses the functions 
    - prepare.ipynb
- Goal: Data Dictionary
    1. 'customer_id' : original feature from SQL database. Unique id for each customer.
    2. 'churn' : original feature from SQL database. Indicates whether or not the customer has canceled services.
    3. 'churn_enc' : Boolean feature (0='No', 1='Yes'), encoded from churn feature. Created using boolean_labeler function found in prepare.py. 
    4. 'tenure' : original feature from SQL database. Value indicates number of months the customer has been with the company.
    5. 'tenure_years' : Calculated feature, value indicates the number of years the customer has been with the company. Created using months_to_years function found in prepare.py. 
    6. 'tenure_nml' : Calculated feature, value indicates a scaled version of the amount of time the customer has been with the company. Created using uniform_scaler function found in prepare.py. 
    7. 'monthly_charges' : original feature from SQL database. Value indicates amount each customer pays each month.
    8. 'monthly_charges_nml' : Calculated feature, value indicates a scaled version of the amount each customer pays each month. Created using uniform_scaler function found in prepare.py.
    9. 'total_charges' : original feature from SQL database. Value indicates total amount the customer has paid since joining the company.
    10. 'total_charges_nml' : Calculated feature, value indicates a scaled version of the total amount the customer has paid since joining the company. Created using uniform_scaler function found in prepare.py.
    11. 'senior_citizen' : original feature from SQL database. Boolean feature (0='No', 1='Yes').
    12. 'gender_enc' : Label encoded feature (0='Female', 1='Male'), generated with the boolean_labeler function in prepare.py. 
    13. 'family_support' : Calculated feature (0='Neither partner nor dependents', 1='Partner', 2='Partner & Dependents', 3='Dependents'), generated with the family_support function in prepare.py.
    14. 'phone_service_enc' : Boolean feature (0='No', 1='Yes'), encoded from original phone_service feature. Created using boolean_labeler function found in prepare.py. 
    15. 'contract_type_id' : original feature from SQL database. Value indicates the type of contract ()
    16. 'internet_service_type_id' : original feature from SQL database. Value indicates the type of internet service the customer has (1='DSL', 2='Fiber Optic', 3='None')
    17. 'extra_lines' : Calculated feature, value indicates the number of phone lines the customer has (0='No phone', 1='Single line', 2 ='Multiple Lines'). Feature generated with extra_lines function found in prepare.py
    18. 'internet_services' : Calculated feature, value indicates the number of extra internet services the customer has (0='No internet', 1='Internet only', 2 - 7 = Extra services). Extra services can include any of the following (online security, online backup, tech support, steaming tv, streaming movies, device protection). Feature generated with internet_services function found in prepare.py
    19. 'has_internet' : Boolean feature (0='No', 1='Yes'), encoded from original internet_service_type_id feature. Created using has_internet function found in prepare.py. 
    20. 'online_security_enc' : Boolean feature (0='No', 1='Yes'), encoded from original online_security feature. Created using more_than_two_labels function found in prepare.py. 
    21. 'online_backup_enc' : Boolean feature (0='No', 1='Yes'), encoded from original online_security feature. Created using more_than_two_labels function found in prepare.py. 
    22. 'device_protection_enc' : Boolean feature (0='No', 1='Yes'), encoded from original device_protection feature. Created using more_than_two_labels function found in prepare.py. 
    23. 'tech_support_enc' : Boolean feature (0='No', 1='Yes'), encoded from original tech_support feature. Created using more_than_two_labels function found in prepare.py. 
    24. 'streaming_tv_enc' : Boolean feature (0='No', 1='Yes'), encoded from original streaming_tv feature. Created using more_than_two_labels function found in prepare.py. 
    25. 'streaming_movies_enc' : Boolean feature (0='No', 1='Yes'), encoded from original streaming_movies feature. Created using more_than_two_labels function found in prepare.py. 
    26. 'paperless_billing_enc' : Boolean feature (0='No', 1='Yes'), encoded from original paperless_billing feature. Created using boolean_labeler function found in prepare.py. 
    27. 'pay_elec_check' : Boolean feature (0='No', 1='Yes'), encoded from original paperless_billing feature. Created using boolean_labeler function found in prepare.py.
    28. 'pay_mail' : Boolean feature (0='No', 1='Yes'), encoded from original payment_type feature. Created using payment_type function found in prepare.py.
    29. 'pay_bank' : Boolean feature (0='No', 1='Yes'), encoded from original payment_type feature. Created using payment_type function found in prepare.py.
    30. 'pay_cc' : Boolean feature (0='No', 1='Yes'), encoded from original payment_type feature. Created using payment_type function found in prepare.py.
    31. 'pay_auto' : Boolean feature (0='No', 1='Yes'), encoded from original payment_type feature. Created using payment_type function found in prepare.py.

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