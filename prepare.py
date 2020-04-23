import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def split_my_data(df, train_pct):
    '''
    Takes in df, train_pct and returns 2 items:
    train, test

    When using this function, in order to have usable datasets, be sure to call it thusly:
    train, test = split_my_data(df, train_pct)
    '''
    return train_test_split(df, train_size = train_pct, random_state = 294)

#### Handle Nulls Function ####
def handle_nulls(df):
    df.total_charges = df['total_charges'].fillna(df['monthly_charges'])
    return df

#### Encoder Functions ####
def payment_type(df):
    df['pay_elec_check'] = np.where(df.payment_type == 'Electronic check', 1, 0)
    df['pay_mail'] = np.where(df.payment_type == 'Mailed check', 1, 0)
    df['pay_bank'] = np.where(df.payment_type == 'Bank transfer (automatic)', 1, 0)
    df['pay_cc'] = np.where(df.payment_type == 'Credit card (automatic)', 1, 0)
    df['pay_auto'] = np.where(df.payment_type == 'Credit card (automatic)', 1,
                               np.where(df.payment_type == 'Bank transfer (automatic)', 1, 0))
    return df

def boolean_labeler(df, col):
    le = preprocessing.LabelEncoder()
    df[f'{col}_enc'] = le.fit_transform(df[col])
    return df

def more_than_two_labels(df, col):
    df[f'{col}_enc'] = np.where(df[col] == 'No', 0,
                                np.where(df[col] == 'Yes', 1, 0))
    return df

#### New Feature Functions ####
def months_to_years(df, col):
    df[f'{col}_months'] = (df[col] / 12).round(2)
    return df

def extra_lines(df):
    df['extra_lines'] = np.where(df['multiple_lines'] == 'Yes', 2,
                                np.where(df['multiple_lines'] == 'No', 1, 0))
    return df

def family_support(df):
    df['family_support'] = np.where( (df['partner'] == 'No') & (df['dependents'] == 'Yes'), 3,
                                    np.where( (df['partner'] == 'Yes') & (df['dependents'] == 'Yes'), 2,
                                             np.where( (df['partner'] == 'Yes') & (df['dependents'] == 'No'), 1, 0)))
    return df

def has_internet(df):
    df['has_internet'] = np.where(df.internet_service_type_id == 3, 0, 1)
    return df

def internet_services(df):
    df['internet_services'] = (df.has_internet + 
                               df.online_security_enc + 
                               df.online_backup_enc + 
                               df.tech_support_enc + 
                               df.streaming_tv_enc + 
                               df.streaming_movies_enc + 
                               df.device_protection_enc)
    return df

#### Scaler Function ####
def uniform_scaler(train, valid, test):
    '''
    Uses the train, valid & test datasets created by the split_my_data function
    First, make new dfs containing only those columns you want scaled, else this function will scale every numerical value, including booleans.

    This is a non-linear transformer, and it smooths out unusual distributions.
    It spreads out the most frequent values and reduces the impact of (marginal) outliers, therefore it is robust.
    It distorts correlations and distances within and across features.

    '''
    unf_scaler = preprocessing.QuantileTransformer(n_quantiles=100, output_distribution='normal', random_state=123, copy=True).fit(train)
    train = pd.DataFrame(unf_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    valid = pd.DataFrame(unf_scaler.transform(valid), columns=valid.columns.values).set_index([valid.index.values])
    test = pd.DataFrame(unf_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return unf_scaler, train, valid, test
