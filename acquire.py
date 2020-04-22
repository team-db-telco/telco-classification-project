import pandas as pd
import numpy as np

from env import host, user, password

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
    
def get_telco_data():
    '''
    Returns a telco dataframe that includes all tables
    joined on customers
    '''
    query = """
    SELECT *
    FROM customers
    JOIN payment_types using (payment_type_id)
    JOIN internet_service_types using (internet_service_type_id)
    JOIN contract_types using (contract_type_id)
    """
    df = pd.read_sql(query, get_db_url("telco_churn"))
    return df